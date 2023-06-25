from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "secret"

app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app=app)
socketio = SocketIO()
socketio.init_app(app, cors_allowed_origins='*')

@socketio.on("connect")
def handle_connect():
  print("client connected")

@socketio.on("button_stat")
def activity(switch):
    if switch == "True":
        emit("Activity", "True", broadcast=True)
    elif switch == "False":
        emit("Activity", "False", broadcast=True)

@app.route('/')
def index():
    return 'Hello from Flask!'

socketio.run(app,host="0.0.0.0",port=5400)
##app.run(host='0.0.0.0', port=81)
