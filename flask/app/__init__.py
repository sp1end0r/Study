#file name : __init__.py
#pwd : /home/sp1end0r/source/cert/project/app

from flask import Flask
import index
import db_conn
#if you add module, you can
#if you add config file, you can

app = Flask(__name__)
#app.register_blueprint(index.main)
app.register_blueprint(db_conn.main)
