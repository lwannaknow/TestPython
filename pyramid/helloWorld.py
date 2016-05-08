__author__ = 'Administrator'
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='hello')
def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)


if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/hello/{name}')
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('127.0.0.1', 8080, app)
    server.serve_forever()
