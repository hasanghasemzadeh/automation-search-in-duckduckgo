from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, driver
from dotenv import load_dotenv

load_dotenv()

def search_target_word(browser:webdriver, target_word:str):
    search_box = browser.find_element(By.ID, 'searchbox_input')
    search_box.send_keys(target_word)

    seach_btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchbox_homepage"]/div/div/div')))
    seach_btn.click()
    WebDriverWait(browser, 10).until(EC.url_contains('&ia=web'))
    return browser
    

def find_target_article(browser:webdriver, target_text:str):
    
    article_list = browser.find_elements(By.TAG_NAME, 'article')
    
    for article in article_list:
        if target_text in article.text:
            return article.get_attribute('id')
    raise Exception(F"target article: {os.getenv('TARGET_ARTICLE_TITLE')} not found")


def open_target_article(browser:webdriver, article_elm_id:str):
    target_article = browser.find_element(By.ID, article_elm_id)
    target_article.click()
    
def target_page_validation(browser:webdriver):
    title = browser.title
    url = browser.current_url
    if ((title == os.getenv('TARGET_PAGE_TITLE')) and 
        (url == os.getenv('TARGET_PAGE_URL')) and
        (os.getenv('TARGET_PAGE_H_ONE_TAG') in browser.page_source)):
        return "Download Application Scenario Passed"
    else:
        return "Download Application Scenario Failed"

def senario_execution():
        browser = driver.init_browser(os.getenv('SEARCH_ENGINE_URL'))
        search_target_word(browser=browser, target_word=os.getenv('TARGET_SEARCH_KEYWORD'))
        target_elm_id = find_target_article(browser=browser, target_text=os.getenv('TARGET_ARTICLE_TITLE'))
        open_target_article(browser=browser, article_elm_id=target_elm_id)
        print(target_page_validation(browser=browser))
        