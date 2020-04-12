import cgi, cgitb


form = cgi.FieldStorage()

first_name = form.getvalue('usrname')
last_name  = form.getvalue('psw')

print(first_name , last_name)
