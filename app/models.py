from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app import db, app
from flask_login import UserMixin
import enum

class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100), default='https://genshin-guide.com/wp-content/uploads/yae-miko.png')
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)

    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(200))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        #Tạo các bảng
        db.create_all()

        import hashlib
        u = User(name='Admin', username='admin', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()), user_role=UserRoleEnum.ADMIN)
        db.session.add(u)

        c1 = Category(name='Canon')
        c2 = Category(name='Sony')
        c3 = Category(name='Nikon')
        c4 = Category(name='Fujifilm')

        db.session.add_all([c1, c2, c3, c4])

        p1 = Product(name='Canon 750D', price=7500000, image='https://product.hstatic.net/200000354621/product/may-anh-dslr-canon-eos-750d-ef-s18-55-is-stm_40450531012c4f6f89c50efc4fb684de_grande.jpg', category_id=1)
        p2 = Product(name='Sony A6000', price=10000000, image='https://binhminhdigital.com/storedata/images/product/sony-a6000-kit-1650-xam.jpg', category_id=2)
        p3 = Product(name='Canon 600D', price=3500000, image='https://zshop.vn/images/detailed/89/600d.jpeg', category_id=1)
        p4 = Product(name='Fujifilm X-T5', price=54490000, image='https://cdn.vjshop.vn/may-anh/mirrorless/fujifilm/fujifilm-x-t5/mirrorless-camera-fujifilm-x-t5.jpg', category_id=4)

        db.session.add_all([p1, p2, p3, p4])

        db.session.commit()