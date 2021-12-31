from webControls.webControllerFacade import webControllerFacade


webFacade = webControllerFacade()

webFacade.goToAuthenticatedFacebookPage()

numpyImg = webFacade.takeScreenShot()

from matplotlib import pyplot as plt
plt.imshow(numpyImg, interpolation='nearest')
plt.show()
