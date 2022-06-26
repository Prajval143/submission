import pytest


@pytest.mark.usefixture("setup")
class Test_one:

    def test_firstProgram(self, setup):
        self.driver.get("https://www.lambdatest.com/selenium-playground")

        self.driver.implicitly_wait(20)

        self.driver.find_element_by_link_text("Simple Form Demo").click()

        str_url = self.driver.current_url

        assert "simple-form-demo" in str_url

        value = "sonu"

        self.driver.find_element_by_xpath("//*[@id='user-message']").send_keys(value)

        self.driver.find_element_by_id("showInput").click()

        msg = self.driver.find_element_by_id("message").text

        assert msg == value

        print("Test Passed")
