from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'
    
    from .frontend.controlers.views import views
    
    app.register_blueprint(views, url_prefix='/')
    
    from .frontend.models.models import Products
    
    return app