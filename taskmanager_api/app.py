from flask import Flask, request, jsonify
from ariadne import QueryType, MutationType, make_executable_schema, graphql_sync, load_schema_from_path
from ariadne.explorer import ExplorerGraphiQL

from models import Task, create_task

query = QueryType()
mutation = MutationType()

@query.field("tasks")
def resolve_tasks(_, info):
    return tasks

@mutation.field("createTask")
def resolve_create_task(_, info, title, dueDate=None):
    return create_task(title, dueDate)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(type_defs, query, mutation)

app = Flask(__name__)
explorer_html = ExplorerGraphiQL().html(None)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return explorer_html, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request, debug=True)
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True)
