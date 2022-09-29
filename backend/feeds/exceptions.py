from rest_framework.exceptions import APIException



class AccessDenied(APIException):
    status_code = 403
    default_detail = 'you dont have access to this content'
    default_code = 'access_denied'


class NotFound(APIException):
    status_code = 404
    default_detail = 'not found'
    default_code = 'not_found'


class BadRequest(APIException):
    status_code = 400
    default_detail = 'bad request'
    default_code = 'bad_request'

class InternalServerError(APIException):
    status_code = 500
    default_detail = 'internal server error'
    default_code = 'internal_server_error'

class MissingParameter(APIException):
    status_code = 400
    default_detail = 'missing parameter'
    default_code = 'missing_parameter'