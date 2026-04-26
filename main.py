import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
# Secret key security ke liye zaroori hai
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('signal')
def handle_signal(data):
    # Ek phone se dusre phone tak signal bhejta hai
    emit('signal', data, broadcast=True, include_self=False)

if __name__ == '__main__':
    # Render khud port decide karta hai, isliye hum os.environ use kar rahe hain
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port, allow_unsafe_werkzeug=True)
