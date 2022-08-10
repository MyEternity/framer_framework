def parse(buffer: str):
    result = {}
    if buffer:
        params = buffer.split('&')
        for item in params:
            k, v = item.split('=')
            result[k] = v
    return result


class GetRequest:

    @staticmethod
    def request_params(environ):
        query = environ['QUERY_STRING']
        return parse(query)


class PostRequest:

    @staticmethod
    def wsgi_input(env) -> bytes:
        content_length_data = env.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        return env['wsgi.input'].read(content_length) if content_length > 0 else b''

    def wsgi_data(self, data: bytes) -> dict:
        result = {}
        if data:
            result = parse(data.decode(encoding='utf-8'))
        return result

    def request_params(self, environ):
        return self.wsgi_data(self.wsgi_input(environ))
