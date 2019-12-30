from flask import Flask

app = Flask(__name__)
app.config.from_object('config.Config')

from app.views import baseAPI, userAPI

app.register_blueprint(baseAPI.base, url_prefix='/api/v1')
app.register_blueprint(userAPI.user, url_prefix='/api/v1/user')
