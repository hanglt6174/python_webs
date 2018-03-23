# -*- coding: utf-8 -*-

import app.models.db as db
import app.models.pagination as pager


class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class User(BaseModel):
    user = AutoField(column_name='user_id')
    user_address = CharField()
    user_creator = IntegerField()
    user_datecreated = DateTimeField(default=datetime.datetime.now)
    user_dateupdated = DateTimeField(default=datetime.datetime.now)
    user_email = CharField()
    user_fullname = CharField()
    user_nickname = CharField()
    user_pass = CharField()
    user_postcode = IntegerField()
    user_role = CharField()
    user_tel = CharField()
    user_updater = IntegerField()
    user_username = CharField()

    class Meta:
        table_name = 'user'

    # ==========================================
    # 
    # get list by page
    # 
    # ==========================================

    def load(self, page):

        define_page = 10
        start = (page - 1) * define_page

        result = {}

        sql = "select count(id) as all_count from user"
        db.con.execute(sql)
        result = db.con.fetchone()

        result["pagination"] = pager.Pagination(page, define_page, result["all_count"])

        sql = "select * from user order by user_fullname"
        sql += ' limit %s, %s'
        db.con.execute(sql, (start, define_page))
        result["mangas"] = db.con.fetchall()

        return result

#insert to test ORM start
db.connect()
data1=Users(
            user_address = "address test1",
            user_creator = 0,
            user_email = "test1@mail.com",
            user_fullname = 'kazuo',
            user_nickname = "nickname1",
            user_pass = "123456",
            user_postcode = "036142",
            user_role = "2",
            user_tel = "12345678909",
            user_updater = 0,
            user_username = "username1"
            )
data2=Users(
            user_address = "address test2",
            user_creator = 0,
            user_email = "test2@mail.com",
            user_fullname = 'hanako',
            user_nickname = "nickname2",
            user_pass = "123456",
            user_postcode = "036142",
            user_role = "1",
            user_tel = "12345678909",
            user_updater = 0,
            user_username = "username2"
            )
data3=Users(
            user_address = "address test3",
            user_creator = 0,
            user_email = "test3@mail.com",
            user_fullname = 'masako',
            user_nickname = "nickname3",
            user_pass = "123456",
            user_postcode = "036142",
            user_role = "0",
            user_tel = "12345678909",
            user_updater = 0,
            user_username = "username3"
            )
 
data1.save()
data2.save()
data3.save()
database.close()
#insert to test ORM end