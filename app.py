from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import pymsgbox

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'admin'
#app.config['MONGO_URI'] = 'mongodb://sumanth:123456@127.0.0.1:27017/admin'
app.config['MONGO_URI'] = 'mongodb+srv://<admin>:<password>@cluster0-jtpxd.mongodb.net/admin'

mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        return render_template('user.html')

    return render_template('index.html')

@app.route('/logout')
def logout():
    session.clear()
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    user_name = request.form['username']

    users = mongo.db.users
    login_user = users.find_one({'name' : user_name})

    if login_user:
        if (request.form['pass'] == login_user['password']):
            session['username'] = user_name 
            return redirect(url_for('index'))

    return render_template('invalid.html')
    

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            username = request.form['username']
            pwd = request.form['pass']
            users.insert({'name' : username, 'password' : pwd})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        pymsgbox.alert('That username already exists!', 'Error')
        return 'That username already exists!'

    return render_template('register.html')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)
