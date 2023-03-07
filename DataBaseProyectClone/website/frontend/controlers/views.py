from flask import Blueprint, render_template, request, flash
from .controlers import ProductsList

views = Blueprint('views', __name__, template_folder='../templates/')

@views.route('/', methods = ['GET', 'POST'])
def shop():
    products = ProductsList()
    cartProducts= 2
    cartTotal = 0
    return render_template('shop.html', 
                           products = products,
                           cartProducts = cartProducts,
                           cartTotal = cartTotal,)