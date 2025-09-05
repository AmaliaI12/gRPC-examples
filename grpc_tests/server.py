import pickle
import grpc

from concurrent import futures
from grpc_tests.protos import service_pb2, service_pb2_grpc
from .complex_num import Complex

class DictionaryService (service_pb2_grpc.DictionaryServiceServicer):
    def GetDictionary(self, request, context):
        data_dict = {"name": "Aurica", "age": 21, "city": "Vladesti"}
        pickled_data = pickle.dumps(data_dict)
        print("Returning the pickled dictionary")
        return service_pb2.PickledData(data=pickled_data)

class ObjectService (service_pb2_grpc.ObjectServiceServicer):
    def GetObject(self, request, context):
        obj = Complex(3.0, -4.5)
        print("Complex number: ", obj.r, " ", obj.i)
        pickled_data = pickle.dumps(obj)
        print("Returning the pickled object")
        return service_pb2.PickledData(data=pickled_data)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    #service_pb2_grpc.add_DictionaryServiceServicer_to_server(DictionaryService(), server)
    service_pb2_grpc.add_ObjectServiceServicer_to_server(ObjectService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server started on port 50051")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

