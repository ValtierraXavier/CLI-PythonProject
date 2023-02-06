from peewee import *

db = PostgresqlDatabase('contact_book', user='xaviervaltierra', password='242013',
                        host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db
class contacts(BaseModel):
    first_name = CharField()
    last_name = CharField()
    number = BigIntegerField()
    type = CharField()

db.drop_tables([contacts])
db.create_tables([contacts])

xavier = contacts(first_name = 'Xavier', last_name = 'valt', number = 8625549989, type = 'mobile')
xavier.save()