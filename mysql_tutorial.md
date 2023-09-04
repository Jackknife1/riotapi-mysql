# mysql.md

**Description**

In this file i'll show how to create your own database, table and how to modify database.

# Workflow process

 **Python**


  **1. In bash execute this command to install mysl.connector module for connecting to mysql database and alternating it**
     <pre>
       `
       pip install mysql-connector-python
       `
     </pre>

     
  **2. First we import module mysql.connector**
     <pre>
       `
       import mysql.connector
       `
     </pre>

      
  **3. Now we need to estabilish a connection with database by passing infromation about host, user and password**
        <pre>
          ```connection = mysql.connector.connect()```
          host = "host"
          user = "root"
          password = "your_password"
        </pre>

     
  **4. Now we need to create a cursor to interact with database**
     <pre>
       `
       mycursor = connection.cursor()
       `
     </pre>

     
  **5. Create database**
     <pre>
      `
      mycursor.execute("CREATE DATABASE database_name")
      `
     </pre>

     
  **6. Commit changes to save them**
     <pre>
     `
     connection.commit()
     `
     </pre>


  **7. Create table in your database, define table structure and collumns**
     <pre>
     ```table_query = """```
     CREATE TABLE IF NOT EXISTS your_table_name (
     collumn_name1 VARCHAR(45),
     collumn_name2 VARCHAR(45),
     collumn_name3 INT
     """
     cursor.execute(table_query)
     </pre>

  **NOTE**
  Dont forget to specify in *connection* your database name where table can be created
    <pre>
    ```connection = mysql.connector.connect()```
    host = "host"
    user = "root"
    password = "your_password"
    </pre>
  
  **8. Insert data into database**
  <p>
    
  [data_to_sql](data_to_sql.py) - process is shown in file

  </p>

  **NOTE**
  When inserting data into database, always check
  - Collumn order must match with collumn names in table
  - Number of placeholders must match number of rows
  - Format api data into hashable format, like tuple(), so it can be properly inserted
  - Check if data types of your varibales match data types of your collumns (can't insert str into int collumn)

  Thank you for reading





     


  

