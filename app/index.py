import math
from flask import render_template, request, redirect, jsonify, session
from flask_login import login_user
import dao
import utils
from app import app, login,admin
from app.models import *
import hashlib
from app.templates import cypher


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calendar')
def calendar():
    return render_template('/pages/calendar.html')


@app.route('/contact')
def contact():
    return render_template('/pages/contact.html')


@app.route('/edu')
def edu():
    return render_template('/pages/edu.html')


@app.route('/news')
def news():
    return render_template('/pages/news.html')


@app.route('/paymentGuide')
def payment_guide():
    return render_template('/pages/paymentGuide.html')


@app.route('/services')
def services():
    return render_template('/pages/services.html')


# @app.route('/admin/login', methods=['post'])
# def admin_login():
#     request.form.get('username')
#     request.form.get('password')


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/login_admin", methods=['get', 'post'])
def login_admin():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        user = dao.authenticated_user(username, password)
        if user:
            login_user(user=user)

    return redirect("/admin")


if __name__ == '__main__':
    app.run(debug=True)
