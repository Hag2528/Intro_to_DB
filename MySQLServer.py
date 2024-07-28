import mysql.connector
def create_database(db_name="alx_book_store", host="localhost", user="your_username", password="your_password"):
  try:
    connection = mysql.connector.connect(host=host, user=user, password=password)
    cursor = connection.cursor()
  
    sql = f"CREATE DATABASE IF NOT EXISTS {db_name}"
    cursor.execute(sql)

    connection.commit()

    print(f"Database '{db_name}' created successfully!")

  except mysql.connector.Error as err:
    print(f"Error creating database: {err}")

  finally:
    if connection:
      connection.close() 

if __name__ == "__main__":
  create_database()
