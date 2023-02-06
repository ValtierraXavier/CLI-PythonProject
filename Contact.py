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
    number = CharField()
    type = CharField()

# db.drop_tables([contacts])
# db.create_tables([contacts])

# xavier = contacts(first_name = 'Xavier', last_name = 'Valt', number = '8625549989', type = 'Mobile')
# xavier.save()
# jasmine = contacts(first_name = 'Jasmine', last_name = 'Mil', number = '8627774779', type = 'Mobile')
# jasmine.save()
# jason = contacts(first_name = 'Jason', last_name = 'Mil', number = '9735549989', type = 'Mobile')
# jason.save()
# fred = contacts(first_name = 'Fred', last_name = 'Mers', number = '6467788899', type = 'Sat-Phone')
# fred.save()
# hideki = contacts(first_name = 'Hideki', last_name = 'Nakugama', number = '9175549989', type = 'Land-Line')
# hideki.save()
# jesus = contacts(first_name = 'Jesus', last_name = 'Christ', number = '0000000001', type = 'Holy-Line')
# jesus.save()

def find_contact():
    name_input = input('Find a contact by first name: ')
    get_specific_contact = contacts.get(contacts.first_name == name_input)
    print(f'\nContact for: {name_input}\n\nFirst Name: {get_specific_contact.first_name}    ||  Last Name:  {get_specific_contact.last_name}\n\nNumber:  {get_specific_contact.number}    ||  Type:  {get_specific_contact.type}\n')
    exit_or_stay()
    
# def open_contacts():
#     i=1
#     while i < 7:
#         get_list_of_names = contacts.get(i)
#         print(f'\nFirst Name: {get_list_of_names.first_name}\nLastname: {get_list_of_names.last_name}\nNumber: {get_list_of_names.number}\nType: {get_list_of_names.type}\n')
#         i+=1

def open_contacts():
    get_contacts = contacts.select().execute()
    all_contacts = list(get_contacts)
    for contact in all_contacts:
        print(f'\nFirst Name: {contact.first_name}\nLastname: {contact.last_name}\nNumber: {contact.number}\nType: {contact.type}\n')
    exit_or_stay()

def add_contacts():
    add_first_name_input = input('Enter the first name ')
    add_last_name_input = input('Enter the last name ')
    add_number_input = input('Enter the number ')
    add_type_input = input('Enter the type of phone ')
    contacts.create(first_name = add_first_name_input, last_name = add_last_name_input, number = add_number_input, type = add_type_input)
    print(f'\n\nAdded contact {add_first_name_input}:\nFirst Name: {add_first_name_input}\nLast Name: {add_last_name_input}\nNumber: {add_number_input}\nType: {add_type_input}\n')
    exit_or_stay()

def exit_or_stay():
    exit_input = input('Exit?(Y/N) ')
    if exit_input == "n" or exit_input == "N":
        table_of_contacts()
    elif exit_input == "y" or exit_input == "Y":
        return

def table_of_contacts():
    choice = input("What would you like to do? See contacts (l), Get specific contact (g), Add contact (a): ")
    if choice == 'l' or choice == 'L':
        open_contacts()
        # exit_or_stay()

    elif choice == 'g' or choice == 'G':
        find_contact()
        # exit_or_stay()
        
    elif choice == 'a' or choice == 'A':
        print("Let's add a contact")
        add_contacts()
        # exit_or_stay()
        

table_of_contacts()