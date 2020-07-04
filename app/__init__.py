from flask import Flask
from app.controllers.status import status

def create_app():
  app = Flask(__name__)
  app.register_blueprint(status, url_prefix='/')

  return app