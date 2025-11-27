from flask import Flask, request, render_template, redirect, url_for
app = Flask (__name__)

@app.route('/home', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST': 
        username = request.form['Username']
        password = request.form['password']
        return redirect('/')
    else:
        return render_template ('home.html', username=username)

@app.route ('/')
def titlepage():
    return render_template('titlepage.html')

@app.route ('/about')
def about():
    return render_template('about.html')

@app.route ('/contact')
def contact():
    return render_template('contact.html')

@app.route ('/createaccount')
def createaccount ():
    return render_template('createaccount.html')

@app.route ('/login')
def login ():
    return render_template('login.html')

@app.route ('/test')
def test ():
    return render_template('test.html')

@app.route ('/backend')
def backend ():
    return render_template('backend.py')

if __name__ == '__main__':
    app.run(debug=True)