from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE_MSG = "Difference between expected and actual status codes"
    NOT_STATUS_OK = "Key 'status' is not ok"
    NOT_STR_INSTANSE = "Object type is not a STR"
    NOT_INT_INSTANSE = "Object type is not a INT"
    NOT_LIST_INSTANSE = "Object type is not a LIST"
    RAISE_404_ERROR = "Route or entity not found"
    NO_CONTENT_LENGHTH = "Content-Length is missing in response headers"
    NO_ETAG = "Etag is missing in headers"
    NOT_MATCHED_TO_MIN_VALUE = "The attribute value doesn't match to min valid value"
    NOT_MATCHED_TO_EXPECTED_VALUE = "The attribute value doesn't match to expected value"
    VALUE_IS_NONE = "Item is None"


class GlobalErrorDict(Enum):
    error_404_found = {
    "status": "error",
    "message": "Not found"
}


# class GLobalHeadersVariables(Enum):
#     H_SERVER = "nginx/1.18.0 (Ubuntu)",
#     # Date
#     H_CONTENT_TYPE = "application/json; charset=utf-8",
#     # Content - Length
#     H_CONNECTION = "keep-alive",
#     H_X_POWERED_BY = "Express",
#     H_VARY = "Vary",
#     H_ACC_CONTROL_ALLOW_CRED = True,
#     # ETag


#HEADERS ATTRIBUTES:
H_SERVER = "nginx/1.18.0 (Ubuntu)"
H_CONTENT_TYPE = "application/json; charset=utf-8"
H_CONNECTION = "keep-alive"
H_X_POWERED_BY = "Express"
H_VARY = "Origin"
H_ACC_CONTROL_ALLOW_CRED = "true"

#MIN VALUE IN ATTRIBUTES
MIN_ATTR_VALUE_INSTRUCTION = 1