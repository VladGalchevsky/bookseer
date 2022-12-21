from .settings import PORTAL_URL


def books_proc(request):
    return {'PORTAL_URL': PORTAL_URL}
