import sqlite3
from flask import Flask, jsonify, render_template, request
from forms import contactForm
from forms import filterForm
from flask_mail import Mail, Message 

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'development key'

mail = Mail()
app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True 
app.config["MAIL_USERNAME"] = 'bastakilanguage@gmail.com'
app.config["MAIL_PASSWORD"] = 'qkzwxlnrmwgxrzgd'
mail.init_app(app)

def get_db_connection():
    conn = sqlite3.connect('bastaki.db')
    conn.row_factory = sqlite3.Row
    return conn

#get all items, only search if theres something to search 
def getitems_all(search):
    if len(search) >= 1: 
        conn = sqlite3.connect('bastaki.db')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM Master WHERE English LIKE ? OR [Bastaki Transliteration] LIKE ?",
            ("%"+search+"%", "%"+search+"%",)
        )
        results = cursor.fetchall()
        conn.close()
    elif len(search) == 0: 
        results = getAll()
    return results 

#get all items 
def getAll():
    conn = sqlite3.connect('bastaki.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Master")
    allData = cursor.fetchall()
    conn.close()
    return allData

#search function. looks for items to match search, otherwise don't return anything 
def getitems(search):
    if len(search) >= 1: 
        conn = sqlite3.connect('bastaki.db')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM Master WHERE English LIKE ? OR [Bastaki Transliteration] LIKE ? OR [Additional Classifier] LIKE ?",
            ("%"+search+"%", "%"+search+"%","%"+search+"%",)
        )
        results = cursor.fetchall()
        conn.close()
    else: 
        results = []
    return results 

#selects the part of speech 
def getPartofSpeech(pos):
    if pos == "pronoun" or pos == "noun" or pos == "verb" or pos == "adjective" or pos == "preposition" or pos == "adverb" or pos == "culture": 
        conn = sqlite3.connect('bastaki.db')
        cursor = conn.cursor()
        cursor.execute(
            #"SELECT * FROM Master WHERE [Part of Speech] LIKE ?",
            "SELECT * FROM Master WHERE [Part of Speech]=?",
            #("%"+pos+"%",)
            (pos,)
        )
        results = cursor.fetchall()
        conn.close() 
    elif pos == "culture":
        conn = sqlite3.connect('bastaki.db')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM Master WHERE [Part of Speech] LIKE ?",
            ("%"+ pos +"%",)
        )
        results = cursor.fetchall()
        conn.close()
    else:
        results = getAll()
    return results 

#find intersection between 2 lists 
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

@app.route('/', methods=["GET","POST"])
#@app.route('/')
def index():
  # SEARCH RESULTS 
    if request.method == "POST":
        #data = dict(request.form)
        #items = getitems(data['indsearch'])
        #print(items)
        data = request.form.get("indsearch")
        items = getitems(data)
    else:
        items = []
    return render_template('index.html', itm=items)


@app.route('/process/', methods=["GET", "POST"])
def process():
      # SEARCH RESULTS 
    if request.method == "POST":
        data = request.form.get('searchdata')
        print(data)
        items = getitems(data)
    else:
        items = []
    return render_template('process.html', itm=items)


'''
@app.route('/dictprocess/', methods=["GET", "POST"])
def dictprocess():
    # SEARCH RESULTS 
    if request.method == "POST":
        data = request.form.get('dictdata')
        print(data)
        items = getitems(data)
    else: 
        items = getAll()
    return render_template('dictprocess.html', itm = items)



@app.route('/dictionary/')
def dictionary():
    return render_template('dictionary.html')

'''
@app.route('/dictionary/', methods=["GET", "POST"])
def dictionary():
    #form = filterForm()
    if request.method == "POST":
        pos = request.form.get("partofspeech")
        data = request.form.get("dictsearch")
        if pos == "pronoun" or pos == "noun" or pos == "verb" or pos == "adjective" or pos == "preposition" or pos == "adverb" or pos == "culture": 
            words = getPartofSpeech(pos)
        else:
            words = getAll()
        if len(data) >= 1:  
            words2 = getitems_all(data)
        else:
            words2 = getAll()
        items = intersection(words,words2)     
    else: 
        items = getAll()
    return render_template('dictionary.html', itm = items)

    
@app.route('/info/')
def info():
    return render_template('info.html')

@app.route('/contact', methods = ['GET','POST'])
def contact():
    form = contactForm()
    if request.method == 'POST':
        subject = request.form.get("subject")
        email = request.form.get("email")
        message = request.form.get("message")
        msg = Message(subject, sender='bastakilanguage@gmail.com', recipients=['narmeenzain@pm.me'])
        msg.body = """ 
From: %s <%s>
%s
""" % (subject, email, message)
        mail.send(msg)
        return render_template('contact.html', success=True)
        #return 'form posted'
    elif request.method == 'GET':
        return render_template('contact.html', form = form)


# sanity check route
@app.route('/badabing', methods=['GET'])
def ping_pong():
    return jsonify('badaboom')

if __name__ == '__main__':
    app.run()
