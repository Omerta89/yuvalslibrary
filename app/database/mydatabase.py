from datetime import date, datetime, timedelta
from sqlalchemy.orm import relationship
from flask import Flask 
from sqlalchemy import DATE, create_engine, false
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

SQLITE = 'sqlite'

# Table Names
CUSTOMERS = 'customers'
LOANS = 'loans'
BOOKS ='books'


class MyDatabase:
    DB_ENGINE = {SQLITE: 'sqlite:///app/database/{DB}'}

    # Main DB Connection Ref Obj
    db_engine = None

    def __init__(self, dbtype, username='', password='', dbname=''):
        dbtype = dbtype.lower()

        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)

            self.db_engine = create_engine(engine_url)
            print(self.db_engine)
                    
        else:
            print("DBType is not found in DB_ENGINE")

    def create_db_tables(self):
        metadata = MetaData()
        customers = Table(CUSTOMERS, metadata,
                      Column('custid', Integer, primary_key=True),
                      Column('name', String(20,unique=True,nullable=False)),
                      Column('city', String),
                      Column('age', Integer),
                      )

        loans = Table(LOANS, metadata,
                      Column('custid', None, ForeignKey('customers.custid')),
                      Column('bookid', None, ForeignKey('books.bookid')),
                      Column('loandate', DATE),
                      Column('returndate', DATE),
                      )

        books = Table(BOOKS, metadata,
                        Column('bookid', Integer, primary_key=True),
                        Column('name', String, nullable=False),
                        Column('author', String),
                        Column('yearpublished', Integer),
                        Column('loantype', Integer)
                        )

        try:
            metadata.create_all(self.db_engine)
            print("Tables created")
        except Exception as e:
            print("Error occurred during Table creation!")
            print(e)

    # Insert, Update, Delete
    
    # looks to me like simple print query = SEARCH
    def execute_query(self, query=''):
        if query == '' : return

        print (query)
        
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)


    def print_all_data(self, table='', query=''):
        query = query if query != '' else f"SELECT * FROM '{table}';"
        print(query)
        res = []
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    res.append(row)
                    print(row) # print(row[0], row[1], row[2])
                result.close()
        # print("\n")
        return res



    def find_book_home(self,name, table='', query=''):
        query = query if query != '' else f"SELECT * FROM '{table}' WHERE name LIKE '%{name}%' ;"
        print(query)
        res = []
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    res.append( row)
                    # print(row) # print(row[0], row[1], row[2])
                result.close()
        # print("\n")
        return res




# altering func to print book data
    def print_all_data_books(self, table='', query=''):
        query = query if query != '' else f"SELECT * FROM '{table}';"
        print(query)
        res = []
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    res.append(row)
                    print(row) # print(row[0], row[1], row[2])
                result.close()
        # print("\n")
        return res


#  altering to call print general func. recieves parameter 'name'. and sql statment narrows search.
#  sql =  SELECT custid FROM '{table}' WHERE name ='{name}'
    def print_id_data_customers(self,name,table='',query=''):
        query= query if query != '' else f"SELECT custid FROM '{table}' WHERE name= '{name}';"
        print(query)
        res = []
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                 for row in result:
                    res.append( row)
                    # print(row) # print(row[0], row[1], row[2])
                 result.close()
         # print("\n")
        return res
    

