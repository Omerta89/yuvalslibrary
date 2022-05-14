from flask import Flask, Blueprint, redirect, render_template, request, url_for
from database import mydatabase

admin = Blueprint('admin',__name__, url_prefix='/admin')
dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname='CUSTOMERS.sqlite')



# page home to link (manage add/remove/update) methods

@admin.route('/member/<username>/', defaults={'username': ''})
@admin.route('/member/<username>')
def admin_member(username=""):
    res = dbms.print_all_data_books(table=mydatabase.BOOKS)
    custid = dbms.print_id_data_customers(username,table= mydatabase.CUSTOMERS)
    
    return render_template("adhome.html",res=res, custid=custid, username=username)



# pages

# page books
@admin.route('/member/<username>/books/', defaults={'username': ''})
@admin.route('/member/<username>/books')
def admin_member_books(username=""):
    res = dbms.print_all_data_books(table=mydatabase.BOOKS)
    return render_template("adbooks.html",username=username,res=res)


# page customers to show all customers
@admin.route('/member/<username>/customers/', defaults={'username': ''})
@admin.route('/member/<username>/customers')
def admin_member_cust(username=""): 
    res =dbms.print_all_data_customers(table= mydatabase.CUSTOMERS)
    custid = dbms.print_id_data_customers(username,table= mydatabase.CUSTOMERS)
    return render_template("adcust.html",username=username,res= res,cust=custid)


# page loans (link it) to show admin loans and instanceiatiate del,add methods.
@admin.route('/member/<username>/loans/', defaults={'username':''})
@admin.route('/member/<username>/loans')
def admin_member_loans(username=""):
    res = dbms.print_all_data_loans(table= mydatabase.LOANS)
    custid = dbms.print_id_data_customers(username,table= mydatabase.CUSTOMERS)
    return render_template("adloans.html",username=username,res=res,custid=custid)




@admin.route('/books/<username>',methods=["POST","GET"])
def admin_search_books(username="test"):
    if request.method == "POST":
        searchName = request.form.get('searchName')
        bookfind = dbms.find_book_home(searchName,table=mydatabase.BOOKS)
        print(bookfind)
        return render_template('adbooks.html',bookfind=bookfind,username=username)
    if request.method == "GET":
        res = dbms.print_all_data_books(table=mydatabase.BOOKS)
        return render_template('adbooks.html',username=username,res=res)





@admin.route('/customers/<username>',methods=["POST","GET"])
def admin_search_cust(username="test"): 
    if request.method == "POST":
        searchName = request.form.get('searchName')
        bookfind = dbms.find_book_home(searchName,table=mydatabase.CUSTOMERS)
        print(bookfind)
        return render_template('adcust.html',bookfind=bookfind,username=username)
    if request.method == "GET":
        res =dbms.print_all_data_customers(table= mydatabase.CUSTOMERS)
        return render_template("adcust.html",username=username,res= res)



# methods

# add book
@admin.route("/addbook",methods=["POST", "GET"])
def admin_add_book():
    name = request.form.get('name')
    author = request.form.get('author')
    yearpublished = request.form.get('yearpublished')
    loantype = request.form.get('loantype')
    print(name,author,yearpublished,loantype)
    dbms.insert_books(name,author,yearpublished,loantype)
    return admin_member_books()


# add cust
@admin.route("/addcust",methods=["POST"])
def admin_add_cust():
    name = request.form.get('name')
    city = request.form.get('city')
    age = request.form.get('age')
    print(name,city,age)
    dbms.insert_customers(name,city,age)
    return admin_member_cust()


# delete book
@admin.route("/delbook")
def deleteBook():
    bookid = request.args.get('bookid')
    dbms.delete_by_id_books(bookid)
    print(f'delete by id {{dbms.delete_by_id_books(bookid)}}')
    return admin_member_books()

# delete customer
@admin.route("/delcust")
def deleteCust():
    custid = request.args.get('custid')
    dbms.delete_by_id_customers(custid)
    return admin_member_cust()

# delete loan
@admin.route("/delloan")
def deleteLoan():
    custid = request.args.get('custid')
    bookid = request.args.get('bookid')
    dbms.delete_by_id_loans(custid,bookid)
    return admin_member_loans()


# how to search
@admin.route('/search')
def admin_search():
    return ("admin search")




# unfinished thoughts:

# old member func. maybe smth to learn
# @admin.route('/member/', defaults={'username': 'username not found'})
# @admin.route('/member/<username>')
# def admin_member(username):
#     context={"username":username}
#     return render_template("member222.html",context=context)

# # route inside a route. make to do specific to user
# @admin.route('/member/<username>/loadallusers', methods=['GET', 'POST'])
# def admin_load(username):
#     context={"username":username,"position":users.index(username)}
#     return render_template("member.html",context=context)

# Display all customers function


# admin from meir
# users = ["test",1234]
# @admin.route("/auth",methods=["POST"])
# def auth():
#     username = request.form.get('username')
#     password = request.form.get('password')
#     if(username in users):
#         return redirect(f"books/{username}")
#     else:
#         return render_template("login.html")
    