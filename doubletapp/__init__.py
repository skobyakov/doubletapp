from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config.from_object('config')
db = MongoEngine(app)


from .event.views import event_page
from .admin.views import admin_page
app.register_blueprint(event_page, url_prefix='/event')
app.register_blueprint(admin_page, url_prefix='/admin')