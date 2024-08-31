# Develop a Flask app that uses URL parameters to display dynamic content

from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')  # Default to 'Guest' if 'name' is not provided
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Greeting</title>
        </head>
        <body>
            <h1>Hello, {{ name }}!</h1>
        </body>
        </html>
    ''', name=name)

if __name__ == '__main__':
    app.run(debug=True)
