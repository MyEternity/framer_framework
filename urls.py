from views import Main, Info, Contacts


def data(request):
    request['data'] = 123


def key(request):
    request['key'] = '123'


fronts = [data, key]

routes = {
    '/': Main(),
    '/info/': Info(),
    '/contacts/': Contacts(),
}
