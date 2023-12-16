from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.secret_key = "14124512B3JKB12IBTIB3214TNY23KLBJ4TB3JKT3B4TUB3T43%%#%^46%$#^#$%@$%2"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/data_athttt?charset=utf8mb4" % quote(
    '123456a@A')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 1

db = SQLAlchemy(app)
login = LoginManager(app=app)
