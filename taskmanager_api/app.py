from flask import Flask, request, jsonify
from ariadne import graphql_sync, make_executable_schema, ObjectType, QueryType, MutationType, load_schema_from_path
from ariadne.constants import PLAYGROUND_HTML
from models import db, Task

# Flask App
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Schema
type_defs = load_schema_from_path("schema.graphql")

query = QueryType()
mutation = MutationType()
task_obj = ObjectType("Task")

# Query: Get all tasks
@query.field("tasks")
def resolve_tasks(_, info):
    return Task.query.all()

# Query: Get single task
@query.field("task")
def resolve_task(_, info, id):
    return Task.query.get(id)
