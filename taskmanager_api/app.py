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

# Mutation: Create
@mutation.field("createTask")
def resolve_create_task(_, info, title, dueDate=None):
    task = Task(title=title, due_date=dueDate)
    db.session.add(task)
    db.session.commit()
    return task

# Mutation: Toggle Complete
@mutation.field("toggleDone")
def resolve_toggle_done(_, info, id):
    task = Task.query.get(id)
    task.is_done = not task.is_done
    db.session.commit()
    return task

# Mutation: Delete
@mutation.field("deleteTask")
def resolve_delete(_, info, id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return True
