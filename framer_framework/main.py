import quopri

from .pr_requests import GetRequest, PostRequest


class NotFound404:
    def __call__(self, request):
        return '404 What', 'Page not found'


class Framework:

    def __init__(self, routes_obj, fronts_obj):
        self.routes_lst = routes_obj
        self.fronts_lst = fronts_obj

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        request = {}
        for front in self.fronts_lst:
            front(request)

        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequest().request_params(environ)
            request['data'] = data

        if method == 'GET':
            request_params = GetRequest().request_params(environ)
            request['request_params'] = request_params

        if path in self.routes_lst:
            view = self.routes_lst[path]
        else:
            view = NotFound404()

        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        buffer = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            buffer[k] = val_decode_str
        return buffer


class DebugApplication(Framework):
    def __init__(self, routes_obj, fronts_obj):
        self.application = Framework(routes_obj, fronts_obj)
        super().__init__(routes_obj, fronts_obj)

    def __call__(self, env, start_response):
        print('DEBUG MODE')
        print(env)
        return self.application(env, start_response)


class FakeApplication(Framework):
    def __init__(self, routes_obj, fronts_obj):
        self.application = Framework(routes_obj, fronts_obj)
        super().__init__(routes_obj, fronts_obj)

    def __call__(self, env, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Hello from Fake']
