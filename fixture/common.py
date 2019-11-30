

class CommonHelper:
    def fill_fields(self, model_part):
        wd = self.wd
        for key, value in model_part.__dict__.items():
            if value:
                wd.find_element_by_name(key).click()
                wd.find_element_by_name(key).clear()
                wd.find_element_by_name(key).send_keys(value)