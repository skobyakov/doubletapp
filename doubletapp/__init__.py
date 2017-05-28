from flask import Flask
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface


app = Flask(__name__)
app.config.from_object('config')
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)

from .event.views import event_page
app.register_blueprint(event_page, url_prefix='/event')

import flask_admin as admin
from flask_admin.contrib.mongoengine import ModelView
from doubletapp.event.models import Event, User, AdvertisingCompany, Icon
from doubletapp.event import views

admin = admin.Admin(app, 'Admin Interface')
admin.add_view(ModelView(Event))
admin.add_view(ModelView(User))
admin.add_view(ModelView(AdvertisingCompany))
admin.add_view(ModelView(Icon))