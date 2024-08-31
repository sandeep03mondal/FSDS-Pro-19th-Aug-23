# Create a Flask app with a form that accepts user input and displays it

from flask import Flask, request, render_template_string

app = Flask(__name__)

# Route to display the form and handle form submission
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input', 'No input provided')
        return render_template_string('''
            <!DOCTYPE html>
            <html>
            <head>
                <title>User Input</title>
            </head>
            <body>
                <h1>Your Input:</h1>
                <p>{{ user_input }}</p>
                <a href="/">Go back</a>
            </body>
            </html>
        ''', user_input=user_input)
    
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Input Form</title>
        </head>
        <body>
            <h1>Input Form</h1>
            <form method="post">
                <label for="user_input">Enter something:</label>
                <input type="text" id="user_input" name="user_input">
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
