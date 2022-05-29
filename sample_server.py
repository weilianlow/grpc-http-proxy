from concurrent import futures
import grpc
from proto.gen.src.sample import helloworld_pb2, helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        msg = ''
        if request.name:
            msg += f'Welcome, {request.name}!'
        if request.age:
            if msg:
                msg += ' '
            msg += f'Your age is {request.age}.'
        if request.contact:
            for i, contact in enumerate(request.contact):
                if msg:
                    msg += ' '
                if contact.email:
                    msg += f'Your {i + 1}th contact detail is by email: "{contact.email}".'
                elif contact.phone:
                    msg += f'Your {i + 1}th contact detail is by phone: "{contact.phone}".'

        return helloworld_pb2.HelloReply(message=msg)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
