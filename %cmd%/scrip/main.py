
from calendar import c
import subprocess
import sys
import time
import logging
import os
import afd
current_time = time.localtime()
import time
import webbrowser as wb
print("RUNTIME",current_time.tm_hour,":",current_time.tm_min,":",current_time.tm_sec)
print("cmd-1.1.4")
time.sleep(0.4)
print("debug.s")
os.system('cls')
print("importing 9 package{/calendar/supprocess/time/sys/loging/os/afd/}")
time.sleep(5.5)
os.system('cls')
print("Loading script...")
time.sleep(2)
os.system('cls')
print("Finishing...")
time.sleep(2)
os.system('cls')
print("RUNTIME",current_time.tm_hour,":",current_time.tm_min,":",current_time.tm_sec)
print("cmd-1.1.4")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("runlog.log", mode='a'),
    ]
)
logging.info('start')
n=input("name: ")
logging.info('name registed as var n')
i=input("%cmd%/scrip/main.py>> ")
jj = 44
while(jj == 44):


    if i == "hello":
        afd.hey(n)
        logging.info('hello')
        i = None 
        i = input("%cmd%/scrip/main.py>> ")
    elif i == "none":
        i = None 
        logging.info('none')
        i = input("%cmd%/scrip/main.py>> ")
    elif i == "notepad":
        i = None 
        afd.notepad()
        logging.info('npad')
        i = input("%cmd%/scrip/main.py>> ")
    elif i == "openexe":
        i = None 
        logging.info('openerexe')
        ij=input("Enter directory (with file name) : ")
        logging.info('reg dir')
        subprocess.Popen(ij)
        ij = None
        i = input("%cmd%/scrip/main.py>> ")
    elif i == "PRANK2":
        i = None 
        logging.info('notrickroll')
        wb.open('https://www.youtube.com/watch?v=x9aNNZY2lrY')
        i = input("%cmd%/scrip/main.py>> ")
    elif i == "secret":
        i = None 
        logging.info('subto')
        
        wb.open('https://www.youtube.com/channel/UCU5CZoYO0jNgrqTXYrhctrw')
        i = input("%cmd%/scrip/main.py>> ")
    elif i == "virusim":
        i = None 
        logging.warning('virus')
        time.sleep(2)
        print("---------------installer---------------------------")
        print("install virus.pyc 100%")
        print("---------------------------------------------------")
        time.sleep(1)
        print("Detetor have detec file 'VIRC4' and found virus")
        time.sleep(3)
        print("can't delete virus")
        time.sleep(3)
        print()
        print("------------Error-report-------------")
        print("The program ran into the problem. ")
        print("We will check a problem and end ")
        print("program for you.")
        print("STOPCODE 'VIRUS_DET_CAN_DELV_ERR551 '")
        print("ERRORTIME",current_time.tm_hour,":",current_time.tm_min,":",current_time.tm_sec)
        print("-------------------------------------")
        print("END")
        logging.error('virus simulator is ate a program')
        logging.info('ended')
        sys.exit()
    elif i == "url":
        i = None 
        logging.info('url opener')
        urltj = input("enter url: ")
        logging.info('url recorded')
        wb.open(urltj)
        urltj = None
        i = input("%cmd%/scrip/main.py>> ")
    elif i == "malwaresim":
        i = None 
        time.sleep(4)
        logging.warning('malware runned')
        print("---------------installer---------------------------")
        print("install malvajava.pyc 100%")
        print("---------------------------------------------------")
        time.sleep(1)
        print("Detetor have detec file 'malvagoodserv450' and found  malware")
        time.sleep(3)
        print("can't delete malware")
        time.sleep(3)
        print()
        print("------------Error-report-------------")
        print("The program ran into the problem. ")
        print("We will check a problem and end ")
        print("program for you.")
        print("STOPCODE 'VIRUS_DET_CAN_DELV_ERR551 '")
        print("ERRORTIME",current_time.tm_hour,":",current_time.tm_min,":",current_time.tm_sec)
        print("-------------------------------------")
        print("END")
        logging.error('malware ate a program')
        logging.info('ended')
        sys.exit()
    elif i == "endses":
        i = None 
        print("ENDTIME",current_time.tm_hour,":",current_time.tm_min,":",current_time.tm_sec)
        print("END")
        logging.info('ended')
        
        sys.exit()
    elif i == "PRANK":
        wb.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        i = None 
        logging.info('desert you')
        i = input("%cmd%/scrip/main.py>> ")
    elif i == "reload":
        i = None 
        n = None
        logging.info('reload')
        time.sleep(6)
        print("restart complete!")
        time.sleep(0.5)
        os.system('cls')
        n = input("name: ")  
        logging.info('name registed as var n')     
        i = input("%cmd%/scrip/main.py>> ")
    elif i == "info":
        i = None 
        print("Create 2-10-2021")
        print("Made in thailand")
        print("Made with python")
        logging.info('info')
        i = input("%cmd%/scrip/main.py>> ")
    else:
        i = None 
        print("Invalid command")
        logging.info('invalid synstax')
        i = input("%cmd%/scrip/main.py>> ")



