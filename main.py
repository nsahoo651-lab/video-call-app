from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from pyngrok import ngrok

app = Flask(__name__)
# SocketIO ko initialize karein
socketio = SocketIO(app, cors_allowed_origins="*")

# APNA NGROK TOKEN YAHAN DAALEIN
ngrok.set_auth_token("2hK...aapka_token_yahan...")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('signal')
def handle_signal(data):
    emit('signal', data, broadcast=True, include_self=False)

if __name__ == '__main__':
    try:
        # Internet link banana
        public_url = ngrok.connect(5000).public_url
        print("\n" + "="*35)
        print("MUBARAK HO! APKA LIVE LINK YE HAI:")
        print(public_url)
        print("="*35 + "\n")
    except Exception as e:
        print("Ngrok Error:", e)

    # Server ko run karein (allow_unsafe_werkzeug zaroori hai)
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
