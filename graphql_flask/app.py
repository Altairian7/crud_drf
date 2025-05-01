from flask import Flask, request, jsonify
from ariadne import QueryType, graphql_sync, make_executable_schema
from ariadne.explorer import ExplorerGraphiQL

# Define schema and resolvers
type_defs = """
    type Query {
        hello: String!
    }
"""

query = QueryType()

@query.field("hello")
def resolve_hello(_, info):
    return "Hello from Ariadne + Flask!"

schema = make_executable_schema(type_defs, query)
explorer_html = ExplorerGraphiQL().html(None)

# Create Flask app
app = Flask(__name__)

@app.route("/graphql", methods=["GET"])
def graphql_explorer():
    return explorer_html, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
