import pytest
from model.group import Group
from model.user import User
from fixture.application import Application
from pathlib import Path
import yaml, importlib
import jsonpickle

fixture = None
config = None

@pytest.fixture
def app(request):
    global fixture
    global config
    root_path = Path(__file__).parent.absolute()
    if config is None:
        with open(root_path / request.config.getoption('--config')) as fp:
            config = yaml.load(fp.read())
    browser = request.config.getoption('--browser')
    if not fixture or not fixture.is_valid():
        fixture = Application(browser=browser, url=config['baseUrl'])
    fixture.session.ensure_login(config['username'], config['password'])
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return app

@pytest.fixture
def create_group():
    if not fixture.group.is_exist():
        if fixture.group.count() == 0:
            fixture.group.create(Group(name=fixture.group.random_string(),
                               header=fixture.group.random_string(),
                               footer=fixture.group.random_string()))
    return fixture.group.get_group_list()


@pytest.fixture
def create_contact():
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
    return fixture.contact.get_contact_list()




def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--config', action='store', default='config.yaml')



