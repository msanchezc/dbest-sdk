# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from dbest_sdk.autogen import bidirectional_pb2 as bidirectional__pb2


class BidirectionalStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribeStateListener = channel.unary_stream(
            '/Bidirectional/SubscribeStateListener',
            request_serializer=bidirectional__pb2.Subscribe.SerializeToString,
            response_deserializer=bidirectional__pb2.NewState.FromString,
        )
        self.UnsubscribeStateListener = channel.unary_unary(
            '/Bidirectional/UnsubscribeStateListener',
            request_serializer=bidirectional__pb2.Subscribe.SerializeToString,
            response_deserializer=bidirectional__pb2.Ok.FromString,
        )
        self.UpdateState = channel.unary_unary(
            '/Bidirectional/UpdateState',
            request_serializer=bidirectional__pb2.NewState.SerializeToString,
            response_deserializer=bidirectional__pb2.Ok.FromString,
        )
        self.SimpleRequest = channel.unary_unary(
            '/Bidirectional/SimpleRequest',
            request_serializer=bidirectional__pb2.Message.SerializeToString,
            response_deserializer=bidirectional__pb2.Message.FromString,
        )
        self.UpdateAnswer = channel.unary_unary(
            '/Bidirectional/UpdateAnswer',
            request_serializer=bidirectional__pb2.Message.SerializeToString,
            response_deserializer=bidirectional__pb2.Ok.FromString,
        )


class BidirectionalServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SubscribeStateListener(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnsubscribeStateListener(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SimpleRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAnswer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BidirectionalServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'SubscribeStateListener': grpc.unary_stream_rpc_method_handler(
            servicer.SubscribeStateListener,
            request_deserializer=bidirectional__pb2.Subscribe.FromString,
            response_serializer=bidirectional__pb2.NewState.SerializeToString,
        ),
        'UnsubscribeStateListener': grpc.unary_unary_rpc_method_handler(
            servicer.UnsubscribeStateListener,
            request_deserializer=bidirectional__pb2.Subscribe.FromString,
            response_serializer=bidirectional__pb2.Ok.SerializeToString,
        ),
        'UpdateState': grpc.unary_unary_rpc_method_handler(
            servicer.UpdateState,
            request_deserializer=bidirectional__pb2.NewState.FromString,
            response_serializer=bidirectional__pb2.Ok.SerializeToString,
        ),
        'SimpleRequest': grpc.unary_unary_rpc_method_handler(
            servicer.SimpleRequest,
            request_deserializer=bidirectional__pb2.Message.FromString,
            response_serializer=bidirectional__pb2.Message.SerializeToString,
        ),
        'UpdateAnswer': grpc.unary_unary_rpc_method_handler(
            servicer.UpdateAnswer,
            request_deserializer=bidirectional__pb2.Message.FromString,
            response_serializer=bidirectional__pb2.Ok.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Bidirectional', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class Bidirectional(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SubscribeStateListener(request,
                               target,
                               options=(),
                               channel_credentials=None,
                               call_credentials=None,
                               compression=None,
                               wait_for_ready=None,
                               timeout=None,
                               metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Bidirectional/SubscribeStateListener',
                                              bidirectional__pb2.Subscribe.SerializeToString,
                                              bidirectional__pb2.NewState.FromString,
                                              options, channel_credentials,
                                              call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnsubscribeStateListener(request,
                                 target,
                                 options=(),
                                 channel_credentials=None,
                                 call_credentials=None,
                                 compression=None,
                                 wait_for_ready=None,
                                 timeout=None,
                                 metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bidirectional/UnsubscribeStateListener',
                                             bidirectional__pb2.Subscribe.SerializeToString,
                                             bidirectional__pb2.Ok.FromString,
                                             options, channel_credentials,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateState(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bidirectional/UpdateState',
                                             bidirectional__pb2.NewState.SerializeToString,
                                             bidirectional__pb2.Ok.FromString,
                                             options, channel_credentials,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SimpleRequest(request,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bidirectional/SimpleRequest',
                                             bidirectional__pb2.Message.SerializeToString,
                                             bidirectional__pb2.Message.FromString,
                                             options, channel_credentials,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAnswer(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bidirectional/UpdateAnswer',
                                             bidirectional__pb2.Message.SerializeToString,
                                             bidirectional__pb2.Ok.FromString,
                                             options, channel_credentials,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)
