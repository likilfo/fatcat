

class ContactHelper:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd


    def create(self, user):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        for key, value in user.__dict__.items():
            wd.find_element_by_name(key).click()
            wd.find_element_by_name(key).clear()
            wd.find_element_by_name(key).send_keys(value)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("home").click()
