# Implement user sessions in a Flask app to store and display user-specific data

from flask import Flask, request, session, render_template_string, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form.get('user_name', 'Guest')
        session['user_name'] = user_name
        return redirect(url_for('welcome'))

    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>User Input</title>
        </head>
        <body>
            <h1>Enter Your Name</h1>
            <form method="post">
                <label for="user_name">Name:</label>
                <input type="text" id="user_name" name="user_name">
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    ''')

@app.route('/welcome')
def welcome():
    user_name = session.get('user_name', 'Guest')
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Welcome</title>
        </head>
        <body>
            <h1>Welcome, {{ user_name }}!</h1>
            <a href="/">Go back</a>
        </body>
        </html>
    ''', user_name=user_name)

if __name__ == '__main__':
    app.run(debug=True)
