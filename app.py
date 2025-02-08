from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Default credentials
USERNAME = 'admin@gmail.com'
PASSWORD = 'admin'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['email']
    password = request.form['password']
    if username == USERNAME and password == PASSWORD:
        session['user'] = username
        return redirect(url_for('home'))
    return "Invalid credentials, please try again."

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/home')
def home():
    if 'user' in session:
        return render_template('home.html', username=session['user'])
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
