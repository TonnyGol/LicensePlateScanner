from flask import request, redirect

@app.route('https://tonnygol.github.io/LicensePlateScanner/new.py', methods = ['POST'])
def signup():
    userName = request.form['usrname']
    passWord = request.form['psw']
    print("The username and password are" + userName + passWord)
    return redirect('https://tonnygol.github.io/LicensePlateScanner/page.html')
