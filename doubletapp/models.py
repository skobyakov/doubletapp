from doubletapp import db


class Icon(db.Document):
    title = db.StringField()
    image = db.ImageField()

    def __unicode__(self):
        return self.title


class Event(db.Document):
    title = db.StringField(max_length=32, required=True)
    organizer = db.StringField(max_length=32)
    logo = db.ImageField()
    description = db.StringField(max_length=128)
    what = db.StringField(max_length=32)
    where = db.StringField(max_length=32)
    when = db.StringField(max_length=32)
    icons = db.ListField(db.ReferenceField(Icon))
    location = db.StringField()
    call = db.StringField()
    website = db.URLField()

    def __unicode__(self):
        return self.title


class User(db.Document):
    name = db.StringField(required=True)
    gender = db.StringField(choices=['male', 'female'])
    age = db.IntField()
    coordinates = db.StringField()

    def __unicode__(self):
        return self.name


class AdvertisingCompany(db.Document):
    title = db.StringField(required=True)
    event = db.ReferenceField('Event')
    audience = db.ListField(db.ReferenceField(User))
    date = db.DateTimeField()
    coordinates = db.StringField()

    def __unicode__(self):
        return self.title


Icon.register_delete_rule(Event, 'icons', 1)
User.register_delete_rule(AdvertisingCompany, 'audience', 1)