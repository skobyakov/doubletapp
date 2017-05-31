from doubletapp import db


class Admin(db.Document):
    login = db.StringField()
    password = db.StringField()

    def __unicode__(self):
        return self.login

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)