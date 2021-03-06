# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create_contact(Contact(firstname="john", middlename="j", lastname="smith", nickname="neo",
                               title="title", companyname="RealCo", firstaddress="1st Street",
                               homephone="666666", mobilephone="+79657766664", workphone="666666 6",
                               faxphone="666666 66", firstemail="jphnsmith@email.com",
                               secondemail="johnsmith2@email.com", thirdemail="johnsmith3@email.com",
                               homepage="https://smith.net", secondaddress="2nd Street", phone2="3rd NY",
                               notes="Just New Guy"))
    app.session.logout()
