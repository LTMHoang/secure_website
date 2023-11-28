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
    kw = request.args.get('kw')
    cate_id = request.args.get('cate_id')
    page = request.args.get('page')

    pros = dao.load_products(kw, cate_id, page)
    num = dao.count_product()

    return render_template('index.html', products=pros,
                           pages=math.ceil(num/app.config["PAGE_SIZE"]))


@app.route('/admin/login', methods=['post'])
def admin_login():
    request.form.get('username')
    request.form.get('password')


@app.route('/api/cart', methods=['post'])
def add_to_cart():
    """
    {
        "cart": {
            "1": {
                "id": "1",
                "name": "ABC",
                "price": 12,
                "quantity": 1
            }
        }
    }
    :return:
    """

    data = request.json

    cart = session.get('cart')
    if cart is None:
        cart = {}

    id = str(data.get("id"))
    if id in cart:
        cart[id]['quantity'] += 1
    else:
        cart[id] = {
            "id": id,
            "name": data.get('name'),
            "price": data.get('price'),
            "quantity": 1
        }

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))


@app.route('/cart')
def cart():
    return render_template('cart.html')


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


@app.context_processor
def common_response():
    return {
        'categories': dao.load_categories(),
        'cart': utils.count_cart(session.get('cart'))
    }


if __name__ == '__main__':
    from app import admin
    app.run(debug=True)