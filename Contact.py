from peewee import *

db = PostgresqlDatabase('people', user='xaviervaltierra', password='242013',
                        host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db
class Contact(BaseModel):
    name = CharField()
    number = IntegerField()
    type = CharField()

db.drop_tables([Contact])
db.create_tables([Contact])

