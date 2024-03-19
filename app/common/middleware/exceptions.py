from logging import getLogger

logger = getLogger("app")


class ExceptionLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        msg = f"{request.method} {request.path} {exception.__class__.__name__}: {exception}"
        logger.exception(msg=msg, exc_info=True)
