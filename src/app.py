from flask import Flask, jsonify, request
import json
app = Flask(__name__)

#Lista de todos 
todos = [
   { "label": "My first task", "done": False },
   { "label": "My second task", "done": False }
]

#Get
@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

#Post
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request.data)
    todos.append(decoded_object)
    print("todos")
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

#Delete
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(1) #Número de posición para eliminar 
    print("This is the position to delete: ",position)
    return jsonify(todos)

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)