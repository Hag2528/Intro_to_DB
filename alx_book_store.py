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

# def tableinsert(author_id,author_name,book_id):
#     query="INSERT INTO Authors(author_id,author_name,book_id)values(%s,%s,%s)"
#     values=(author_id,author_name,book_id)
#     mycursor.execute(query,values)
#     mydb.commit()
#     print("Record SuccessFully")
# tableinsert(1,"kebe",1)
def books(book_id,title,price,publication_date,author_id):
    query="INSERT INTO Books(book_id,title,price,publication_date,author_id)values(%s,%s,%s,%s,%s)"
    values=(book_id,title,price,publication_date,author_id)
    mycursor.execute(query,values)
    mydb.commit()
    print("Successfully inserted into Book table")
books(1,"Advanced SWE","100,2024-07-26",1)