import pytest

from selenium.webdriver.support.select import Select


@pytest.mark.usefixture("setup")
class Test_three:

    def test_thirdProgram(self, setup):
        self.driver.get("https://www.lambdatest.com/selenium-playground")

        self.driver.implicitly_wait(20)

        self.driver.find_element_by_link_text("Input Form Submit").click()

        self.driver.find_element_by_xpath("//*[@id='seleniumform']/div[6]/button").click()

        messagetoVerify = "Please include an '@' in the email address. 'xyz' is missing an '@'."

        myValidationmsg = self.driver.find_element_by_id("name").get_attribute("validationMessage")

        assert myValidationmsg == "Please fill out this field."
        self.driver.find_element_by_id("name").send_keys("sonu")

        self.driver.find_element_by_id("inputEmail4").send_keys("sonu@gmail.com")

        self.driver.find_element_by_id("inputPassword4").send_keys("pass123")

        self.driver.find_element_by_id("company").send_keys("xyz")

        self.driver.find_element_by_id("websitename").send_keys("www.google.com")

        se = Select(self.driver.find_element_by_name("country"))

        se.select_by_visible_text("United States")

        self.driver.find_element_by_id("inputCity").send_keys("abc")

        self.driver.find_element_by_id("inputAddress1").send_keys("abc")

        self.driver.find_element_by_id("inputAddress2").send_keys("abc")

        self.driver.find_element_by_id("inputState").send_keys("abc")

        self.driver.find_element_by_id("inputZip").send_keys("abc")

        self.driver.find_element_by_xpath("//*[@id='seleniumform']/div[6]/button").click()

        msg = self.driver.find_element_by_xpath("//*[@id='__next']/div[1]/section[3]/div/div/div[2]/div/p").text

        assert msg == "Thanks for contacting us, we will get back to you shortly."

        print("Test Passed")
