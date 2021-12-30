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



class webControllerFacade:
    """Web controller facade primarily to scroll through facebook"""



    def __init__(self,exec_path=config('WEBDRIVER_EXEC_PATH')):
        self.__webservice__ = Service(exec_path)
        self.__driver__ = webdriver.Chrome(service=self.__webservice__)


    def goToURL(self,urlString):
        self.__driver__.get(urlString)



    def goToAuthenticatedFacebookPage(self,loginOptions):
        return

    def takeScreenShot(self):
        '''Returns a numpy array representing the screenshot image of the numpy array'''

        pngImg = self.__driver__.get_screenshot_as_png()
        img = Image.open(io.BytesIO(pngImg))
        numpy_array = np.asarray(img)
        return numpy_array



    def __del__(self):
        self.__driver__.close()

