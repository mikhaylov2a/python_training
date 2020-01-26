# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login("admin", "secret")
    app.create_contact(Contact(firstname="john", middlename="j", lastname="smith", nickname="neo",
                               title="title", companyname="RealCo", firstaddress="1st Street",
                               homephone="666666", mobilephone="+79657766664", workphone="666666 6",
                               faxphone="666666 66", firstemail="jphnsmith@email.com",
                               secondemail="johnsmith2@email.com", thirdemail="johnsmith3@email.com",
                               homepage="https://smith.net", secondaddress="2nd Street", phone2="3rd NY",
                               notes="Just New Guy"))
    app.logout()
