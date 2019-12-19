from fixture.common import CommonHelper
from model.user import User
from pathlib import Path

c = CommonHelper()
testdata = [User(firstname='', middlename='',
                  lastname='', nickname='',
                  title='', company='', home='',
                  mobile='', work='', address='',
                  email='', email2='',email3='')] + \
            [User(firstname=c.random_string(),
                  middlename=c.random_string(),
                  lastname=c.random_string(),
                  nickname=c.random_string(),
                  title=c.random_string(),
                  company=c.random_string(),
                  address=c.random_address(),
                  home=c.random_phone(),
                  work=c.random_phone(),
                  mobile=c.random_phone(),
                  email=c.random_email(),
                  email2=c.random_email(),
                  email3=c.random_email())
             for i in range(5)]

data_file = Path(__file__).parent.parent.absolute() / 'data/contacts.json'
c.create_data_file(data_file, testdata)
test_data = c.load_from_json(data_file)