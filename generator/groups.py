from model.group import Group
from fixture.common import CommonHelper
from pathlib import Path
import jsonpickle

c = CommonHelper()
testdata = [Group(name=c.random_string(),
                  header=c.random_string(),
                  footer=c.random_string())
             for i in range(5)] + \
            [Group(name='',
                   header='',
                   footer='')]


data_file = Path(__file__).parent.parent.absolute() / 'data/groups.json'
with open(data_file, 'w') as fp:
    jsonpickle.set_encoder_options('json', indent=2)
    fp.write(jsonpickle.encode(testdata))

def load_from_json():
    with open(data_file) as fp:
        return jsonpickle.decode(fp.read())

test_data = load_from_json()