from flask import Flask, render_template
from database import mydatabase

# # connection to file mydatabase
dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname='CUSTOMERS.sqlite')

# dbms = customerstable.CCustomers(customerstable.SQLITE, dbname='CUSTOMERS.sqlite')


res= dbms.print_all_data(table= mydatabase.BOOKS)
print(res)
# dbms.print_all_data(customerstable.CUSTOMERS)

dbms.insert_books('The apple', 'shimon', 2010, 2)



# #     # Create Tables
# dbms.create_db_tables()

# dbms.print_all_data(customerstable.CUSTOMERS)


# # dbms.insert_single_data()
# # dbms.print_all_data(mydatabase.ADDRESSES)
# dbms.insert_customer('yuval', 'roshha', 32)


dbms.insert_loans(6, 2, 8, 12)

# dbms.print_all_data(table= mydatabase.LOANS)

# dbms.print_all_data(query= f"select color from '{mydatabase.LOANS}'")
# # dbms.delete_by_id(mydatabase.CARS,2 )


# dbms.delete_by_id_books(bookid)
# dbms.delete_by_id_loans('None','None')


# dbms.sample_query() # simple query

# dbms.second_sample_query()

    # # dbms.sample_delete() # delete data
    # # dbms.sample_insert() # insert data
    # # dbms.sample_update() # update data


# generate mock data
# from faker import Faker
# # fake= Faker()
# # for name in range(20):
# #     print(fake.age())