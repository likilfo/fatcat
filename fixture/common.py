from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CommonHelper:
    def fill_fields(self, model_part):
        wd = self.wd
        for key, value in model_part.__dict__.items():
            if value:
                wd.find_element_by_name(key).click()
                wd.find_element_by_name(key).clear()
                wd.find_element_by_name(key).send_keys(value)

    def wait_for(self, path):
        try:
            WebDriverWait(self.wd, 10).until(
                EC.presence_of_element_located((By.XPATH, path))
            )
            return True
        except:
            return False
