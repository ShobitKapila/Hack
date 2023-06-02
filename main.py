from flask import Flask, render_template, redirect, url_for
import mysql.connector
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

 
# app.secret_key = 'your secret key'
 
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'your password'
# app.config['MYSQL_DB'] = 'geeklogin'

# mysql = MySQL(app)

# MySQL database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database_name',
}


app = Flask(__name__)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        email = request.form['email']
        contact = request.form['contact']
        weight = request.form['weight']
        height = request.form['height']
        blood_group = request.form['blood_group']
        #illness = request.form['illness']
        emergency_contact = request.form['emergency_contact']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Example: Checking if password and confirm_password match
        if password != confirm_password:
            error_message = "Passwords do not match."
            return render_template('next.html', error_message=error_message)

        # Redirect to a success page
        return render_template('success.html', name=name)

    # Render the login page
    return render_template('next.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Connect to the MySQL database
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        # Retrieve the stored password for the given email
        query = "SELECT password FROM personal_info WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()

        # Check if the email exists and the password matches
        if result and password == result[0]:
            cursor.close()
            cnx.close()

            # Redirect to the success page
            return redirect(url_for('success', email=email))
        else:
            cursor.close()
            cnx.close()

            error_message = "Invalid email or password."
            return render_template('login.html', error_message=error_message)

    # Render the login page
    return render_template('login.html')

@app.route('/success')
def success():
    email = request.args.get('email')
    return render_template('success.html', email=email)


if __name__ == '__main__':
    app.run()
