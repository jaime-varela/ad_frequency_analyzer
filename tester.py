# A test file to check selenium and other tools

# from selenium import webdriver
# from selenium.webdriver.chrome import service
# from selenium.webdriver.chrome.service import Service
# from decouple import config



# # driver initialization
# service = Service(config('WEBDRIVER_EXEC_PATH'))
# driver = webdriver.Chrome(service=service)
# # launch URL
# driver.get("https://www.tutorialspoint.com/index.htm")


# from PIL import Image
# import io
# import numpy as np

# pngImg = driver.get_screenshot_as_png()
# img = Image.open(io.BytesIO(pngImg))
# numpy_array = np.asarray(img)

# print(numpy_array)

# driver.close()

from webControls.webControllerFacade import webControllerFacade


webFacade = webControllerFacade()

webFacade.goToURL("https://www.tutorialspoint.com/index.htm")

numpyImg = webFacade.takeScreenShot()

from matplotlib import pyplot as plt
plt.imshow(numpyImg, interpolation='nearest')
plt.show()
