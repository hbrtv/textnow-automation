from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import sys
import urllib
import requests
from reCaptch import runCaptcha

def waitPage(pDriver, pId, pTimeout=10):
    element_present = EC.presence_of_element_located((By.ID, pId))
    WebDriverWait(pDriver, pTimeout).until(element_present)
# THE FILE CONTAINS THE PARAMS WILL LOOK LIKE THIS
# FIRST LINE : FUNCTION EX : goto-autoresponder
# SECOND LINE : EMAIL FOR GOTOWEBINAR
# THIRD LINE : PASSWORD FOR GOTOWEBINAR
# NEXT LINES WILL BE PROVIDED IN EACH FUNCTION BLOCK
#Decode Sample
#sampleURL = "Registration%20Body%0AThis%20is%20next%20line"
##print urllib.unquote(sampleURL).decode('utf8')
#print "This is the name of the script: ", sys.argv[0]
#print "Number of arguments: ", len(sys.argv)
#print "The arguments are: " , str(sys.argv)
# if len(sys.argv) < 2:
# 	#print "Arguments are not provided"
# 	exit()
# filepath = sys.argv[1]
# with open(filepath, 'r') as theFile:
#     # Return a list of lines (strings)
#     data = theFile.read().split('\n')
#     theFile.close()
# #print data
# function = data[0]
# email = data[1]
# password = data[2]
# webinarID = data[3]
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(chrome_options=chrome_options)

chrome_driver = "chromedriver"
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary
#options.add_argument("--kiosk") #Full Screen

temp_driver = webdriver.Chrome(chrome_driver)
temp_driver.get("https://temp-mail.org/en/")

actionChains = ActionChains(temp_driver)

#Temp Email address.
tempEmail = temp_driver.execute_script("return document.getElementById('mail').value;")
print (tempEmail)

result = runCaptcha(tempEmail)

print (result)

defaultPwd = "Password12345now"

filepath = "./initalParam.txt"

with open(filepath, 'a+') as theFile:
    # Return a list of lines (strings)
    theFile.write("%s, %s\r\n" % (tempEmail, defaultPwd) )
    theFile.close()


