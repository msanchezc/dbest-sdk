import enum

class DbestResponse(enum.Enum):
    ACK = 200
    NOT_ALLOWED_IN_CURRENT_STATE = 400
    INCONGRUITY_SENSOR_ON_AUXILIARY_AREA = 501
    INCONGRUITY_SENSOR_OFF_AUXILIARY_AREA = 502
    INCONGRUITY_SENSOR_ON_EXCHANGE_AREA = 503
    INCONGRUITY_SENSOR_OFF_EXCHANGE_AREA = 504
