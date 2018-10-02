import logging

from pyramid.view import view_config

from bookish.lib import Request


logger = logging.getLogger(__name__)


@view_config(
    route_name='search',
    renderer='templates/search.jinja2',
)
def search(request):
    if 'isbn' in request.POST:
        request = Request(request.POST['isbn'])
        response = request.perform()

        return {
            'result': response,
        }

    return {}
