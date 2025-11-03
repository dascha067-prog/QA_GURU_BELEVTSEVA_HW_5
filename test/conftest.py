# conftest.py
import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_management():
    # Браузер и базовый URL
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1280
    browser.config.window_height = 900
    browser.config.timeout = 6.0

    yield

    # Корректно закрываем браузер после каждого теста
    browser.quit()

