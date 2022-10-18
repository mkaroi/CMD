
from calendar import c
import sys
import time
import a
current_time = time.localtime()
import time
print("RUNTIME",current_time.tm_hour,":",current_time.tm_min,":",current_time.tm_sec)
print("cmd2.6")
print("Importing lib...")
time.sleep(0)
print("Loading script....")
time.sleep(0)
print("Finishing.....")
time.sleep(0)
n=input("name: ")
i=input("%cmd%/bin/>> ")
maid = "Ud"
math = "dd"
jj = 44

while(jj == 44):
    if i == "load main":
        maid = "use"
        print("func loaded")
        i = None 
        i = input("%cmd%/bin/>> ")
    elif i == "load math":
        math = "use"
        print("func loaded")
        i = None 
        i = input("%cmd%/bin/>> ")
    elif i == "main.hello":
        if maid == "use":
            print("Hello", n)
            i = None 
            i = input("%cmd%/bin/>> ")
        else:
            print("No main func loaded Run *load main* to load")
            i = None
            i = input("%cmd%/bin/>> ")
    elif i == "math.tri":
        if math == "use":
            a.tri()
            i = None 
            i = input("%cmd%/bin/>> ")
        else:
            print("No math func loaded Run *load math* to load")
            i = None
            i = input("%cmd%/bin/>> ")
    elif i == "math.rec":
        if math == "use":
            a.rec()
            i = None 
            i = input("%cmd%/bin/>> ")
        else:
            print("No math func loaded Run *load math* to load")
            i = None
            i = input("%cmd%/bin/>> ")
    elif i == "math.cir":
        if math == "use":
            a.cir()
            i = None 
            i = input("%cmd%/bin/>> ")
        else:
            print("No math func loaded Run *load math* to load")
            i = None
            i = input("%cmd%/bin/>> ")
    elif i == "math.sqr":
        if math == "use":
            a.sqr()
            i = None 
            i = input("%cmd%/bin/>> ")
        else:
            print("No math func loaded Run *load math* to load")
            i = None
            i = input("%cmd%/bin/>> ")
    elif i == "exit":
        i = None 
        current_time = time.localtime()
        print("ENDTIME",current_time.tm_hour,":",current_time.tm_min,":",current_time.tm_sec)
        print("END")
        sys.exit()
    else:
        i = None 
        print("Invalid command")
        i = input("%cmd%/bin/>> ")
