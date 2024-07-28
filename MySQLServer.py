import mysql.connector
def create_database(db_name="alx_book_store", host="localhost", user="root", password="Do!mybest2121"):
  try:
    connection = mysql.connector.connect(host=host, user=user, password=password)
    cursor = connection.cursor()
  
    sql = CREATE DATABASE IF NOT EXISTS alx_book_store;
    cursor.execute(sql)

    connection.commit()

    print(f"Database '{alx_book_store}' created successfully!")

  except mysql.connector.Error as err:
    print(f"Error creating database: {err}")

  finally:
    if connection:
      connection.close() 

if __name__ == "__main__":
  create_database()
