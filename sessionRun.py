from datetime import date
from json.tool import main
from os import wait
from tesseractControls.tesseractUtils import numpyImageToText
from webControls.webControllerFacade import webControllerFacade
from utils import getFBSidePane, getFBfeedScreenshot
import datetime
from PIL import Image

def saveImageToPng(numpyImage, basePathAndName):
    im = Image.fromarray(numpyImage)
    imageFilePath = basePathAndName + ".png"
    im.save(imageFilePath)

def saveTextToFile(stringValue,basePathAndName):
    textFilePath = basePathAndName + ".txt"
    with open(textFilePath, "w") as out_f:
        out_f.write(stringValue + "\n")



def runSession(webFacade,numberOfScrolls=30,outputDirectory="./dump/"):
    nameDelim = "_"
    webFacade.goToAuthenticatedFacebookPage()    
    totalText= ""

    sponsoredShot = getFBSidePane(webFacade)
    outputBasename = outputDirectory + "sidePane_img" + nameDelim + str(datetime.datetime.now())
    saveImageToPng(sponsoredShot,outputBasename)
    text = numpyImageToText(sponsoredShot)
    saveTextToFile(text,outputBasename)

    for x in range(numberOfScrolls):

        clippedShot = getFBfeedScreenshot(webFacade)
        outputBasename = outputDirectory + "img" + str(x) + nameDelim + str(datetime.datetime.now())

        # Begin Image store
        saveImageToPng(clippedShot,outputBasename)

        # Begin text store
        text = numpyImageToText(clippedShot)
        saveTextToFile(text,outputBasename)
        
        totalText += text + "\n\n"
        webFacade.scrollDownOnePage()

    finalTextFile = outputDirectory + "total_text_" + str(datetime.datetime.now())
    saveTextToFile(totalText,finalTextFile)
    


webFacade = webControllerFacade()
runSession(webFacade)
