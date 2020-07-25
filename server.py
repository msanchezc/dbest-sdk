from concurrent import futures

import grpc, time, uuid, asyncio, logging, janus
from grpc.experimental import aio                                               
import bidirectional_pb2_grpc as bidirectional_pb2_grpc
import bidirectional_pb2 as bidirectional_pb2
from SerialBroker import SerialBroker

class State:
    def __init__(self, state):
        self.state = state

class Unsubscribe:
    def __init__(self, uid):
        self.uid = uid

class BidirectionalService(bidirectional_pb2_grpc.BidirectionalServicer):

    def __init__(self):
        self.queues = {}

    async def SubscribeStateListener(self, request, context):
        uid = request.id
        queue = janus.Queue()
        self.queues[uid] = queue
        while True:
            message = await self.queues[uid].async_q.get()
            if isinstance(message, State):
                yield bidirectional_pb2.NewState(state = message.state)

            if isinstance(message, Unsubscribe):
                self.queues[uid].close()
                self.queues[uid] = None 
                break

    def UnsubscribeStateListener(self, request, context):
        uid = request.id
        self.queues[uid].sync_q.put(Unsubscribe(uid))
        return bidirectional_pb2.Ok()

    def UpdateState(self, request, context):
        new_state = request
        dbest_state = State(new_state.state)
        for key in self.queues:
            if self.queues[key] and not self.queues[key].closed:
                self.queues[key].sync_q.put(dbest_state)
        response = bidirectional_pb2.Ok()
        return response


async def _start_async_server():                                                
    server = aio.server()                                                         
    server.add_insecure_port('[::]:50051')                                        
    bidirectional_pb2_grpc.add_BidirectionalServicer_to_server(BidirectionalService(), server)
    await server.start()                                                          
    await server.wait_for_termination()                                           
                                                                                
                                                                                
def main():
    sb = SerialBroker()
    sb.start()
    loop = asyncio.get_event_loop()                                               
    loop.create_task(_start_async_server())                                       
    loop.run_forever()                                                            


if __name__ == '__main__':                                                      
    logging.basicConfig()                                                         
    main()  
