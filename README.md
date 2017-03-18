# CS270-Project
Poetry Explorer lets you browse for poems based on special tags we generated as part of our CS 270 project

## Setup

To set up and run the program, please do the following.

1. Install required packages for Python.
   
   This step assumes you use the Python package manager [pip](https://pypi.python.org/pypi/pip).

   `pip install -r requirements.txt`
   
2. Download MongoDB and set it up on your local computer
   
   Follow the instructions for your Operating System. I have linked a few pages which detail how to set up the database on different platforms.
   
   ### Mac OS X
   
   [Installation Instructions for Mac OS X from official MongoDB page](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)
   
   ### Windows
   
   [Installation Instructions for Windows from official MongoDB page](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/)
   
   ### Linux
   
   For Ubuntu/Debian:
   [Installation Instructions for Ubuntu/Debian from official MongoDB page](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
   
   For Red Hat:
   [Installation Instructions for Red Hat from official MongoDB page](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/)
   
   For Arch Linux:
   
   Run the following in your terminal
   
       pacman -Syua mongodb
       sudo systemctl start mongodb.service
       
3. Load the MongoDB database with the poem data

   Run the following in your terminal
   
       python loadMongo.py
       
4. Run the server and connect to the webapp.

   Run the following in your terminal
   
       python app.py
       
   You should see output like
   
        * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   
   Now you can visit that link in your browser and use the app!
