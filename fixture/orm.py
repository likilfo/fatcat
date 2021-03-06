from pony.orm import *
from model.group import Group


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='footer')


    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')


    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host,
                            database=name,
                            user=user,
                            password=password,
                            autocommit=True)
        self.db.generate_mapping()

    def convert_group_to_model(self, groups):
        def convert(group):
            return Group(id=gr)

    @db_session
    def get_group_list(self):
        return self.convert_group_to_model(list(select(g for g in ORMFixture.ORMGroup)))