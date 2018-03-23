from peewee import *

database = MySQLDatabase('demo', **{'charset': 'utf8', 'use_unicode': True, 'host': 'localhost', 'user': 'root', 'passwd': ''})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class User(BaseModel):
    user_address = CharField()
    user_creator = IntegerField()
    user_datecreated = DateTimeField()
    user_dateupdated = DateTimeField()
    user_email = CharField()
    user_fullname = CharField()
    user = AutoField(column_name='user_id')
    user_nickname = CharField()
    user_pass = CharField()
    user_postcode = IntegerField()
    user_role = CharField()
    user_tel = CharField()
    user_updater = IntegerField()
    user_username = CharField()

    class Meta:
        table_name = 'user'

