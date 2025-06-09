from flask import Flask
from .models import db
from .routes import bp as main_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main_blueprint)

    return app
