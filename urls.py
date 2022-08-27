from datetime import date


def data(request):
    request['data'] = {}
    request['objects'] = {}
    request['date'] = date.today()


def key(request):
    request['key'] = ''


fronts = [data, key]

