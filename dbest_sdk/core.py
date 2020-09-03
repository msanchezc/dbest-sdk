import grpc
import uuid
import threading
import time
from threading import Lock
from dbest_sdk.autogen import bidirectional_pb2_grpc as bidirectional_pb2_grpc
from dbest_sdk.autogen import bidirectional_pb2 as bidirectional_pb2
from dbest_sdk.states import DbesState
from dbest_sdk.messages import _DbestRequest as DbestRequest, DbestResponse


class Dbest:
    def __init__(self, ip="localhost:50051"):
        """
        Args:
            - ip (str): Ip address of GRPC server running on DBEST
        """
        self.ip = ip
        self.channel = None

    @staticmethod
    def _build_simple_request_message(data_str):
        id = "123456789"  # str(uuid.uuid1()) # stress_test
        return bidirectional_pb2.Message(id=id, data=data_str)

    def _simple_request(self, data_str):
        stub = bidirectional_pb2_grpc.BidirectionalStub(self.channel)
        message_response = stub.SimpleRequest(
            Dbest._build_simple_request_message(data_str), timeout=10
        )
        time.sleep(1)  # TODO remove sleep, bug #1
        return message_response.data

    def _response_from_request(self, dbest_request):
        response_str = self._simple_request(dbest_request)
        response = DbestResponse(int(response_str))
        return response

    def connect(self):
        """
        Allow you connect your instance to server running on DBEST
        """
        self.channel = grpc.insecure_channel(self.ip)

    def is_socket_enabled(self, n):
        """
        Get current enabled state of battery socket with index n
        Args:
            - n (int): Socket index [0, 7]
        Returns:
            [boolean]: True / False if socket is enabled / disabled on index n
        """
        return self._response_from_request(DbestRequest.is_socket_enabled_request(n))

    def is_socket_cooling(self, n):
        """
        Get current cooling state of battery socket with index n
        Args:
            - n (int): Socket index [0, 7]
        Returns:
            [boolean]: True / False if socket is cooling / disabled on index n
        """
        return self._response_from_request(DbestRequest.is_socket_cooling_request(n))

    def set_socket_enabled(self, flag, n):
        """
        Enable / Disable battery socket with index n
        Args:
            - n (int): Socket index [0, 7]
        Returns:
            [DbestResponse]: Request response.
        """
        return self._response_from_request(
            DbestRequest.set_socket_enabled_request(flag, n)
        )

    def exchange_battery(self, n):
        """
        If there are any drones in the exchange area, Dbest starts exchanging the drone battery with the battery in the socket with index n.
        Args:
            - n (int): Socket index [0, 7]
        Returns:
            [DbestResponse]: Request response.
        """
        return self._response_from_request(DbestRequest.exchange_battery_request(n))

    def lock(self):
        """
        Lock Dbest, in this state no request is received.
        Returns:
            [DbestResponse]: Request response.
        """
        return self._response_from_request(DbestRequest.LOCK)

    def unlock(self):
        """
        Unlock Dbest. DANGER: before calling this method it is necessary to remove all the drones from the exchanger manually. This method will reset Dbest to its initial state.

        Returns:
            [DbestResponse]: Request response.
        """
        return self._response_from_request(DbestRequest.UNLOCK)

    def take_drone_out(self):
        """
        Take out a drone from exchange area or auxiliary area, deploy top plattform and moves the drone to takeoff area.
        Returns:
            [DbestResponse]: Request response.
        """
        return self._response_from_request(DbestRequest.TAKE_DRONE_OUT)

    def take_drone_in(self):
        """
        Retract top plattform and move the drone from takeoff area to exchange area.
        Returns:
            [DbestResponse]: Request response.
        """
        return self._response_from_request(DbestRequest.TAKE_DRONE_OUT)

    def prepare_to_descent(self):
        """
        Deploy bottom plattform (Biggest ARUCO)
        Returns:
            [DbestResponse]: Request response.
        """
        return self._response_from_request(DbestRequest.PREPARE_TO_DESCENT)

    def prepare_to_land(self):
        """
        Deploy top plattform (Smallest ARUCO)
        Returns:
            [DbestResponse]: Request response.
        """
        return self._response_from_request(DbestRequest.PREPARE_TO_LAND)

    def retract_bottom_platform(self):
        """
        Starts to retract buttom plaftform

        Returns:
            [DbestResponse]: Request response.
        """
        return self._response_from_request(DbestRequest.RETRACT_BOTTOM_PLATTFORM)

    def retract_top_platform(self):
        """
        Starts to retract top plaftform

        Returns:
            [DbestResponse]: Request response.
        """
        return self._response_from_request(DbestRequest.RETRACT_TOP_PLATTFORM)

    def get_current_state(self):
        """
        Gets the current state of Dbest
        Returns:
            [DbesState]: Current Dbest state.
        """
        return self._response_from_request(DbestRequest.GET_CURRENT_STATE)

    def get_drone_count(self):
        """
        Gets total drone count inside Dbest, returned value can be 0, 1 or 2.
        Returns:
            [int]: drone count
        """
        return self._response_from_request(DbestRequest.GET_DRONE_COUNT)

    def _move_drone_from_exchange_area_to_auxiliary_area(self):
        """
        Starts to move drone from exchange area to auxiliary area
        Returns:
            [DbesState]: Current Dbest state.
        """
        return self._response_from_request(
            DbestRequest.MOVE_DRONE_FROM_EXCHANGE_AREA_TO_AUXILIARY_AREA
        )

    def _move_drone_from_auxiliary_area_to_exchange_area(self):
        """
        Starts to move drone from auxiliary area to exchange area
        Returns:
            [DbesState]: Current Dbest state.
        """
        return self._response_from_request(
            DbestRequest.MOVE_DRONE_FROM_AUXILIARY_AREA_TO_EXCHANGE_AREA
        )

    def wait_for_state(self, status_to_wait):
        """
        Block excecution untul 'status_to_wait' is reached on DBEST
        Args:
            - status_to_wait (DbesState): An possible state of DBEST
        """
        await_state_listener = _AwaitStateListener(self, status_to_wait)
        await_state_listener.wait()

    def disconnect(self):
        """
        Allow you disconnect your instance from server running on DBEST
        """
        self.channel.close()


