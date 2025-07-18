# (c) @TheLx0980
# Year : 2023

import logging, re
from os import environ

id_pattern = re.compile(r'^.\d+$')



API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
SESSION = environ.get('SESSION', '')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
DB_URL = environ.get('DB_URL', '')

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