# check type
    def check_type(self,bookid,query=''):
        query = query if query != '' else f"SELECT loantype FROM BOOKS WHERE bookid = {bookid};"
        print(query)
        res = []
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    res.append( row)
                    # print(row) # print(row[0], row[1], row[2])
                result.close()
        # print("\n")
        return res[0]


                #  PRINT ALL *CUSTOMERS*
    def print_all_data_customers(self, table='', query=''):
        query = query if query != '' else f"SELECT * FROM '{table}';"
        print(query)
        res = []
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    res.append( row)
                    # print(row) # print(row[0], row[1], row[2])
                result.close()
        # print("\n")
        return res


            # PRINT ALL *LOANS*
    def print_all_data_loans(self, table='', query=''):
        query = query if query != '' else f"SELECT * FROM {table};"
        print(query)
        res = []
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    res.append( row)
                    # print(row) # print(row[0], row[1], row[2])
                result.close()
        # print("\n")
        return res
    
    
    
    
    
    def print_data_loans(self,name, table='', query=''):
        query = query if query != '' else \
         f"SELECT LOANS.loandate,LOANS.returndate, Customers.name as custname, BOOKS.name, BOOKS.bookid as bookid, Customers.custid as custid \
            FROM (({table}   \
            INNER JOIN Customers ON LOANS.custid = Customers.custid) \
            INNER JOIN BOOKS ON LOANS.bookid = BOOKS.bookid) \
            where Customers.name = '{name}';"
        print(query)
        res = []
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    res.append( row)
                # print(row) # print(row[0], row[1], row[2])
                result.close()
             # print("\n")
            return res
        
    


            # Insert Data to customers .insert_customers
    def insert_customers(self, name, city, age):
        query = f"INSERT INTO CUSTOMERS(name, city, age) " \
                f"VALUES ('{name}','{city}', {age});"
        # print(query)
        self.execute_query(query)
        # self.print_all_data(CUSTOMERS)



            # DEL DEF. 
        # Delete Data by Id *LOANS*
    def delete_by_id_loans(self,custid,bookid):
        query = f"DELETE FROM LOANS WHERE custid={custid} and bookid={bookid}"
        self.execute_query(query)


        # Delete Data by Id *CUSTOMERS*
    def delete_by_id_customers(self,id):
        query = f"DELETE FROM CUSTOMERS WHERE custid={id}"
        self.execute_query(query)

            # Delete Data by Id *BOOKS*
    def delete_by_id_books(self,id):
        query = f"DELETE FROM BOOKS WHERE bookid={id}"
        self.execute_query(query)
        # self.print_all_data(table)






    # Examples

    def sample_query(self):
        # Sample Query
        query = "SELECT name, custid FROM CUSTOMERS WHERE " \
                "name LIKE 'y%';"
        self.print_all_data(query=query)

        # Sample Query Joining
        query = "SELECT c.name as name, " \
                "l.loandate as loan_date, l.returndate as return_date " \
                "FROM {TBL_CSTR} AS c " \
                "LEFT JOIN {TBL_LNS} as l " \
                "WHERE c.custid=l.custid AND c.name LIKE 'y%';" \
            .format(TBL_CSTR=CUSTOMERS, TBL_LNS=LOANS)
        self.print_all_data(query=query)


    def second_sample_query(self):
        # Sample Query Joining
        query = "SELECT b.author as author, " \
                "l.loandate as loan_date, l.returndate as return_date " \
                "FROM {TBL_BK} AS b " \
                "RIGHT JOIN {TBL_LNS} as l " \
                "WHERE b.bookid=l.bookid" \
            .format(TBL_BK=BOOKS, TBL_LNS=LOANS)
        self.print_all_data(query=query)


    def delete_by_id(self,table,id):
        # Delete Data by Id
        
        query = f"DELETE FROM {table} WHERE id={id}"
        self.execute_query(query)
        self.print_all_data(CUSTOMERS)


    def sample_delete(self):
        # Delete Data by Id
        query = f"DELETE FROM {CUSTOMERS} WHERE id=3"
        self.execute_query(query)
        self.print_all_data(CUSTOMERS)

        # Delete All Data
        '''
        query = "DELETE FROM {}".format(CUSTOMERS)
        self.execute_query(query)
        self.print_all_data(CUSTOMERS)
        '''

        #  Column('id', Integer, primary_key=True),
        #               Column('color', String),
        #               Column('model', Integer)

    def insert_loans(self, custid, bookid, loandate, returndate):
        # Insert Data
        query = f"INSERT INTO {LOANS}(custid, bookid, loandate, returndate) " \
                f"VALUES ('{custid}','{bookid}','{loandate}','{returndate}');"
        # print(query)
        self.execute_query(query)
        self.print_all_data(LOANS)
        
        
        
    def insert_customer(self, name, city, age):
        # Insert Data
        query = f"INSERT INTO {CUSTOMERS}(name, city, age) " \
                f"VALUES ('{name}','{city}','{age}');"
        # print(query)
        self.execute_query(query)
        self.print_all_data(CUSTOMERS)
        
        
    def insert_books(self, name, author, yearpublished, loantype):
        # Insert Data
        query = f"INSERT INTO {BOOKS}(name, author, yearpublished, loantype) " \
                f"VALUES ('{name}','{author}','{yearpublished}','{loantype}');"
        # print(query)
        self.execute_query(query)
        self.print_all_data(BOOKS)


    def sample_insert(self):
        # Insert Data
        query = "INSERT INTO {}(id, first_name, last_name) " \
                "VALUES (3, 'Terrence','Jordan');".format(CUSTOMERS)
        self.execute_query(query)
        self.print_all_data(CUSTOMERS)



    def sample_insert(self):
        # Insert Data
        query = "INSERT INTO {}(id, first_name, last_name) " \
                "VALUES (3, 'Terrence','Jordan');".format(CUSTOMERS)
        self.execute_query(query)
        self.print_all_data(CUSTOMERS)

    def sample_update(self):
        # Update Data
        query = "UPDATE {} set first_name='XXXX' WHERE id={id}"\
            .format(CUSTOMERS, id=3)
        self.execute_query(query)
        self.print_all_data(CUSTOMERS)