class StatusChangedListener:
    def __init__(self, dbest_instance):
        """
        Args:
            - dbest_instance (Dbest): An connected Dbest instance
        """
        self.dbest_instance = dbest_instance
        self.uid = str(uuid.uuid1())

    def _subscribe(self, responses):
        try:
            for new_state_response in responses:
                state = DbesState(int(new_state_response.state))
                t = threading.Thread(target=self.onStateChanged, args=[state])
                t.daemon = True
                t.start()
        except Exception as e:
            print("INFO: Channel closed, Listener closed.")
            print(e)

    def subscribe(self):
        """
        When subscribe function is called,
        onStateChange will be called when a DBEST status change is notified.
        Returns:
            [DbestResponse]: Response for subscribe request
        """
        stub = bidirectional_pb2_grpc.BidirectionalStub(self.dbest_instance.channel)
        responses = stub.SubscribeStateListener(
            bidirectional_pb2.Subscribe(id=self.uid)
        )
        if responses:
            t = threading.Thread(target=self._subscribe, args=[responses])
            t.daemon = True
            t.start()
            return DbestResponse.ACK
        else:
            return DbestResponse.INTERNAL_ERROR

    def unsubscribe(self):
        """
        When subscribe function is called,
        onStateChange will be called when a DBEST status change is notified.
        """
        stub = bidirectional_pb2_grpc.BidirectionalStub(self.dbest_instance.channel)
        response = stub.UnsubscribeStateListener(
            bidirectional_pb2.Unsubscribe(id=self.uid)
        )
        return response

    def onStateChanged(self, state):
        """
        This function must be overwritten
        in order to catch the changes of state
        Args:
            - state (DbestState): new Dbest state
        """
        pass


class _AwaitStateListener(StatusChangedListener):
    def __init__(self, dbest_instance, status_to_wait):
        self.status_to_wait = status_to_wait
        super().__init__(dbest_instance)
        self.lock = Lock()
        self.lock.acquire()
        self.subscribe()

    def onStateChanged(self, state):
        print("LOG: esperando %s, actual %s" % (self.status_to_wait, state))
        if state.strip() == self.status_to_wait.strip():
            self.lock.release()

    def wait(self):
        self.lock.acquire()
        self.lock.release()
        self.unsubscribe()
