from flask import Blueprint, render_template


admin_page = Blueprint('admin', __name__,
                       template_folder='templates',
                       static_folder='static')


@admin_page.before_request
def admin_verification():
    print('Admin detected')


@admin_page.route('/')
def admin():
    return render_template('admin/index.html')