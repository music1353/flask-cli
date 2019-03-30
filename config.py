import os

# BASE_DIR = os.path.join(os.getcwd(), 'app/modules/')
LOG_DIR = os.path.join(os.getcwd(), 'app/logs/')
MONGO_URI= 'YOUR MONGO URI'

# try:
#     client = pymongo.MongoClient(MONGO_URI)
#     print('成功連接至mongodb')
# except:
#     print('連接mongodb失敗')

class Config(object):
    JSON_AS_ASCII = False
    DEBUG = True
    TESTING = True