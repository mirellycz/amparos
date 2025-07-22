from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'triomaravilha'  

    from app.routes.routes import auth_bp
    app.register_blueprint(auth_bp)

    return app
