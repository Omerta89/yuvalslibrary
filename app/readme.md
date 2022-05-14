to install all packages, run in terminal: pip install -r requirements. txt



* Project status: working/prototype
- just starting at 8/4. this is a prototype.
- 22.4 - implement DB by flask

# TODO



25/4 

  admin: 
        add book - DONE - (instancetiate from books page)
        delete book- DONE - (instancetiate from books page)
26/4
        add customer - DONE
        del customer - DONE

        delete loan - DONE
   user:
        loan book - 





implement DB by flask
        add • Display all customers - at admin route index as a button
        which routes to /admin/display - do i have to generate a specific page or can it auto generate?










add a new customer
dbms.insert_customer('yuval', 'roshha', 32)


- layout.html - from bootstrap use css+nav bar - done

home page -> button to display all books
admin login

 - flow chart - DONE
 (think about table+rows names, table relations (PK+FK))
 (what should the method return-which page)

- tables - insert and print is manually by script - in progress

- INFRASTRUCTURE
 define methods against DB (CRUD-search,delete) - in progress

 blueprint names (user,admin) - done
 
 Build a class for each entity (books,customers,loans)

 - start with tables - data. what should the method recieve (()) by table. what should it show - working in terminal

### Features
in general i will be implementing CRUD

Add the following operations (display a simple menu)
•	Add a new customer
•	Add a new book
•	Loan a book
•	Return a book
•	Display all books
•	Display all customers
•	Display all loans
•	Display late loans
•	Find book by name
•	Find customer by name
•	Remove book
•	Remover customer

### Content (Description, sub-modules organization...)

In this project you will implement a simple system to manage books library

1.	Create a simple sqlite database with 3 tables:
•	             (Books )
•	Id (PK)
•	Name
•	Author 
•	Year Published 
•	Type (1/2/3)
•	           (Customers)
•	CustId (PK)
•	Name
•	City
•	Age
•	             (Loans)
•	CustID 
•	BookID
•	Loandate
•	Returndate
2.	The book type set the maximum loan time for the book:
•	1 – up to 10 days
•	2 – up to 5 days
•	3 – up to 2 days
3.	Create the DAL:
•	Build a class for each entity
•	Create a separate module for each class
•	Build unit tests 

# TO Rememeber
* programmer test unit (print to terminal)
* use existing DB. using a method - there are queries that check if there is data and if not it enters data. (if data, continue, if not, add)
* develop working patterns (maybe code in jupiter)

# For later
- add deploy instructions to user in readme.
- upload to github in the end.


# Title / Repository Name
Books_course_project1

## About / Usage
this application is supposed to manage a simple book library. 

* What is it, what does it do / Abstract
Build a client application to use the DAL (from project file instruction). i will be using flask as logic and html as gui and sql-alchemy as database managment. sqlite3 as SQL database.

* this is what i will use
i will use dal to handle the database part. (from google): Segregating the data access code to allow better maintainability and easy migration of database if needed.
i will use flask to build a development server to upload the program to the web and allows fast debugging at real time. also, use blueprints (object in flask) to divide the program
i will use html in order to let the user view the program online.
i will be working in a virtual enviorment


## Table of contents

> * [Title / Repository Name](#title--repository-name)
> * [About / Usage](#about--Usage)
> * [Table of contents](#table-of-contents)
> * [Installation/Requirements](#installation)
> * [Screenshots](#screenshots)
> * [Features](#features)
> * [Content](#content)
> * [Deploy (how to install build product)](#deploy-how-to-install-build-product)
> * [Resources (Documentation and other links)](#resources-documentation-and-other-links)
> * [About The Programmer](#about-Yuval)

## Installation/Requirements
alchemy module. sqlite3. flask. python version __
* From the __ Marketplace: install [package](link). 
* From the command line: `nuxeoctl mp-install nuxeo-sample`

### Screenshots
to add:
 1. table relation from gliffy "C:\python course 8\project1_books\static\python_project_relation_tables.jpg"
 2. pages relations (redirects) from same gliffy file


### Deploy (how to install build product)

* remember that user (eyal) clones repository from git and runs URL
* for me - try to run from a clean computer 

* instructions 
what link to press or where to start
what to excpect
the first page you will land is...
what you need to enter is...(username)
what tests are ready to check




 > for example -(Copy the built artifacts into `$NUXEO_HOME/templates/custom/bundles/` and activate the `custom` template.)

## Resources (Documentation and other links)
i have the support of colleagues using zoom to work together and the support of john bryce instructor. examples from programming forums.
Database Model @mahmudahsan. Source: https://github.com/zzzeek/sqlalchemy/
- Install Library alchemy
http://docs.sqlalchemy.org/en/latest/intro.html#installation
Windows:
pip install SQLAlchemy 


## About the programmer

Yuval Sherman is a junior programmer with python language.
Enrolled in python course at john bryce technical college.
points of intreset are...
is an open source. Data can be stored in both SQL