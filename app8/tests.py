from django.test import TestCase, Client
from django.urls import resolve

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from .views import home
import time


#Create your tests here.

## -------------------------------------- Unit Test ----------------------------------------
class Story8Test(TestCase):
    def test_url_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code,200)  
    
    def test_story7_using_home_func(self):
        found = resolve('/')
        self.assertEqual(found.func, home)
    
    def test_inside_html(self):
        response=Client().get('')
        response_content = response.content.decode('utf-8')
        self.assertIn("Johanes Steven", response_content)
    
    def test_story_using_show_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'index.html')


## -------------------------------------- Functional Test ----------------------------------------
class Story8FunctionalTest(TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_argument('--no-sandbox')        
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('disable-gpu')
        chrome_path = r'/usr/local/bin/chromedriver' #path from 'which chromedriver'
        self.selenium = webdriver.Chrome(executable_path=chrome_path)
        # self.selenium = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
        super(Story8FunctionalTest, self).setUp()


    def tearDown(self):
        self.selenium.quit()
        super(Story8FunctionalTest, self).tearDown()

    def test_input_todo(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('https://story8j.herokuapp.com/')
        # selenium.get('localhost:8000')
        # find the form element
        selenium.implicitly_wait(1)

        acc1 = selenium.find_element_by_id('acc1')
        acc2 = selenium.find_element_by_id('acc2')
        acc3 = selenium.find_element_by_id('acc3')
        acc4 = selenium.find_element_by_id('acc4')

        # When clicked
        acc1.click()
        assert "under lockdown" in selenium.page_source
        time.sleep(2)

        acc2.click()
        assert "Yamaha" in selenium.page_source
        time.sleep(2)

        acc3.click()
        assert "Props" in selenium.page_source
        time.sleep(2)

        acc4.click()
        assert "Sempoa" in selenium.page_source
        time.sleep(2)

        print("OK")

        time.sleep(5)
