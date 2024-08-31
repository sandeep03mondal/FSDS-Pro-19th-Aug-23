# Implement notifications in a Flask app using WebSockets to notify users of updates

from flask import Flask, render_template_string
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Notifications</title>
            <script src="https://cdn.socket.io/4.0.0/socket.io.min.js"></script>
        </head>
        <body>
            <h1>Notifications</h1>
            <div id="notifications"></div>
            <button onclick="sendNotification()">Send Notification</button>
            <script>
                var socket = io();
                var notifications = document.getElementById('notifications');

                socket.on('notification', function(message) {
                    var item = document.createElement('div');
                    item.textContent = message;
                    notifications.appendChild(item);
                });

                function sendNotification() {
                    socket.emit('send_notification', 'New update available!');
                }
            </script>
        </body>
        </html>
    ''')

@socketio.on('send_notification')
def handle_send_notification(message):
    emit('notification', message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
