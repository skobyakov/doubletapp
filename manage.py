from flask_script import Manager
from doubletapp import app
from doubletapp.auth.models import Admin
import getpass


manager = Manager(app)


@manager.command
def runserver(port):
    print(port)
    app.run(host='127.0.0.1', port=8080)


@manager.command
def createadmin():
    login = input('Login: ')
    password = getpass.getpass('Password: ')
    admin = Admin(login=login, password=password)
    admin.save()


if __name__ == '__main__':
    manager.run()