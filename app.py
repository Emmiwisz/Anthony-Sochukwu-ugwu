from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a random secret key

# Dummy users data
users = {
    'admin': 'password'
}

@app.route('/')
def home():
    if 'logged_in' in session:
        return redirect(url_for('product'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            session['logged_in'] = True
            return redirect(url_for('product'))
        else:
            return 'Invalid Credentials, Please try again!'
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return 'User already exists!'
        users[username] = password
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/product')
def product():
    if 'logged_in' in session:
        return render_template('product.html')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
