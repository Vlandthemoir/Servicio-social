from flask import Blueprint

cms = Blueprint('cms',__name__,
                 template_folder='templates',
                 static_folder='static')
from . import routes
