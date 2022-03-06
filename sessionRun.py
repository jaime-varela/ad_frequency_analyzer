from tesseractControls.tesseractUtils import numpyImageToText
from webControls.webControllerFacade import webControllerFacade
from utils import getFBSidePane, getFBfeedScreenshot
from PIL import Image
import os
from decouple import config


def saveImageToPng(numpyImage, basePathAndName):
    im = Image.fromarray(numpyImage)
    imageFilePath = basePathAndName + ".png"
    im.save(imageFilePath)

def saveTextToFile(stringValue,basePathAndName):
    textFilePath = basePathAndName + ".txt"
    with open(textFilePath, "w") as out_f:
        out_f.write(stringValue + "\n")



def runSession(webFacade,numberOfScrolls=30,outputDirectory="./dump/"):
    if not os.path.exists(outputDirectory):
        os.makedirs(outputDirectory)

    nameDelim = "_"
    totalText= ""

    sponsoredShot = getFBSidePane(webFacade)
    outputBasename = outputDirectory + "sidePane_img"
    saveImageToPng(sponsoredShot,outputBasename)
    text = numpyImageToText(sponsoredShot)
    saveTextToFile(text,outputBasename)

    for x in range(numberOfScrolls):

        clippedShot = getFBfeedScreenshot(webFacade)
        outputBasename = outputDirectory + "img" + str(x)

        # Begin Image store
        saveImageToPng(clippedShot,outputBasename)

        # Begin text store
        text = numpyImageToText(clippedShot)
        saveTextToFile(text,outputBasename)
        
        totalText += text + "\n\n"
        webFacade.scrollDownOnePage()

    finalTextFile = outputDirectory + "total_text"
    saveTextToFile(totalText,finalTextFile)
    

if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.
    webFacade = webControllerFacade()
    webFacade.goToAuthenticatedFacebookPage(email=config('JAIME_FB_EMAIL'),password=config('JAIME_FB_PASSWORD'))
    runSession(webFacade)
