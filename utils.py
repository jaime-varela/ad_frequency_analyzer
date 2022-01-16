

#Global params, change as needed
from math import floor


FB_LEFT_CROP_PERCENTAGE = 30
FB_RIGHT_CROP_PERCENTAGE = 30

FB_SPONSORED_AD_TOP_CLIP_PERCENTAGE= 5
FB_SPONSORED_AD_CROP_PERCENTAGE= 45


#---------------------- Begin Functions -------------------------#

def getFBfeedScreenshot(webFacade):
    '''Takes a web control facade and outputs a screenshot of the feed as numpy array'''
    fullScreenshot = webFacade.takeScreenShot()
    height , width , channels = fullScreenshot.shape
    leftIndex = int(floor((FB_LEFT_CROP_PERCENTAGE/100.0)*width))
    rightIndex = int(width - floor((FB_RIGHT_CROP_PERCENTAGE/100.0)*width))

    croppedScreenShot = fullScreenshot[:,leftIndex:rightIndex,:]
    return croppedScreenShot


def getFBSponsoredSidePane(webFacade):
    '''Takes a web control facade and outputs a screenshot of the sponsored pane as numpy'''
    fullScreenshot = webFacade.takeScreenShot()
    height , width , channels = fullScreenshot.shape
    # the right crop percentage should be enough to have the sponsored pane
    leftIndex = int(width - floor((FB_RIGHT_CROP_PERCENTAGE/100.0)*width))

    top = int(height * (FB_SPONSORED_AD_TOP_CLIP_PERCENTAGE/100.0))
    bottom = int(height * (FB_SPONSORED_AD_CROP_PERCENTAGE/100.0))
    croppedScreenShot = fullScreenshot[top:bottom,leftIndex:,:]
    return croppedScreenShot

