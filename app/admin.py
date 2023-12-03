from flask import redirect
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, logout_user

from app import app, db, admin
from app.models import Category, Product, HocVien, KhoaHoc, DangKy, LopHoc, GiaoVien, UserRoleEnum


class AuthenticatedAdminMV(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN


class AuthenticatedAdminBV(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN


class MyProductView(AuthenticatedAdminMV):
    column_list = ['id', 'name', 'price']
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['price', 'name']
    column_editable_list = ['name', 'price']
    details_modal = True
    edit_modal = True


class MyHocVienView(AuthenticatedAdminMV):
    column_list = ['id', 'ho_ten', 'ngay_sinh', 'dia_chi', 'email']
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['name']
    column_editable_list = ['ho_ten', 'ngay_sinh', 'dia_chi', 'email']
    details_modal = True
    edit_modal = True


class MyKhoaHocView(AuthenticatedAdminMV):
    column_list = ['id', 'ten_khoa_hoc', 'mo_ta', 'dang_kys', 'email']
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['name']
    column_editable_list = ['name', 'price']
    details_modal = True
    edit_modal = True


class MyDangKyView(AuthenticatedAdminMV):
    column_list = ['id', 'hoc_vien_id', 'khoa_hoc_id', 'ngay_dang_ky']
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['name']
    column_editable_list = ['name']
    details_modal = True
    edit_modal = True


class MyLopHocView(AuthenticatedAdminMV):
    column_list = ['id', 'khoa_hoc_id', 'phong_hoc', 'thoi_gian', 'phong_hoc', 'giao_vien_id']
    can_export = True
    column_searchable_list = ['khoa_hoc_id', 'phong_hoc', 'giao_vien_id']
    column_filters = ['khoa_hoc_id', 'phong_hoc', 'giao_vien_id']
    column_editable_list = ['khoa_hoc_id', 'phong_hoc', 'giao_vien_id']
    details_modal = True
    edit_modal = True


class MyDiemView(AuthenticatedAdminMV):
    column_list = ['id', 'hoc_vien_id', 'lop_hoc_id', 'diem_so']
    can_export = True
    column_searchable_list = ['hoc_vien_id', 'lop_hoc_id', 'diem_so']
    column_filters = ['hoc_vien_id', 'lop_hoc_id', 'diem_so']
    column_editable_list = ['hoc_vien_id', 'diem_so']
    details_modal = True
    edit_modal = True


class MyGiaoVienView(AuthenticatedAdminMV):
    column_list = ['id', 'ten_giao_vien']
    can_export = True
    column_searchable_list = ['ten_giao_vien']
    column_filters = ['ten_giao_vien']
    column_editable_list = ['ten_giao_vien']
    details_modal = True
    edit_modal = True


class MyCategoryView(AuthenticatedAdminBV):
    column_list = ['name', 'products']


class StatsView(AuthenticatedAdminBV):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')


class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()

        return redirect('/admin')
    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(StatsView(name='Thống kê báo cáo'))
admin.add_view(LogoutView(name="Đăng xuất"))
admin.add_view(MyHocVienView(HocVien, db.session))
admin.add_view(MyKhoaHocView(KhoaHoc, db.session))
admin.add_view(MyDangKyView(DangKy, db.session))
admin.add_view(MyLopHocView(LopHoc, db.session))
admin.add_view(MyGiaoVienView(GiaoVien, db.session))
