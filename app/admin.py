from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from app import app, db
from app.models import Category, Product, UserRoleEnum
from flask_login import current_user, logout_user
from flask import redirect


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


class MyCategoryView(AuthenticatedAdminMV):
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


admin = Admin(app=app, name='QUẢN TRỊ BÁN HÀNG', template_mode='bootstrap4')
admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(StatsView(name='Thống kê báo cáo'))
admin.add_view(LogoutView(name="Đăng xuất"))