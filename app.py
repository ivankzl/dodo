import falcon
from resources.status import StatusResource
from settings.base import API_ROOT, API_VERSION

app = falcon.API()

status = StatusResource()


app.add_route(API_ROOT + API_VERSION + '/status', status)

