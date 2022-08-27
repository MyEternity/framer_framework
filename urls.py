from datetime import date

from views import Main, Info, Contacts, About, StudyPrograms, CoursesList, CreateCourse, CreateCategory, CategoryList, \
    CopyCourse


def data(request):
    request['data'] = {}
    request['objects'] = {}
    request['date'] = date.today()


def key(request):
    request['key'] = ''


fronts = [data, key]

routes = {
    '/': Main(),
    '/info/': Info(),
    '/contacts/': Contacts(),
    '/about/': About(),
    '/study_programs/': StudyPrograms(),
    '/courses-list/': CoursesList(),
    '/create-course/': CreateCourse(),
    '/create-category/': CreateCategory(),
    '/category-list/': CategoryList(),
    '/copy-course/': CopyCourse()
}
