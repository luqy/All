import pytest
import pytestselenium.config.config as cf
from pytestselenium.page_object.select_page import register_page
class TestRegister():
    driver=cf.get_value("driver")
    register_page=register_page(driver)
    def test_open_register_page(self):
        try:
            self.register_page.Loginemail()
            self.register_page.EnterIframe()
        except Exception:
            raise Exception

