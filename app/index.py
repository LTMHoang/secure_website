import math
from flask import render_template, request, redirect, jsonify, session
from flask_login import login_user
import dao
import utils
from app import app, login, admin
from app.models import *
import hashlib
from app.templates import cypher


@app.route('/')
def index():
    return render_template('index.html')


@app.context_processor
def common_response():
    return {

        'course': utils.count_course(session.get('course'))
    }


@app.route('/calendar')
def calendar():
    courses = dao.loadCourse()
    return render_template('/pages/calendar.html', courses=courses)


@app.route('/assets/calendar.html')
def calendar_assets():
    courses = dao.loadCourse()
    return render_template('/pages/calendar.html', courses=courses)


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
            if user.user_role == UserRoleEnum.ADMIN:
                login_user(user=user)
            else:
                return render_template('index.html')

    return redirect("/admin")


@app.route('/api/course', methods=['post'])
def add_to_course():
    """
    {
        "course":{
            "1":{
                "id": "1",
                "classname": "ABC",
                "starttime": "07:00:00",
                "endtime": "09:30:00",
                "startdate": "2023-12-20 00:00:00",
                "address":"Nguyễn Kiệm",
                "type":"Thiết kế website"
                "quantity": 2
            }, "2": {
                "id": "2",
                "classname": "xyz",
                "starttime": "07:00:00",
                "endtime": "09:30:00",
                "startdate": "2023-12-20 00:00:00",
                "address":"Nhà Bè",
                "type":"Lập trình di động"
                "quantity": 2
            }
        }
    }
    :return:
    """
    data = request.json

    course = session.get('course')
    if course is None:
        course = {}
    id = str(data.get('id'))
    if id in course:  # Khóa học đã được đăng
        course[id]['quantity'] += 1  # tăng sl khóa học lên 1
    else:  # Khóa học chữ được đăng ký
        course[id] = {
            "id": id,
            "classname": data.get('classname'),
            "starttime": data.get('starttime'),
            "endtime": data.get('endtime'),
            "startdate": data.get('startdate'),
            "address": data.get('address'),
            "type": data.get('type'),
            "quantity": 1
        }
    session['course'] = course
    print(course)

    # return jsonify({
    #     "total_amount": 100,
    #     "total_quantity": 10,
    # })

    return utils.count_course(course)

@app.route('/course')
def registercourse():
    return render_template('registercourse.html')

if __name__ == '__main__':
    from flask_sslify import SSLify

    sslify = SSLify(app)
    app.run(debug=True)
