from flask_admin.contrib.mongoengine import ModelView
from flask_login import current_user, login_user
from flask_admin import AdminIndexView, expose
from flask import render_template, Blueprint, request, url_for, redirect
from .forms import LoginForm


admin_auth_page = Blueprint('admin_auth_page', __name__,
                            template_folder='templates')


@admin_auth_page.route('/login/', methods=('GET', 'POST'))
def login_view():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = form.get_user()
        login_user(user)
        return redirect(url_for('admin.index'))
    return render_template('auth/form.html', form=form)


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if current_user.is_authenticated:
            return self.render('admin/index.html')
        return redirect(url_for('admin_auth_page.login_view'))