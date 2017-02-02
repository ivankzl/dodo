import json

import falcon
import psycopg2


class StatusResource(object):

    """ Clase que informa sobre el estado de la conexion a la BD
    """

    def on_get(self, req, resp):

        status = {'status': 'ok'}
        resp.body = json.dumps(status)
        resp.status = falcon.HTTP_200

        # try:
        #     conn = psycopg2.connect(DSN)
        #     cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        #     cur.execute("select 1")
        #     import ipdb; ipdb.set_trace()
        #     cur.close()
        #     conn.close()
        # except:
        #     print ("No se pudo conectar a la base de datos")
        #     status = {'status': 'no se pudo conectar  a la base de datos'}
        #     resp.body = json.dumps(status)
        #     resp.status = falcon.HTTP_504
        #     resp.body = json.dumps(status)

        # resp.status = falcon.HTTP_200
