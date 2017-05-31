from flask import Flask
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('config')
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)
login_manager = LoginManager()
login_manager.init_app(app)


from .event.views import event_page
from .auth.views import admin_auth_page
app.register_blueprint(event_page, url_prefix='/event')
app.register_blueprint(admin_auth_page, url_prefix='/admin')


import flask_admin as admin
from .event.models import Event, User, AdvertisingCompany, Icon
from .event import views
from .auth.models import Admin
from .auth.views import MyAdminIndexView, MyModelView


admin = admin.Admin(app, 'Admin Interface', index_view=MyAdminIndexView())
admin.add_view(MyModelView(Event))
admin.add_view(MyModelView(User))
admin.add_view(MyModelView(AdvertisingCompany))
admin.add_view(MyModelView(Icon))


@login_manager.user_loader
def load_admin(admin_id):
    return Admin.objects(pk=admin_id).first()