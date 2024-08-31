# Integrate a SQLite database with Flask to perform CRUD operations on a list of items

from flask import Flask, request, jsonify, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    items = Item.query.all()
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Item List</title>
        </head>
        <body>
            <h1>Items</h1>
            <ul>
                {% for item in items %}
                <li>{{ item.name }}</li>
                {% endfor %}
            </ul>
            <form method="post" action="/add">
                <input type="text" name="name" placeholder="Item Name">
                <input type="submit" value="Add Item">
            </form>
        </body>
        </html>
    ''', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    item = Item(name=name)
    db.session.add(item)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
