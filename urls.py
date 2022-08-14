from views import Main, Info, Contacts, About


def data(request):
    request['data'] = {}


def key(request):
    request['key'] = ''


fronts = [data, key]

routes = {
    '/': Main(),
    '/info/': Info(),
    '/contacts/': Contacts(),
    '/about/': About(),
}
