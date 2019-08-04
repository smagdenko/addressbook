
def test_contacts_on_home_page(app):

    contact_from_home_page = app.contact.get_contacts_list()[1]
    contact_from_edit_page = app.contact.get_info_from_edit_page(1)

    assert contact_from_edit_page.email_1 == contact_from_home_page.email_1
    assert contact_from_edit_page.email_2 == contact_from_home_page.email_2
    assert contact_from_edit_page.email_3 == contact_from_home_page.email_3


def test_phones_on_home_page(app):

    phones_from_home_page = app.contact.get_contacts_list()[1]
    phones_from_edit_page = app.contact.get_info_from_edit_page(1)

    assert phones_from_edit_page.work_phone == phones_from_home_page.work_phone
    assert phones_from_edit_page.home_phone == phones_from_home_page.home_phone
    assert phones_from_edit_page.mobile_phone == phones_from_home_page.mobile_phone
