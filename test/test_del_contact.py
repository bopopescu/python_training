
from model.contact import Contact
from random import randrange
import random

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(fname="first", lname="last", homeaddress="address", phone="789456123", email="first.last@gmail.com"))
    app.open_home_page()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    #index = randrange(len(old_contacts))
    app.contact.delete_contact_by_id(contact.id)
    app.open_home_page()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


