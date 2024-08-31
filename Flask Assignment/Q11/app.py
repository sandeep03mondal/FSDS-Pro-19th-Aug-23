# Create a real-time chat application using Flask-SocketIO

from flask import Flask, render_template_string
from flask_socketio import SocketIO, send, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Chat Room</title>
            <script src="https://cdn.socket.io/4.0.0/socket.io.min.js"></script>
        </head>
        <body>
            <h1>Chat Room</h1>
            <div id="messages"></div>
            <input id="message_input" autocomplete="off">
            <button onclick="sendMessage()">Send</button>
            <script>
                var socket = io();
                var messages = document.getElementById('messages');

                socket.on('message', function(msg) {
                    var item = document.createElement('div');
                    item.textContent = msg;
                    messages.appendChild(item);
                });

                function sendMessage() {
                    var input = document.getElementById('message_input');
                    socket.send(input.value);
                    input.value = '';
                }
            </script>
        </body>
        </html>
    ''')

@socketio.on('message')
def handle_message(message):
    send(message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
