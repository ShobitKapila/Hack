from flask import Flask, render_template, request

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

        # Perform any validation or processing on the data here

        # Example: Checking if password and confirm_password match
        if password != confirm_password:
            error_message = "Passwords do not match."
            return render_template('login.html', error_message=error_message)

        # Example: Saving the data to a database or performing any other actions

        # Redirect to a success page
        return render_template('success.html', name=name)

    # Render the login page
    return render_template('next.html')

if __name__ == '__main__':
    app.run()
