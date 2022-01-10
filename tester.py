from os import wait
from tesseractControls.tesseractUtils import numpyImageToTex
from webControls.webControllerFacade import webControllerFacade


webFacade = webControllerFacade()

webFacade.goToAuthenticatedFacebookPage()

webFacade.scrollDownOnePage()


webFacade.scrollDownOnePage()

numpyImg = webFacade.takeScreenShot()

from matplotlib import pyplot as plt

# A plot of the image
plt.imshow(numpyImg, interpolation='nearest')
plt.show()

print("The image extracted text is")
print("------------------------------")

print(numpyImageToTex(numpyImg))

