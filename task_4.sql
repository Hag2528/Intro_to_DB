USE alx_book_store;
SELECT 
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(130) NOT NULL,
    author_id INT,
    price DOUBLE,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
FROM      
  INFORMATION_SCHEMA.book_id,
   INFORMATION_SCHEMA.title,
   INFORMATION_SCHEMA.author_id,
   INFORMATION_SCHEMA.price,
   INFORMATION_SCHEMA.publication_date
WHERE
   TABLE_SHEMA=DATABASE() AND TABLE_NAME='books';
