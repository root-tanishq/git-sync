#!/usr/bin/env python3
import os 
import sys
# Colors 
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
banner = '''
░██████╗░██╗████████╗░░░░░░░██████╗██╗░░░██╗███╗░░██╗░█████╗░███████╗██████╗░
██╔════╝░██║╚══██╔══╝░░░░░░██╔════╝╚██╗░██╔╝████╗░██║██╔══██╗██╔════╝██╔══██╗
██║░░██╗░██║░░░██║░░░█████╗╚█████╗░░╚████╔╝░██╔██╗██║██║░░╚═╝█████╗░░██████╔╝
██║░░╚██╗██║░░░██║░░░╚════╝░╚═══██╗░░╚██╔╝░░██║╚████║██║░░██╗██╔══╝░░██╔══██╗
╚██████╔╝██║░░░██║░░░░░░░░░██████╔╝░░░██║░░░██║░╚███║╚█████╔╝███████╗██║░░██║
░╚═════╝░╚═╝░░░╚═╝░░░░░░░░░╚═════╝░░░░╚═╝░░░╚═╝░░╚══╝░╚════╝░╚══════╝╚═╝░░╚═╝
'''
print(banner)
print(f'{bcolors.WARNING}[!]{bcolors.ENDC} This Configuration will only work for Current User')
#Taking Credentials
os.system('git config --global credential.helper store')
location = input(f'{bcolors.OKCYAN}[?]{bcolors.ENDC} Please provide the folder location where to put the repo: ')
repo_link = input(f'{bcolors.OKCYAN}[?]{bcolors.ENDC} Please provide the link of the repo[if not created please create one]: ')
repo_name = input(f'{bcolors.OKCYAN}[?]{bcolors.ENDC} Please provide the repo name: ')
print(f'{bcolors.OKCYAN}[?] {bcolors.ENDC}Please provide git username and API key as password: ')
os.system(f'cd {location} ; git clone {repo_link}')
#Creating a custom command for ease
command = f'''
#!/bin/bash
cd {location}/{repo_name}/
'''
command += '''
#git config --global credential.helper store
#git pull
gstatus=`git status --porcelain`
if [ ${#gstatus} -ne 0 ]
then
    echo -e "\033[0;33m[!]\e[0m unsynced files found"
    echo -e "\n"
    git add --all 1>/dev/null
    git commit -m "`date`" 1>/dev/null
    git push 1>/dev/null
    echo -e "\n"
    echo -e "\033[0;32m[+]\e[0m synced all files"
else
    echo -e "\033[0;32m[+]\e[0m all files are already synced"
fi
'''
print(f'{bcolors.OKGREEN}[+]{bcolors.ENDC} Creating A Custom Command For Ease')
command_name = input(f'{bcolors.OKCYAN}[?]{bcolors.ENDC} Please provide the command name: ')
file = open(f"/usr/local/bin/{command_name}" , "w")
file.write(command)
file.close()
os.system(f'chmod +x /usr/local/bin/{command_name}')

