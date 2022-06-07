from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import AuthorsBaseTest


class AuthorsRegisterTest(AuthorsBaseTest):
    def get_by_placeholder(self, web_element, placeholder):
        return web_element.find_element(
            By.XPATH, f'//input[@placeholder="{placeholder}"]'
        )
    
    def fill_form_imaginary_data(self,form):
        fields = form.find_elements(By.TAG_NAME, 'input')
        for field in fields:
            if field.is_displayed():
                field.send_keys(' '*20)

    def test_empyt_first_name_error_message(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.browser.find_element(
            By.XPATH,
            '/html/body/main/div[2]/form/div[1]' 
        )

        self.fill_form_imaginary_data(form)
        form.find_element(By.NAME, 'email').send_keys('anything@email.com')

        first_name_field = self.get_by_placeholder(form, 'Ex.: John')
        first_name_field.send_keys(' ')
        first_name_field.send_keys(Keys.ENTER)

        form = self.browser.find_element(
            By.XPATH,
            '/html/body/main/div[2]/form/div[1]' 
        )

        self.assertIn('Write your first name', form.text)


