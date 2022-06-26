import pytest
from selenium import webdriver


username = "prajvalmohan143"
# accessToken:  AccessToken can be genarated from automation dashboard or profile section
accessToken = "niBed4Rd3T3uTNad5gC0SdeSAGxctofBsSZ7TddTXIsFXLtUFW"
# gridUrl: gridUrl can be found at automation dashboard
gridUrl = "hub.lambdatest.com/wd/hub"

capabilities = {
    'LT:Options': {
        "build": "selenium_assignment",
        "name": "pytest",
        "platformName": "Windows 10"
    },
    "browserName": "Chrome",
    "browserVersion": "88.0",
}

url = "https://" + username + ":" + accessToken + "@" + gridUrl


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Remote(command_executor=url, desired_capabilities=capabilities)
    request.cls.driver = driver

    yield
    driver.close()
