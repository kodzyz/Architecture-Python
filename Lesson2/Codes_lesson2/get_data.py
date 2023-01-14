from wsgiref.simple_server import make_server


# http://127.0.0.1:8000/?id=1&category=10

def parse_input_data(data):  # data: 'id=1&category=10'
    result = {}  # result: {} / result: {'id': '1'} / result: {'id': '1', 'category': '10'}
    if data:

        params = data.split('&')  # params: ['id=1', 'category=10']
        for item in params:  # item: 'id=1' / # item: 'category=10'

            k, v = item.split('=')  # k: 'id'  v: '1' / # k: 'category'  v: '10'
            result[k] = v
    return result  # result: {'id': '1', 'category': '10'}


def application(environ, start_response):
    query_string = environ['QUERY_STRING']
    print(query_string)  # -> 'id=1&category=10'
    request_params = parse_input_data(query_string)
    print(request_params)  # -> {'id': '1', 'category': '10'}
    start_response('200 OK', [('Content-Type', 'text/html')])

    return [b'Hello world from a simple WSGI application!']


with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
