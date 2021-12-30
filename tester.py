from webControls.webControllerFacade import webControllerFacade


webFacade = webControllerFacade()

webFacade.goToURL("https://www.tutorialspoint.com/index.htm")

numpyImg = webFacade.takeScreenShot()

from matplotlib import pyplot as plt
plt.imshow(numpyImg, interpolation='nearest')
plt.show()
