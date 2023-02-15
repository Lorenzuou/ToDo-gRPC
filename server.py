import grpc
from concurrent import futures
import time

import protos.todo_pb2 as todo_pb2
import protos.todo_pb2_grpc as todo_pb2_grpc




# Create a class to define the server functions, derived from
# todo_pb2_grpc.TodoServicer.
# methods:    rpc createTodo (TodoItem) returns (TodoItem); 
    # rpc getTodo (TodoItem) returns (TodoItem);
    # rpc updateTodo (TodoItem) returns (TodoItem);
    # rpc deleteTodo (TodoItem) returns (TodoItem);
    # rpc listTodo (TodoItem) returns (stream TodoItem); 

def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Register the service
    server.add_insecure_port('[::]:50051')
    print("Server started on port 50051")

    # Add the defined class to the server
    todo_pb2_grpc.add_TodoServicer_to_server(TodoServicer(), server)



    server.start()
    print("Server started")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()