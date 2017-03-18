class Poem:
    def __init__(self, pfid, title, author, html, plainText, categories = set()):
        self.pfid = pfid
        self.title = title
        self.author = author
        self.html = html # can be None
        self.plainText = plainText # can be None
        self.categories = categories

    def __str__(self):
        return str(self.__dict__)
    def __eq__(self, other):
        return self.pfid == other.pfid
    def __ne__(self, other):
        return not self == other
    def __hash__(self):
        return hash(self.pfid)
        
class Poet:
    def __init__(self, name, bio, categories = []):
        self.name = name
        self.bio = bio
        self.categories = categories

    def __str__(self):
        return str(self.__dict__)
    def __eq__(self, other):
        return self.bio == other.bio
    def __ne__(self, other):
        return not self == other
    def __hash__(self):
        return hash(self.bio)

class Category:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __str__(self):
        return str(self.__dict__)
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self == other
    def __hash__(self):
        return hash(self.name)
