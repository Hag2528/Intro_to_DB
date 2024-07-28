import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Do!mybest2121",
    database="alx_book_store"
)
mycursor=mydb.cursor()
# mycursor.execute("SELECT * FROM Authors")
# for i in mycursor:
#     print(i)

def authors(author_id,author_name,book_id):
    query="INSERT INTO Authors(author_id,author_name,book_id)values(%s,%s,%s)"
    values=(author_id,author_name,book_id)
    mycursor.execute(query,values)
    mydb.commit()
    print("Record SuccessFully")
authors(16,"shumuye",1)
def books(book_id,title,price,publication_date,author_id):
    query="INSERT INTO Books(book_id,title,price,publication_date,author_id)values(%s,%s,%s,%s,%s)"
    values=(book_id,title,price,publication_date,author_id)
    mycursor.execute(query,values)
    mydb.commit()
    print("Successfully inserted into Book table")
books(16,"Advanced SWE","100","2024-07-26",1)
def Customers(customer_id,customer_name,email,address,order_id):
    query="INSERT INTO Books(customer_id,customer_name,email,address,order_id)values(%s,%s,%s,%s,%s)"
    values=(customer_id,customer_name,email,address,order_id)
    mycursor.execute(query,values)
    mydb.commit()
    print("Successfully inserted into Customers table")
Customers(3,"Hagos","hag12@gmail.com","addisAbaba",1)
def orders(order_id,customer_id,order_date):
    query="INSERT INTO Books(order_id,customer_id,order_date)values(%s,%s,%s)"
    values=(order_id,customer_id,order_date)
    mycursor.execute(query,values)
    mydb.commit()
    print("Successfully inserted into Orders table")
orders(2,1,"2024-07-26")
def Order_Details(order_detail_id,order_id,book_id,quantity):
    query1="INSERT INTO Books(order_detail_id,order_id,book_id,quantity)values(%s,%s,%s,%s)"
    values=(order_detail_id,order_id,book_id,quantity)
    mycursor.execute(query1,values)
    mydb.commit()
    print("Successfully inserted into Orders table")
Order_Details(1,1,1,"200")
    
    
    
    