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
import datetime
import time





if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.
    webFacadeMaria = webControllerFacade()
    webFacadeMaria.goToAuthenticatedFacebookPage(email=config('MARIA_FB_EMAIL'),password=config('MARIA_FB_PASSWORD'))
    
    mariaDirectoryName = "./data/maria_" + str(datetime.datetime.now()) + "/"
    runSession(webFacadeMaria,outputDirectory=mariaDirectoryName)


    # Sleep for a bit before next session
    time.sleep(30)

    webFacadeJaime = webControllerFacade()
    webFacadeJaime.goToAuthenticatedFacebookPage(email=config('JAIME_FB_EMAIL'),password=config('JAIME_FB_PASSWORD'))

    jaimeDirectoryName = "./data/jaime_" + str(datetime.datetime.now()) + "/"    
    runSession(webFacadeJaime,outputDirectory=jaimeDirectoryName)
    

