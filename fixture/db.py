import pymysql.cursors
from model.group import Group
from model.user import User
from .common import CommonHelper
import re

class DbFixture:


    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = \
            pymysql.connect(host=host,
                            database=name,
                            user=user,
                            password=password,
                            autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select group_id, group_name, '
                               'group_header, group_footer '
                               'from group_list')
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name,
                                  header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def clear(self, sring):
        return re.sub('\r', '', sring)

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select id, firstname, lastname, address, mobile,'
                           ' home, work, email, email2, email3 from addressbook')
            contact_helper = CommonHelper()
            for row in cursor:
                (id, firstname, lastname, address, mobile, home, work, email, email2, email3) = row
                address = self.clear(address)
                all_phones = contact_helper.contacts_like_on_home_page([home, mobile, work])
                all_emails = contact_helper.contacts_like_on_home_page([email, email2, email3])
                list.append(User(id=str(id),
                                 firstname=firstname,
                                 lastname=lastname,
                                 address=address,
                                 home=home,
                                 mobile=mobile,
                                 work=work,
                                 email=email,
                                 email2=email2,
                                 email3=email3,
                                 all_phones=all_phones,
                                 all_emails=all_emails
                ))

        finally:
            cursor.close()
        return list

    def get_groups_for_contact(self, contact_id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select group_id from address_in_groups where id=%s', contact_id)
            for row in cursor:
                list.append(row[0])
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
