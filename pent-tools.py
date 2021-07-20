import os
from colorama import init,Fore, Back, Style
init()
logo = """"



______ _____ _   _ _____    _____ _____  _____ _      _____ 
| ___ \  ___| \ | |_   _|  |_   _|  _  ||  _  | |    /  ___|/
| |_/ / |__ |  \| | | |______| | | | | || | | | |    \ `--. 
|  __/|  __|| . ` | | |______| | | | | || | | | |     `--. \/
| |   | |___| |\  | | |      | | \ \_/ /\ \_/ / |____/\__/ //
\_|   \____/\_| \_/ \_/      \_/  \___/  \___/\_____/\____// 
@rafa_ailes                                                            
"""
print(Fore.GREEN  + logo)

print(Fore.GREEN  + "[1]web scanning with nikto: ")
print(Fore.GREEN  + "[2]vulnerability scanning with nmap: ")
print(Fore.GREEN  + "[3]BruteFroce website with gobuster: ")
choix = input("choose an options: ")
if choix == "1":
    url = input("enter url of your web site: ")
    os.system("nikto -h " +url)
    sql = input("do you want start an sql attaque with sqlmap[y/n]: ")
    if sql == "y":
        os.system("sqlmap -u " +url)
if choix == "2":
    ip = input("enter target ip address: ")
    os.system("nmap -sV " +ip)
    msf1 = input("do you want search an exploit of your scanning[y/n]: ")
        
    if msf1 == "y":
        install = input("if you d'ont have searchsploit you do try install: ")
        exploit = input("enter a vulnerability of your scan: ")
        os.system("searchsploit " +exploit)
    
if choix == "3":
    url2 = input("enter target url: ")
    path = input("enter path of your wordlist example:(/usr/share/wordlists/dirb/big.txt): ")
    os.system("gobuster dir -u " +url2 +" -w " +path)


  
