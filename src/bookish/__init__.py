from pyramid.config import Configurator


def main(_, **settings):
    config = Configurator(settings=settings)

    config.include('pyramid_jinja2')

    config.add_route('search', '/')
    config.scan('bookish.views')

    config.add_static_view(name='static', path='../../static')

    return config.make_wsgi_app()
