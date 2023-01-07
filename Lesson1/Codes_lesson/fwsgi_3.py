from wsgiref.simple_server import make_server


# python fwsgi_3.py
# Заходим в браузер: http://127.0.0.1:8000/
#                    http://127.0.0.1:8000/abc/


def application(environ, start_response):
    """
    00:47
    simple PC: маршрутизатор
    :param environ: словарь данных от сервера
    :param start_response: функция для ответа серверу
    """
    # print(type(environ))  # <class 'dict'>
    # print(environ)
    path = environ['PATH_INFO']  # 'PATH_INFO': '/'
    if path == '/':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Index']
    elif path == '/abc/':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'ABC']
    else:
        start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
        return [b'404 Not Found']


with make_server('', 8000, application) as httpd:
    """Запуск непосредственно из PyCharm"""
    print("Serving on port 8000...")
    httpd.serve_forever()
