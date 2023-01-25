class CustomError(Exception):
    def __init__(self, message=None, extra=None, object=None):
        self.message = message
        self.object = object
        self.extra = extra

class Validation(CustomError):
    status = 400

class NotFound(CustomError):
    status = 404
