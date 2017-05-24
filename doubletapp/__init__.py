from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__, static_url_path='/static')
app.config.from_object('config')
db = MongoEngine(app)


import flask_admin as admin
from flask_admin.contrib.mongoengine import ModelView
from doubletapp.models import Event, User, AdvertisingCompany, Icon
from doubletapp import views

admin = admin.Admin(app, 'Admin Interface')
admin.add_view(ModelView(Event))
admin.add_view(ModelView(User))
admin.add_view(ModelView(AdvertisingCompany))
admin.add_view(ModelView(Icon))