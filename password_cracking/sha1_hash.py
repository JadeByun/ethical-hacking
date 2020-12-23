from urllib.request import urlopen
import hashlib
from termcolor import colored


sha1_hash = input('[*] Enter Sha1 Hash value: ')
password_list = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

for password in password_list.split('\n'):
    hashed = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
    if hashed == sha1_hash:
        print(colored('[+] The password is: ' + str(password), 'green'))
        quit()
    else:
        print(colored('[-] Password ' + str(password) + ' does not match, trying next...', 'red'))

print('Password not in the password list')