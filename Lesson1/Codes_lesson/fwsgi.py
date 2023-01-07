def application(environ, start_response):
    """
    00:36
    :param environ: словарь данных от сервера(Nginx -> Gunicorn -> dict())
    :param start_response: функция для ответа серверу
    """
    # сначала в функцию start_response передаем код ответа и заголовки
    start_response('200 OK', [('Content-Type', 'text/html')])
    # возвращаем тело ответа в виде списка из bite
    return [b'Hello world from a simple WSGI application!']

# Для запуска можно использовать gunicorn или uwsgi или их аналоги

# gunicorn - wsgi-коннектор
# pip install gunicorn
# gunicorn simple_wsgi:application

# uwsgi
# pip install uwsgi
# uwsgi --http :8000 --wsgi-file simple_wsgi.py

# Заходим в браузер: http://127.0.0.1:8000/

