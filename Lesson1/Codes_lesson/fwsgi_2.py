from wsgiref.simple_server import make_server


# python fwsgi_2.py
# Заходим в браузер: http://127.0.0.1:8000/

def application(environ, start_response):
    """
    по стандарту PEP-3333 принимает только два параметра
    :param environ: словарь данных от сервера
    :param start_response: функция для ответа серверу
    """
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Hello world from a simple WSGI application!']


with make_server('', 8000, application) as httpd:
    """
    00:44
    Запуск непосредственно из PyCharm (runserver)
    """
    print("Serving on port 8000...")
    httpd.serve_forever()
