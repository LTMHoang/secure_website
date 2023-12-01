import math
from flask import render_template, request, redirect, jsonify, session
from flask_login import login_user
import dao
import utils
from app import app, login
from app.models import *
import hashlib


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


@app.route('/calendar.html')
def pages():
    return render_template('/pages/calendar.html')


@app.route('/admin/login', methods=['post'])
def admin_login():
    request.form.get('username')
    request.form.get('password')


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/login-admin", methods=['get', 'post'])
def login_admin():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password", "")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        user = User.query.filter(User.username == username.strip(), User.password == password).first()
        if user:
            login_user(user=user)

    return redirect("/admin")


if __name__ == '__main__':
    from app import admin
    app.run(debug=True)