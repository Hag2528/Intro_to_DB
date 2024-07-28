USE alx_book_store;
SELECT 
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(130) NOT NULL,
    author_id INT,
    price DOUBLE,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
FROM      
  INFORMATION_SCHEMA.book_id,COLUMN_NAME="BOOK_ID",COLUMN_TYPE="INT",
   INFORMATION_SCHEMA.title,COLUMN_NAME="TITLE",COLUMN_TYPE="VARCHAR",
   INFORMATION_SCHEMA.author_id,COLUMN_NAME="AUTHOR_ID",COLUMN_TYPE="INT",
   INFORMATION_SCHEMA.price,COLUMN_NAME="PRICE",COLUMN_TYPE="DOUBLE",
   INFORMATION_SCHEMA.publication_date,COLUMN_NAME="PUBLICATION_DATE",COLUMN_TYPE="DATE",
WHERE
   TABLE_SHEMA='ALX_BOOK_STORE()'AND TABLE_NAME='Books';
