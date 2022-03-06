##############################################
#
#
# Program which runs one session of the experiment and logs the data
#
#
##############################################


from webControls.webControllerFacade import webControllerFacade
from decouple import config
from sessionRun import runSession























if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.
    webFacadeMaria = webControllerFacade()
    webFacadeMaria.goToAuthenticatedFacebookPage(email=config('MARIA_FB_EMAIL'),password=config('MARIA_FB_PASSWORD'))
    
    runSession(webFacadeMaria,outputDirectory="")


    webFacadeJaime = webControllerFacade()
    webFacadeJaime.goToAuthenticatedFacebookPage(email=config('JAIME_FB_EMAIL'),password=config('JAIME_FB_PASSWORD'))
    runSession(webFacadeMaria,outputDirectory="")
    
    


