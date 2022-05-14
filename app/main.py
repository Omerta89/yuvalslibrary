# Imports
from flask import Flask, render_template
from admin import admin
from user import user
from database import mydatabase
from flask import Flask, Blueprint, redirect, render_template, request, url_for
from variabledb import users, admins

api = Flask(__name__)
api.register_blueprint(admin)
api.register_blueprint(user)
dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname='CUSTOMERS.sqlite')


@api.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        searchName = request.form.get('searchName')    
        bookfind = dbms.find_book_home(searchName, table=mydatabase.BOOKS)
        print(bookfind)
        return render_template('home.html',bookfind=bookfind)
    if request.method == 'GET':
        searchName = request.form.get('searchName')    
        bookfind = dbms.find_book_home(searchName, table=mydatabase.BOOKS)
        print(bookfind)
        return render_template('home.html',bookfind=bookfind)



# about route
@api.route('/about')
def about():
    return render_template('about.html')

# booklist route, variable book passed to jinja
books=['book1','book2','book3']
@api.route('/booklist')
def booklist():
    return render_template('booklist.html', books=books)





@api.route('/addcustomer/', defaults={'name': ''})
# register func and route. gets register info, insert to db. and redirects to user/member/name from form.
@api.route("/addcustomer" , methods=["POST"])
def add_cust():
    name = request.form.get('name')
    city = request.form.get('city')
    age = request.form.get('age')
    dbms.insert_customer(name,city,age)
    return redirect(f"user/member/{name}")



@api.route('/login')
def login():
    return render_template("login.html")


# auth endpoint. gets username to variable username and checks if user in list users.
# if so redirects to newly created endpoint-member/username

@api.route('/auth',methods=["POST"])
def auth():
    username = request.form.get('username')
    password = request.form.get('password')
    if username in users:
        return redirect(f"user/member/{username}")
    elif username in admins:
        return redirect(f"admin/member/{username}")
    else:
        return render_template('failedauth.html')



if __name__ == '__main__':
    api.run(debug=True)