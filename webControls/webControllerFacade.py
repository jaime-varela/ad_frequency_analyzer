# Facade for web controller

# This file needs to provide a class interface for doing the following



from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from decouple import config
from PIL import Image
import io
import numpy as np
import time

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class webControllerFacade:
    """Web controller facade primarily to scroll through facebook"""



    def __init__(self,exec_path=config('WEBDRIVER_EXEC_PATH')):
        '''exec_path == webdriver exe path'''
        option = Options()

        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")

        # Pass the argument 1 to allow and 2 to block
        option.add_experimental_option("prefs", { 
            "profile.default_content_setting_values.notifications": 1 
        })

        self.__webservice__ = Service(ChromeDriverManager().install())
        self.__driver__ = webdriver.Chrome(chrome_options=option,service=self.__webservice__)
        # Fix the size
        self.__driver__.set_window_size(1280 ,1024)

    def goToURL(self,urlString):
        '''Open a url'''
        self.__driver__.get(urlString)



    def goToAuthenticatedFacebookPage(self,email=config('FB_EMAIL'),password=config('FB_PASSWORD')):
        '''Opens facebook.com with the email and password configuration'''
        self.goToURL(config('FB_LOGIN_URL'))
        time.sleep(1) # Wait for some time to load
        email_element = self.__driver__.find_element_by_id('email')
        email_element.send_keys(email) # Give keyboard input
 
        password_element = self.__driver__.find_element_by_id('pass')
        password_element.send_keys(password) # Give password as input too
 
        login_button = self.__driver__.find_element_by_id('loginbutton')
        login_button.click() # Send mouse click
 
        time.sleep(3) # Wait for 3 seconds for the page to show up        
        return

    def takeScreenShot(self):
        '''Returns a numpy array representing the screenshot image of the numpy array'''

        pngImg = self.__driver__.get_screenshot_as_png()
        img = Image.open(io.BytesIO(pngImg))
        numpy_array = np.asarray(img)
        return numpy_array

    def scrollDownOnePage(self):
        '''Scrolls down roughly one page in the current web session'''
        html = self.__driver__.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_DOWN)

        time.sleep(2) # Wait for 2 seconds for the page to show up        
        return


    def __del__(self):
        self.__driver__.close()

