from flask import Flask
from flask_restful import Api

from common.config import DevelopmentConfig
from common.routes import initialise_routes

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
api = Api(app)

initialise_routes(api)
app.run()
