import enum

# Get data from Dbest
# GTXXYYYYYYYY...
# Examples:
# GTSE6 ->  Get Socket enabled for socket 6
# GTSC0 ->  Get Socket cooling for socket 0
# GTCS -> Get current dbest state
# GTDC -> Get drone count inside Dbest

# Set some data to Dbest
# STXXYYYYYYYY...
# Examples:
# STSET7 -> Set enabled to True to socket with index 7 
# STSEF2 -> Set enabled to False to socket with index 2

class _DbestRequest:
    LOCK = "DRLO"
    UNLOCK = "DRUL"
    TAKE_DRONE_OUT = "DRTO"
    TAKE_DRONE_IN = "DRTI"
    PREPARE_TO_DESCENT = "DRPD"
    PREPARE_TO_LAND = "DRPL"
    RETRACT_BOTTOM_PLATTFORM = "DRRB"
    RETRACT_TOP_PLATTFORM = "DRRT"
    GET_CURRENT_STATE = "GTCS"
    GET_DRONE_COUNT = "GTDC"
    MOVE_DRONE_FROM_EXCHANGE_AREA_TO_AUXILIARY_AREA = "DRMA"
    MOVE_DRONE_FROM_AUXILIARY_AREA_TO_EXCHANGE_AREA = "DRME"

    @staticmethod
    def exchange_battery_request(n):
        assert isinstance(n, int)
        assert n >=0 and n <= 7
        return "DREB%s" % n

    @staticmethod
    def set_socket_enabled_request(flag, n):
        assert isinstance(flag, bool)
        assert isinstance(n, int)
        assert n >=0 and n <= 7
        if flag:
            c = "T"
        else:
            c = "F"
        return "STSE%s%s" % (c, n)
    
    @staticmethod
    def is_socket_cooling_request(n):
        assert isinstance(n, int)
        assert n >=0 and n <= 7
        return "GTSC%s" % n

    @staticmethod
    def is_socket_enabled_request(n):
        assert isinstance(n, int)
        assert n >=0 and n <= 7
        return "GTSE%s" % n

class DbestResponse(enum.Enum):
    ACK = 200
    DONE = 201
    INTERNAL_ERROR = 500
    NOT_ALLOWED_IN_CURRENT_STATE = 400
    INCONGRUITY_SENSOR_ON_AUXILIARY_AREA = 501
    INCONGRUITY_SENSOR_OFF_AUXILIARY_AREA = 502
    INCONGRUITY_SENSOR_ON_EXCHANGE_AREA = 503
    INCONGRUITY_SENSOR_OFF_EXCHANGE_AREA = 504
