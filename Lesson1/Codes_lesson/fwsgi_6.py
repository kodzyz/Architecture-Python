from wsgiref.simple_server import make_server


# 00:55
# python fwsgi_6.py
# Заходим в браузер: http://127.0.0.1:8000/
#                    http://127.0.0.1:8000/abc/


def index_view():
    return '200 OK', [b'Index']  # код и тело ответа


def abc_view():
    return '200 OK', [b'ABC']


def not_found_404_view():
    return '404 WHAT', [b'404 PAGE Not Found']


routes = {
    '/': index_view,
    '/abc/': abc_view,
}


# независимый от routes и view # 00:57
class Application:

    def __init__(self, routes):
        self.routes = routes

    # вызов объекта как функции
    def __call__(self, environ, start_response):

        path = environ['PATH_INFO']
        if path in self.routes:  # '/'
            view = self.routes[path]  # index_view
        else:
            view = not_found_404_view
        code, body = view()  # index_view()
        start_response(code, [('Content-Type', 'text/html')])
        return body


application = Application(routes)

with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
