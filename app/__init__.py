from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = Flask(__name__)
socketio=SocketIO(app)

SECRET_KEY = 'Sup3r$3cretkey'
app.config.from_object(__name__)
from app import views
