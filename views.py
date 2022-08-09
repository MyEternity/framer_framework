from framer_framework.templator import render


class Main:
    def __call__(self, request):
        return '200 OK', render('index.html', data=request.get('data', None))


class Info:
    def __call__(self, request):
        return '200 OK', render('info.html', data=request.get('data', None))


class Contacts:
    def __call__(self, request):
        return '200 OK', render('contacts.html', data=request.get('data', None))