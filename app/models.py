from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, Date, DateTime
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


# class Category(db.Model):
#     __tablename__ = 'category'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False, unique=True)
#     products = relationship('Product', backref='category', lazy=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Product(db.Model):
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False, unique=True)
#     price = Column(Float, default=0)
#     image = Column(String(200))
#     category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
#
#     def __str__(self):
#         return self.name


class HocVien(db.Model):
    __tablename__ = 'hoc_vien'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ho_ten = Column(String(50), nullable=False)
    ngay_sinh = Column(Date, nullable=False)
    dia_chi = Column(String(50))
    email = Column(String(50), unique=True)
    image = Column(String(255))
    dang_kys = relationship('DangKy', backref='hoc_vien')
    diems = relationship('Diem', backref='hoc_vien')

    def __str__(self):
        return self.ho_ten


class KhoaHoc(db.Model):
    __tablename__ = 'khoa_hoc'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ten_khoa_hoc = Column(String(50), nullable=False)
    mo_ta = Column(String(255))
    dang_kys = relationship('DangKy', backref='khoa_hoc')
    lop_hocs = relationship('LopHoc', backref='khoa_hoc')

    def __str__(self):
        return self.ten_khoa_hoc


class DangKy(db.Model):
    __tablename__ = 'dang_ky'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hoc_vien_id = Column(Integer, ForeignKey(HocVien.id))
    khoa_hoc_id = Column(Integer, ForeignKey(KhoaHoc.id))
    ngay_dang_ky = Column(DateTime, nullable=False)


class GiaoVien(db.Model):
    __tablename__ = 'giao_vien'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ten_giao_vien = Column(String(50), nullable=False)
    lop_hocs = relationship('LopHoc', backref='giao_vien')

    def __str__(self):
        return self.ten_giao_vien


class LopHoc(db.Model):
    __tablename__ = 'lop_hoc'
    id = Column(Integer, primary_key=True, autoincrement=True)
    giao_vien_id = Column(Integer, ForeignKey(GiaoVien.id))
    thoi_gian = Column(DateTime, nullable=False)
    phong_hoc = Column(String(50))
    khoa_hoc_id = Column(Integer, ForeignKey(KhoaHoc.id))


class Diem(db.Model):
    __tablename__ = 'diem'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hoc_vien_id = Column(Integer, ForeignKey(HocVien.id))
    lop_hoc_id = Column(Integer, ForeignKey(LopHoc.id))
    diem_so = Column(Float)


class QuanLyHocPhi(db.Model):
    __tablename__ = 'quan_ly_hoc_phi'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hoc_vien_id = Column(Integer, ForeignKey(HocVien.id))
    khoa_hoc_id = Column(Integer, ForeignKey(KhoaHoc.id))
    hoc_phi = Column(Float)
    ngay_thanh_toan = Column(DateTime)


if __name__ == '__main__':
    with app.app_context():
        # Tạo các bảng
        # db.create_all()

        import hashlib
        u = User(name='Admin', username='admin', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
                 user_role=UserRoleEnum.ADMIN)
        db.session.add(u)

        # c1 = Category(name='Canon')
        # c2 = Category(name='Sony')
        # c3 = Category(name='Nikon')
        # c4 = Category(name='Fujifilm')
        #
        # db.session.add_all([c1, c2, c3, c4])
        #
        # p1 = Product(name='Canon 750D', price=7500000, image='https://product.hstatic.net/200000354621/product/may-anh-dslr-canon-eos-750d-ef-s18-55-is-stm_40450531012c4f6f89c50efc4fb684de_grande.jpg', category_id=1)
        # p2 = Product(name='Sony A6000', price=10000000, image='https://binhminhdigital.com/storedata/images/product/sony-a6000-kit-1650-xam.jpg', category_id=2)
        # p3 = Product(name='Canon 600D', price=3500000, image='https://zshop.vn/images/detailed/89/600d.jpeg', category_id=1)
        # p4 = Product(name='Fujifilm X-T5', price=54490000, image='https://cdn.vjshop.vn/may-anh/mirrorless/fujifilm/fujifilm-x-t5/mirrorless-camera-fujifilm-x-t5.jpg', category_id=4)
        #
        # db.session.add_all([p1, p2, p3, p4])

        db.session.commit()
