import os

LOG_DIR = os.path.join(os.getcwd(), 'app/modules/')
MONGO_URI= 'YOUR MONGO URI'

class Config(object):
    JSON_AS_ASCII = False
    DEBUG = True
    TESTING = True