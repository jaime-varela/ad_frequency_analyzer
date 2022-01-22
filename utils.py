

#Global params, change as needed
from math import floor

# On Jaimes PC the numbers are
#FB_LEFT_CROP_PERCENTAGE = 30
#FB_RIGHT_CROP_PERCENTAGE = 30

# On Marias monitor with Jaimes mac its
FB_LEFT_CROP_PERCENTAGE = 24
FB_RIGHT_CROP_PERCENTAGE = 25

# For top pane only
#FB_SPONSORED_AD_TOP_CLIP_PERCENTAGE= 5
#FB_SPONSORED_AD_CROP_PERCENTAGE= 45

# With two side panes
FB_SPONSORED_AD_TOP_CLIP_PERCENTAGE= 5


#---------------------- Begin Functions -------------------------#

def getFBfeedScreenshot(webFacade):
    '''Takes a web control facade and outputs a screenshot of the feed as numpy array'''
    fullScreenshot = webFacade.takeScreenShot()
    height , width , channels = fullScreenshot.shape
    leftIndex = int(floor((FB_LEFT_CROP_PERCENTAGE/100.0)*width))
    rightIndex = int(width - floor((FB_RIGHT_CROP_PERCENTAGE/100.0)*width))

    croppedScreenShot = fullScreenshot[:,leftIndex:rightIndex,:]
    return croppedScreenShot


def getFBSidePane(webFacade):
    '''Takes a web control facade and outputs a screenshot of the sponsored pane as numpy'''
    fullScreenshot = webFacade.takeScreenShot()
    height , width , channels = fullScreenshot.shape
    # the right crop percentage should be enough to have the sponsored pane
    leftIndex = int(width - floor((FB_RIGHT_CROP_PERCENTAGE/100.0)*width))

    top = int(height * (FB_SPONSORED_AD_TOP_CLIP_PERCENTAGE/100.0))
    croppedScreenShot = fullScreenshot[top:,leftIndex:,:]
    return croppedScreenShot

