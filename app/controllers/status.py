from flask import Blueprint

status = Blueprint('/', __name__)


@status.route('/')
def welcome():
  """
    Welcome to Flask apis
  """
  return 'Hello World'