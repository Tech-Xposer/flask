from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/thecodingganja'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '6IOfGlFQwHEr8_WZT86J1w'
db = SQLAlchemy(app)

class Contacts(db.Model):
    #sno,name,email,phone_no,mes,date
    sno = db.Column(db.Integer,primary_key=True)
    phone_num = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    mes = db.Column(db.String(500), nullable=False)
    # date= db.Column(db.String(12),nullable=True)

@app.route('/contact',methods = ['POST', 'GET'])
def contact():
    if request.method == 'POST':
        #fetching details
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('msg')
        
        #adding entries to db
        entry = Contacts(name=name, phone_num=phone, email=email, mes=message)
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html') 

if __name__ == "__main__":
    app.run(host='localhost', port=5000,debug=True)
