class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-My-Header'] = "Resource Header"
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Credentials"] = True
        response["Access-Control-Allow-Headers"] = "Origin,Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,locale"
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD"
        return response