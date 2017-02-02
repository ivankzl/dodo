TRAC API - README
=================

¿Qué es?
--------



¿Cómo funciona?
---------------

La API está construida utilizando el framework minimalista Falcon, que permite
exponer servicios REST de manera muy simple y con una alta performance.

Requerimientos
--------------

* falcon
* psychopg2
* gunicorn


Recursos de la API (endpoints)
------------------------------

* GET /api/v1/status
--> Devuelve el estado de la conexión a la base de datos

