import requests
import os
from colorama import Fore
import platform

system=platform.system()
login_name=os.getlogin()
cwd=os.getcwd()

if system =="Windows":
    try:
        os.chdir("C://Users//"+str(login_name)+"//Downloads//admin-finder")
    except:
        print("Please Copy The Admin wordlists To c://Users//"+str(login_name)+"//Downloads//admin-finder")

if system =="Linux":
    try:
        os.chdir(str(cwd))
    except:
        print("Please Copy The Admin Wordlists To /home/"+str(login_name)+"Downloads/admin-finder")

arr=[]
print(Fore.LIGHTMAGENTA_EX+"""
#############################################
#    ##        ##  #######    ##       ##   #
#    ####    ####  ##     ##   ##     ##    #
#    ##  ####  ##  ##     ##    ##   ##     #
#    ##   ##   ##  ########      ## ##      #
#    ##        ##  ##     ##      ###       #
#    ##        ##  ##     ##     ## ##      #
#    ##        ##  ##     ##    ##   ##     #
#    ##        ##  ##     ##   ##     ##    #
#    ##        ##  ##     ##  ##       ##   #
#############################################
""")
try:
    url=input(Fore.CYAN+"\nEnter The Web Site URL : ")

    for i in open("admin.txt","r"):
        j=i.strip("\n")  
        url1=str(url)+str(j)
        reponse=requests.get(url1) 
        if str(reponse) == "<Response [404]>":
            print(Fore.LIGHTRED_EX+"\n[-] Unable to find admin ==> "+str(url1)) 
        elif str(reponse) =="<Response [200]>":
            print(Fore.GREEN+"The Login Admin Page IS ==> "+str(url1))
            break
except:
    print(Fore.RED+" Error Pleasz Retray")
