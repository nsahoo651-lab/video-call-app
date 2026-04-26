import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'naresh_pro_audio_video'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='gevent')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    room = 'naresh_room'
    join_room(room)
    emit('user-joined', data, to=room, include_self=False)

@socketio.on('signal')
def handle_signal(data):
    # Ye line video aur audio ka data ek phone se dusre phone ko bhejti hai
    emit('signal', data, to='naresh_room', include_self=False)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port)
