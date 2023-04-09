from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to my web app!'

@app.route('/about')
def about():
    return 'This is an about page.'

@app.route('/user/<name>')
def user(name):
    return f'The point of {name} is 3.'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        username = request.form['username']
        password = request.form['password']
        # Check the credentials and grant access if valid
        return 'Login successful!'
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
