import pytest
from selenium.webdriver import ActionChains


@pytest.mark.usefixture("setup")
class Test_two:

    def test_secondProgram(self, setup):
        self.driver.get("https://www.lambdatest.com/selenium-playground")

        self.driver.implicitly_wait(20)

        self.driver.find_element_by_link_text("Drag & Drop Sliders").click()

        slider = self.driver.find_element_by_xpath("//*[@id='slider3']/div/input")

        move = ActionChains(self.driver)

        move.click_and_hold(slider).move_by_offset(120, 0).release().perform()

        range1 = self.driver.find_element_by_id("rangeSuccess").text

        assert range1 == "95"

        print("Test Passed")
