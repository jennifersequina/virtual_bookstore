## Virtual Library for Bookworms 📚

### Description:
This is my personal project creating virtual library using python, flask and bigquery.
I created this web app where the user should create an account and log in to access home and library. In the home page, the user can create his/her own notes anything about books, reviews, etc. In the library page, this is where the user can search for a book and get the link to buy it in Amazon website.

This project contains the following:
- main.py
- bq_connection.py
- gbq.py
- yaml_reader.py
- website
    - static
    - templates (base.html - this will be extended to all html templates -> home.html, library.html, results.html, sign_up.html)
    - init.py
    - auth.py
    - models.py
    - view.py

I am no expert in html, javascript, css thus in creating templates I just followed some tutorials in youtube. 
I also followed the creation of database using SQLAlchemy, this database created only for the purpose of saving the information in sign up and using it in log in and authentication.
However, the main database I used for the books was Google Big Query (GBQ).

### Methodology:
In this section, I'll jump in creating the connection with GBQ and accessing this database using python and showing the results in the web page.

1. Connecting to the database (Google BigQuery) to access the list of books I wanted to show in the search results. Refer to bq_connection.py and yaml_reader.py.
- I created yaml_reader.py to create function for configuration. It's important to keep the project id and credentials confidential. The yaml_reader.py will access the config.yaml I created where the project id and credentials path saved.

2. Setting up class for GBQ and created functions to send SQL queries. Refer to gbq.py.
- Function search_books will return the list of books that the user input in the search bar.
- Function _clean_string is to clean up the search input by user, and for the database would not be manipulated by inputting query in the search bar.
- Function get_book_details will return the full details of the book selected from the search results.

3. Creating route or path for login, logout, sign-up, library and results functions. Refer to auth.py. Each function has decorated with '@auth.route', and the request methods used are GET and POST.
- For login, it will get the email and password input by user in the forms. This will authenticate the user (which has been created in the database-SQLAlchemy during sign-up). If the email exists and password has been authenticated, user will be logged in successfully. Otherwise, it will throw an error message "incorrect password" or "email does not exist". Refer as well to website/login.html to see the template.
- For logout, I've put additional decorator '@login required', so the logout button will only be visible and accessible when the user has logged in. Once logged out, user will be redirected to login page.
- For sign-up, the function will get all the input from user and there are validations for each item. These details will be saved in the database created in SQLAlchemy, and once the account created, it will throw a success message. Refer to website/sign_up.html to see the template.
- For library, I've created this function to access the SQL query created in gbq.py related to search_books. This will return the list of books searched by user in the library page. See also website/library.html for the template.
- For results, I've created this function and pass a parameter 'title' which will be coming from the function get_book_details in gbq.py. The details of the book will be displayed in the results page. See website/results.html for the template.

### NOTE:
I'll be closing this project to this state as I only started it to learn more about sending queries using python, HTTP requests method and have a bit of knowledge with HTML. Creating this project has been a fun and good experience for me.

### FOR IMPROVEMENT:
This project could be further improve by the following:
- creating database of users to Google Big Query (where the database for books located) instead of SQlAlchemy to make it more streamline.
- it could be an online bookstore where add to cart function can be added. In this case, admin user should be also created where it can manipulate the inventory of books and prices.


