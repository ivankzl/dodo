# Base config
API_ROOT = '/api'
API_VERSION = '/v1'
DEVELOPMENT_PORT = 8090

# Database
DB_USER = 'dodo'
DB_PASSWORD = 'dodo'
DB_NAME = 'dodo'
DB_HOST = 'db'
DB_PORT = '5438'

DSN = ("dbname=" + DB_NAME + " user=" + DB_USER +
       " host=" + DB_HOST + " password=" + DB_PASSWORD)

try:
    from settings.settings_production import *
except ImportError:
    pass
