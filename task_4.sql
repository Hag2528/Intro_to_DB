USE alx_book_store;
SELECT 
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(130) NOT NULL,
    author_id INT,
    price DOUBLE,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
FROM      
  INFORMATION_SCHEMA.COLUMNS(
     COLUMN_NAME=BOOK_ID,COLUMN_TYPE=INT,
     COLUMN_NAME=TITLE,COLUMN_TYPE=VARCHAR,
     COLUMN_NAME=AUTHOR_ID,COLUMN_TYPE=INT,
     COLUMN_NAME=PRICE,COLUMN_TYPE=DOUBLE,
     COLUMN_NAME=PUBLICATION_DATE,COLUMN_TYPE=DATE
)
WHERE
   TABLE_SHEMA=ALX_BOOK_STORE() AND TABLE_NAME='Books';
