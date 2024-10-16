from selenium import webdriver

def init_browser(search_engine_url):
    search_engine_url = search_engine_url
    browser = webdriver.Chrome()
    browser.get(search_engine_url)
    return browser
