from os import wait
from webControls.webControllerFacade import webControllerFacade


webFacade = webControllerFacade()

webFacade.goToAuthenticatedFacebookPage()

webFacade.scrollDownOnePage()


webFacade.scrollDownOnePage()

numpyImg = webFacade.takeScreenShot()

from matplotlib import pyplot as plt
plt.imshow(numpyImg, interpolation='nearest')
plt.show()
