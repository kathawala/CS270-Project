from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
import math

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'explorer'
mongo = PyMongo(app)

@app.route('/poem/')
@app.route('/poem/<int:pfid>')
@app.route('/poem/<int:pfid>/')
def displayPoem(pfid=None):
    if pfid:
        query = mongo.db.poems.find_one_or_404({ 'pfid' : pfid })
        return(render_template('display_poem.jinja2', poem=query))
    else:
        home()

@app.route('/browse')
def paginatePoemsByCategories():
    categories = request.args.getlist('category')
    page = int(request.args.get('page'))
    count = mongo.db.poems.find({ "categories" : { "$all": categories}}).count()
    pages = math.ceil(count / 10)
    query = mongo.db.poems.find({ "categories" : { "$all": categories}}).skip((page-1)*10).limit(10)
    mongoPoems = list(query)
    return(render_template('display_results.jinja2', results=mongoPoems, categories=categories, pages=pages, pg=page))
        
@app.route('/categories', methods=['POST'])
def browsePoemsByCategories():
    categories = []
    
    # Some hacky stuff because the Poetic Terms are returned as one string...
    pTerms = request.form.getlist('Poetic Terms')
    pTerms = pTerms[0].split(',')
    categories.extend(pTerms)
    
    # Some hacky stuff because the Subjects list is returned as one string...
    subjects = request.form.getlist('Subjects')
    subjects = subjects[0].split('|,')
    subjects = [x.replace('|','') for x in subjects]
    categories.extend(subjects)
    
    categories.extend(request.form.getlist('Occasions'))
    categories.extend(request.form.getlist('Holidays'))
    categories.extend(request.form.getlist('Events'))
    categories.extend(request.form.getlist('Identity'))
    categories.extend(request.form.getlist('School/Period'))
    categories.extend(request.form.getlist('Region'))
    categories = [x for x in categories if x is not '']
    count = mongo.db.poems.find({ "categories" : { "$all": categories}}).count()
    pages = math.ceil(count / 10)
    query = mongo.db.poems.find({ "categories" : { "$all": categories}}).limit(10)
    mongoPoems = list(query)
    return(render_template('display_results.jinja2', results=mongoPoems, categories=categories, pages=pages, pg=1))

@app.route('/')
def home():
    query = mongo.db.poems.aggregate( [{ "$sample": { "size": 1 }}] )
    poem = list(query)[0]
    poemObj = {"pfid": poem['pfid'], "title": poem['title'], "author": poem['author'], "html": poem['html']}
    return(render_template('random_poem.jinja2', poem=poemObj))

if __name__ == '__main__':
    app.run()