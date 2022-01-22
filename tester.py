from os import wait
from tesseractControls.tesseractUtils import numpyImageToText
from webControls.webControllerFacade import webControllerFacade
from utils import getFBSidePane, getFBfeedScreenshot

webFacade = webControllerFacade()

webFacade.goToAuthenticatedFacebookPage()

webFacade.scrollDownOnePage()


webFacade.scrollDownOnePage()

numpyImg = webFacade.takeScreenShot()

from matplotlib import pyplot as plt

# A plot of the image
plt.imshow(numpyImg, interpolation='nearest')
plt.show()


clippedShot = getFBfeedScreenshot(webFacade)
plt.imshow(clippedShot, interpolation='nearest')
plt.show()

print("The image extracted Feed text is")
print("------------------------------")

print(numpyImageToText(clippedShot))


sponsoredShot = getFBSidePane(webFacade)
plt.imshow(sponsoredShot, interpolation='nearest')
plt.show()


print("The image extracted Sponsored text is")
print("------------------------------")

print(numpyImageToText(sponsoredShot))
