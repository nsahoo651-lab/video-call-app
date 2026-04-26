import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'naresh_pro_ultra'
socketio = SocketIO(app, cors_allowed_origins="*", max_decode_packets=5000000, async_mode='gevent')

@app.route('/')
def index(): return render_template('index.html')

@socketio.on('join')
def on_join(data):
    room = 'naresh_room'
    join_room(room)
    emit('user-joined', data, to=room, include_self=False)

@socketio.on('signal')
def handle_signal(data):
    emit('signal', data, to='naresh_room', include_self=False)

@socketio.on('chat_message')
def handle_message(data):
    emit('chat_message', data, to='naresh_room', include_self=False)

@socketio.on('media_share')
def handle_media(data):
    emit('receive_media', data, to='naresh_room', include_self=False)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
