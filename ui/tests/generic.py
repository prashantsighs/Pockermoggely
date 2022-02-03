from selenium import webdriver
url = "https://pokerwebsite.pokermoogley.com/profile/#"
import  pytest
driver = None

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()