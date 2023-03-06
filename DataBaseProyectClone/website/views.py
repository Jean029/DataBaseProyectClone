from flask import Blueprint, render_template, request, flash
from .controlers import ProductsList

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
def shop():
    products = ProductsList()
    return render_template('shop.html', products = products)