import pickle
import grpc

from grpc_tests.protos import service_pb2, service_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    #stub = service_pb2_grpc.DictionaryServiceStub(channel)
    #response = stub.GetDictionary(service_pb2.Empty())
    
    stub = service_pb2_grpc.ObjectServiceStub(channel)
    response = stub.GetObject(service_pb2.Empty())


    data = pickle.loads(response.data)
    

    print("Recieved: ", data.r, " ", data.i)

if __name__ == '__main__':
    run()
