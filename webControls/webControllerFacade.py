# Facade for web controller

# This file needs to provide a class interface for doing the following

# TODO: Take screenshots

# TODO: manage web sessions

# TODO: manage scrolling


from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service

from decouple import config
from PIL import Image
import io
import numpy as np
import time



class webControllerFacade:
    """Web controller facade primarily to scroll through facebook"""



    def __init__(self,exec_path=config('WEBDRIVER_EXEC_PATH')):
        self.__webservice__ = Service(exec_path)
        self.__driver__ = webdriver.Chrome(service=self.__webservice__)


    def goToURL(self,urlString):
        self.__driver__.get(urlString)



    def goToAuthenticatedFacebookPage(self,email=config('FB_EMAIL'),password=config('FB_PASSWORD')):
        self.goToURL(config('FB_LOGIN_URL'))
        time.sleep(1) # Wait for some time to load
        email_element = self.__driver__.find_element_by_id('email')
        email_element.send_keys(email) # Give keyboard input
 
        password_element = self.__driver__.find_element_by_id('pass')
        password_element.send_keys(password) # Give password as input too
 
        login_button = self.__driver__.find_element_by_id('loginbutton')
        login_button.click() # Send mouse click
 
        time.sleep(2) # Wait for 2 seconds for the page to show up        
        return

    def takeScreenShot(self):
        '''Returns a numpy array representing the screenshot image of the numpy array'''

        pngImg = self.__driver__.get_screenshot_as_png()
        img = Image.open(io.BytesIO(pngImg))
        numpy_array = np.asarray(img)
        return numpy_array



    def __del__(self):
        self.__driver__.close()

