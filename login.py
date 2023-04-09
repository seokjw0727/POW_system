from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # check if username and password are valid
    if username == 'user' and password == 'pass':
        # redirect to welcome page
        return redirect(url_for('welcome'))
    else:
        return 'Invalid login information'

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)