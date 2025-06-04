import pytest
from selenium import webdriver

from Pages.main_page import Main_Page


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://blockstream.info/block/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732")
    request.cls.driver = driver
    main_page =Main_Page(driver)
    request.cls.main_page = main_page
    yield driver  # Run all other pytest_runtest_makereport non wrapped hooks
    driver.quit()