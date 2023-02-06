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

xavier = contacts(first_name = 'Xavier', last_name = 'Valt', number = 8625549989, type = 'mobile')
xavier.save()
jasmine = contacts(first_name = 'Jasmine', last_name = 'Mil', number = 8627774779, type = 'mobile')
xavier.save()
xavier = contacts(first_name = 'Jason', last_name = 'Mil', number = 9735549989, type = 'mobile')
xavier.save()
xavier = contacts(first_name = 'Fred', last_name = 'Mers', number = 6467788899, type = 'Sat')
xavier.save()
xavier = contacts(first_name = 'Hideki', last_name = 'Nakugama', number = 9175549989, type = 'Land-Line')
xavier.save()
xavier = contacts(first_name = 'Jesus', last_name = 'Christ', number = 100000000, type = 'Holy')
xavier.save()

