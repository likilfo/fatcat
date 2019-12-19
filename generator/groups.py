from model.group import Group
from fixture.common import CommonHelper
from pathlib import Path

c = CommonHelper()
testdata = [Group(name=c.random_string(),
                  header=c.random_string(),
                  footer=c.random_string())
             for i in range(5)] + \
            [Group(name='',
                   header='',
                   footer='')]


data_file = Path(__file__).parent.parent.absolute() / 'data/groups.json'
c.create_data_file(data_file, testdata)
test_data = c.load_from_json(data_file)