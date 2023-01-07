def secret_front(request):
    request['secret'] = 'some secret'


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

request = {}
for front in fronts:
    front(request)
print(request)




