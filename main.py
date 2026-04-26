import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'naresh_secret_123'
# CORS allow-all taaki koi bhi jud sake
socketio = SocketIO(app, cors_allowed_origins="*", max_decode_packets=1000000)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('signal')
def handle_signal(data):
    # Multi-user signaling: Jo bhi data aaye use baaki sabko bhej do
    emit('signal', data, broadcast=True, include_self=False)

@socketio.on('chat_message')
def handle_message(data):
    # Chat message aur file sharing data ko sabko bhejna
    emit('chat_message', data, broadcast=True, include_self=False)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port, allow_unsafe_werkzeug=True)
