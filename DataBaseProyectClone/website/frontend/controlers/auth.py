from flask import Blueprint, render_template, request, flash, redirect,url_for
from ..models.UserModel import User

auth = Blueprint('auth', __name__, template_folder='../templates/')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        
        