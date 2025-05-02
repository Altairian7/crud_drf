from flask import Flask, request, jsonify
from ariadne import graphql_sync, make_executable_schema, ObjectType, QueryType, MutationType, load_schema_from_path
from ariadne.constants import PLAYGROUND_HTML
from models import db, Task

# Flask App
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)