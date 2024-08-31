# Build a Flask app that allows users to upload files and display them on the website

from flask import Flask, request, redirect, url_for, render_template_string
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file size to 16 MB

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>File Upload</title>
        </head>
        <body>
            <h1>Upload a File</h1>
            <form method="post" enctype="multipart/form-data">
                <input type="file" name="file">
                <input type="submit" value="Upload">
            </form>
        </body>
        </html>
    ''')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Uploaded File</title>
        </head>
        <body>
            <h1>File Uploaded Successfully</h1>
            <img src="{{ url_for('static', filename='uploads/' ~ filename) }}" alt="Uploaded File">
            <a href="/">Upload another file</a>
        </body>
        </html>
    ''', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
