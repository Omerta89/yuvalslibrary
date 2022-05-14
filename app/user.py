from flask import Flask, Blueprint, redirect, render_template, request, url_for
from database import mydatabase
from datetime import date, timedelta
from unicodedata import name

user = Blueprint('user',__name__, url_prefix='/user')
dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname='CUSTOMERS.sqlite')




# first route - member
@user.route('/member/', defaults={'username': ''})
@user.route('/member/<username>')
def user_member(username):
    res = dbms.print_all_data_books(table=mydatabase.BOOKS)
    custid = dbms.print_id_data_customers(username,table= mydatabase.CUSTOMERS)
    return render_template("member.html",res=res, custid=custid, username=username)


@user.route('/member/<name>',methods=["POST","GET"])
def member(name):
    if request.method == "POST":
        searchName = request.form.get('searchName')
        bookfind = dbms.find_book_home(searchName,table=mydatabase.BOOKS)
        custid = dbms.print_id_data_customers(name,table= mydatabase.CUSTOMERS)
        return render_template('member.html',bookfind=bookfind,name=name,custid=custid[0])
    if request.method == "GET":
        res = dbms.print_all_data_books(table=mydatabase.BOOKS)
        custid = dbms.print_id_data_customers(name,table= mydatabase.CUSTOMERS)
        return render_template("member.html",name=name,res=res,custid=custid[0])








# add loan
@user.route('/addloan/', defaults={'name':''})
@user.route("/addloan/<name>")
def add_loan(name):
    custid = request.args.get('custid')
    bookid = request.args.get('bookid')
    today = date.today()
    res =  dbms.check_type(bookid)
    if res[0] == 1:
        tenDays = date.today() + timedelta(days=10)
        dbms.insert_loans(custid,bookid,today,tenDays)
        print(custid,bookid,today,tenDays)
    if res[0] == 2:
        fiveDays = date.today() + timedelta(days=5)
        dbms.insert_loans(custid,bookid,today,fiveDays)
        print(custid,bookid,today,fiveDays)
    if res[0] == 3:
        twoDays = date.today() + timedelta(days=2)
        dbms.insert_loans(custid,bookid,today,twoDays)
        print(custid,bookid,today,twoDays)
    print(custid,bookid,today,bookid)
    return user_member(name)





@user.route('/loanbook/',defaults={'book':'no loan was found'})
@user.route('/loanbook/<string:book>')
def user_loan_a_book(book):
     return  (f"return book: {book}")
 
 
 
 
 
 
 
 
# user func ...


@user.route('/retbook/',defaults ={"name":""})   
@user.route("/retbook/<name>")
def user_loans(name):
    res = dbms.print_data_loans(name,table= mydatabase.LOANS)
    return render_template("retbook.html",res=res,name=name)

@user.route("/retloan")
def retLoan():
    custid = request.args.get('custid')
    bookid = request.args.get('bookid')
    custname = request.args.get('custname')
    dbms.delete_by_id_loans(custid,bookid)
    return user_loans(custname)











# # half search
# @user.route('/search/', defaults={"res":'No book was found'})
# @user.route('/search/<string:res>')
# def user_search(res):
#     res= dbms.print_all_data(table= mydatabase.BOOKS)
#     return render_template ("search.html",res=res )

