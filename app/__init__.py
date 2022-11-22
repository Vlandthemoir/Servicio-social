from flask import Flask
from flask_mysqldb import MySQL

db = MySQL()


def create_app():
    

    app = Flask(__name__)
    app.secret_key = 'mysecretkey'

    #inicializacion de la base de datos
    app.config['MYSQL_HOST']='localhost'
    app.config['MYSQL_USER']='root'
    app.config['MYSQL_PASSWORD']='100tifico'
    app.config['MYSQL_DB']='servicio'
    db.init_app(app)

    # Registro de los Blueprints
    from .blog import blog
    app.register_blueprint(blog, url_prefix='/blog')

    from .cms import cms
    app.register_blueprint(cms, url_prefix='/cms')


    return app
