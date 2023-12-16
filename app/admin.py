from flask import redirect
from flask_admin import BaseView, expose, Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, logout_user

from app import db, admin, app
from app.models import HocVien, KhoaHoc, DangKy, LopHoc, GiaoVien, UserRoleEnum

admin = Admin(app=app, name='QUẢN TRỊ WEBSITE TIN HỌC', template_mode='bootstrap4')


class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class StatsView(AuthenticatedUser):
    @expose("/")
    def index(self):
        return self.render('admin/stats.html')


class LogoutView(AuthenticatedUser):
    @expose('/')
    def index(self):
        logout_user()

        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated


class MyHocVienView(AuthenticatedAdmin):
    column_list = ['id', 'ho_ten', 'ngay_sinh', 'dia_chi', 'email']
    can_export = True
    column_searchable_list = ['ho_ten']
    column_filters = ['ho_ten']
    column_editable_list = ['ho_ten', 'ngay_sinh', 'dia_chi', 'email']
    details_modal = True
    edit_modal = True


class MyKhoaHocView(AuthenticatedAdmin):
    column_list = ['id', 'ten_khoa_hoc', 'mo_ta', 'dang_kys', 'email']
    can_export = True
    column_searchable_list = ['ten_khoa_hoc']
    column_filters = ['ten_khoa_hoc']
    column_editable_list = ['ten_khoa_hoc']
    details_modal = True
    edit_modal = True


class MyDangKyView(AuthenticatedAdmin):
    column_list = ['id', 'hoc_vien_id', 'khoa_hoc_id', 'ngay_dang_ky']
    can_export = True
    column_searchable_list = ['khoa_hoc_id','hoc_vien_id']
    column_filters = ['khoa_hoc_id','hoc_vien_id']
    column_editable_list = ['khoa_hoc_id','hoc_vien_id', 'ngay_dang_ky']
    details_modal = True
    edit_modal = True


class MyLopHocView(AuthenticatedAdmin):
    column_list = ['id', 'khoa_hoc_id', 'phong_hoc', 'thoi_gian', 'phong_hoc', 'giao_vien_id']
    can_export = True
    column_searchable_list = ['khoa_hoc_id', 'phong_hoc', 'giao_vien_id']
    column_filters = ['khoa_hoc_id', 'phong_hoc', 'giao_vien_id']
    column_editable_list = ['khoa_hoc_id', 'phong_hoc', 'giao_vien_id']
    details_modal = True
    edit_modal = True


class MyDiemView(AuthenticatedAdmin):
    column_list = ['id', 'hoc_vien_id', 'lop_hoc_id', 'diem_so']
    can_export = True
    column_searchable_list = ['hoc_vien_id', 'lop_hoc_id', 'diem_so']
    column_filters = ['hoc_vien_id', 'lop_hoc_id', 'diem_so']
    column_editable_list = ['hoc_vien_id', 'diem_so']
    details_modal = True
    edit_modal = True


class MyGiaoVienView(AuthenticatedAdmin):
    column_list = ['id', 'ten_giao_vien']
    can_export = True
    column_searchable_list = ['ten_giao_vien']
    column_filters = ['ten_giao_vien']
    column_editable_list = ['ten_giao_vien']
    details_modal = True
    edit_modal = True


admin.add_view(StatsView(name='Thống kê báo cáo'))
admin.add_view(LogoutView(name="Đăng xuất"))
admin.add_view(MyHocVienView(HocVien, db.session, name='Quản Lý Học Viên'))
admin.add_view(MyKhoaHocView(KhoaHoc, db.session, name='Quản Lý Khóa Học'))
admin.add_view(MyDangKyView(DangKy, db.session, name='Đăng Ký Khóa Học'))
admin.add_view(MyLopHocView(LopHoc, db.session, name='Quản Lý Lớp Học'))
admin.add_view(MyGiaoVienView(GiaoVien, db.session, name='Quản Lý Giáo Viên'))
