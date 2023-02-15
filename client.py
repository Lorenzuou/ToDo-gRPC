import grpc
import protos.todo_pb2 as todo_pb2
import protos.todo_pb2_grpc as todo_pb2_grpc

# Connect to the server
channel = grpc.insecure_channel('localhost:50051')

# Create a stub for the Todo service
stub = todo_pb2_grpc.TodoStub(channel)

# Create a to-do item
todo = todo_pb2.TodoItem(description="Buy milk")

# Create the to-do item on the server
created_todo = stub.createTodo(todo)
print("Created to-do item:", created_todo)

# Get the created to-do item
todo_id = created_todo.id
get_todo = stub.getTodo(todo_pb2.TodoItem(id=todo_id))
print("Got to-do item:", get_todo)

# Update the to-do item
update_todo = stub.updateTodo(todo_pb2.TodoItem(id=todo_id, description="Buy milk and bread"))
print("updated to-do item:", update_todo)

# Get the updated to-do item
get_todo = stub.getTodo(todo_pb2.TodoItem(id=todo_id))
print("got to-do item:", get_todo)

# Delete the to-do item
stub.deleteTodo(todo_pb2.TodoItem(id=todo_id))
print("Deleted to-do item")

# List all to-do items
todos = list(stub.listTodo(todo_pb2.TodoItem()))
print("List of to-do items:", todos)