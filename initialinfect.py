import os 
from time import sleep
os.chdir("/Users/fin/Desktop/testfolder")
os.system("git clone https://github.com/PayPrawn/Scraper.git")
os.chdir("Scraper/")
#now in correct file with repository cloned
os.system("python3 ./opentunnel.py")