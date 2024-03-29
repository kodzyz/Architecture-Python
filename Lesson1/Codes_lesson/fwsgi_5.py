from wsgiref.simple_server import make_server


# 00:52

# page controller
def index_view(request):
    print(request)
    return '200 OK', [b'Index']


def abc_view(request):
    print(request)
    return '200 OK', [b'ABC']


def not_found_404_view(request):
    print(request)
    return '404 WHAT', [b'404 PAGE Not Found']


routes = {
    '/': index_view,
    '/abc/': abc_view,
}


class Application:

    def __init__(self, routes):
        self.routes = routes

    def __call__(self, environ, start_response):

        path = environ['PATH_INFO']
        if path == '/':
            start_response('200 OK', [('Content-Type', 'text/html')])
            return [b'Index']
        elif path == '/abc/':
            start_response('200 OK', [('Content-Type', 'text/html')])
            return [b'ABC']
        else:
            start_response('404 Not Found', [('Content-Type', 'text/html')])
            return [b'404 Not Found']


application = Application(routes)

with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
