from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'
    
    from .frontend.controlers.views import views
    from .frontend.controlers.auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .frontend.models.shopModels import Products
    from .frontend.models.UserModel import User
    
    return app