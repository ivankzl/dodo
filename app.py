import falcon
from resources.status import StatusResource
from resources.tickets import (ActivityResource, OwnerHistoryResource,
                               TicketResource, TicketsResource)
from resources.wiki import WikiResource
from settings.base import API_ROOT, API_VERSION

app = falcon.API()

status = StatusResource()
tickets = TicketsResource()
ticket = TicketResource()
wiki = WikiResource()
activity = ActivityResource()
owner_history = OwnerHistoryResource()

app.add_route(API_ROOT + API_VERSION + '/status', status)
app.add_route(API_ROOT + API_VERSION + '/tickets/{username}', tickets)
app.add_route(API_ROOT + API_VERSION + '/ticket/{project}/{ticket_id}', ticket)
app.add_route(API_ROOT + API_VERSION + '/wiki/{username}', wiki)
app.add_route(API_ROOT + API_VERSION + '/activity/{username}', activity)
app.add_route(API_ROOT + API_VERSION +
              '/owner-history/{username}', owner_history)
