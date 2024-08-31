# Build a Flask app that updates data in real-time using WebSocket connections

from flask import Flask, render_template_string
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Real-Time Data</title>
            <script src="https://cdn.socket.io/4.0.0/socket.io.min.js"></script>
        </head>
        <body>
            <h1>Real-Time Data</h1>
            <div id="data"></div>
            <script>
                var socket = io();
                var dataElement = document.getElementById('data');

                socket.on('update_data', function(data) {
                    dataElement.textContent = 'Data: ' + data;
                });

                function requestUpdate() {
                    socket.emit('request_update');
                }

                setInterval(requestUpdate, 2000); // Request update every 2 seconds
            </script>
        </body>
        </html>
    ''')

@socketio.on('request_update')
def handle_request_update():
    data = random.randint(1, 100)
    emit('update_data', data)

if __name__ == '__main__':
    socketio.run(app, debug=True)
