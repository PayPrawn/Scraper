import os 
os.chdir("/Users/fin/Desktop/testfolder")
os.system("git clone https://github.com/PayPrawn/Scraper.git")
os.system("cd Scraper/")
#now in correct file with repository cloned
os.system("python3 ./opentunnel.py")