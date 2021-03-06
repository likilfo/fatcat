import pytest
from model.group import Group
from model.user import User
from fixture.db import DbFixture
from fixture.application import Application
from generator.contacts import GENERATE_OONTACTS
from pathlib import Path
import yaml, importlib
import jsonpickle, os

fixture = None
config = None

def load_config(config_file):
    global config
    root_path = Path(__file__).parent.absolute()
    if config is None:
        with open(root_path / config_file) as fp:
            config = yaml.load(fp.read())
    return config


@pytest.fixture
def app(request):
    global fixture
    web_config = load_config(request.config.getoption('--config'))['web']
    browser = request.config.getoption('--browser')
    if not fixture or not fixture.is_valid():
        fixture = Application(browser=browser, url=web_config['baseUrl'])
    fixture.session.ensure_login(web_config['username'], web_config['password'])
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return app


@pytest.fixture(scope='session')
def db(request):
    db_config = load_config(request.config.getoption('--config'))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'],
                          user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture
def create_group(db):
    if not fixture.group.is_exist():
        if fixture.group.count() == 0:
            fixture.group.create(Group(name=fixture.group.random_string(),
                               header=fixture.group.random_string(),
                               footer=fixture.group.random_string()))
    return db.get_group_list()


@pytest.fixture
def create_contact(db):
    if not fixture.contact.is_exist():
        fixture.contact.create(User(firstname=fixture.group.random_string(),
                                     middlename=fixture.group.random_string(),
                                     lastname=fixture.group.random_string(),
                                     nickname=fixture.group.random_string(),
                                     title=fixture.group.random_string(),
                                     company=fixture.group.random_string(),
                                     home = fixture.group.random_phone(),
                                     mobile = fixture.group.random_phone(),
                                     work = fixture.group.random_phone(),
                                     address = fixture.group.random_address(),
                                     email = fixture.group.random_email(),
                                     email2 = fixture.group.random_email(),
                                     email3 = fixture.group.random_email()))
    return db.get_contact_list()

def load_from_module(module):
    return importlib.import_module('data.%s' % module).test_data


def load_from_json(data_file):
    path = Path(__file__).parent.absolute() / ('data/%s.json' % data_file)
    if not os.path.exists(path):
        GENERATE_OONTACTS
    with open(path) as fp:
        return jsonpickle.decode(fp.read())


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith('data_'):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith('json_'):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


@pytest.fixture
def check_ui(request):
    return request.config.getoption('--check_ui')


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--config', action='store', default='config.yaml')
    parser.addoption('--check_ui', action='store_true')



