from termcolor import colored
import hashlib
try:
    from utilities.file_check import *
except ImportError:
    import sys
    # add the submodules to $PATH
    # sys.path[0] is the current file's path
    sys.path.append(sys.path[0] + '/..')
    from utilities.file_check import file_check


def md5_bruteforce():
    md5_hash = input('[*] Enter MD5 Hash value: ')
    filepath = input('Enter the absolute path of a password list: ')
    password_list = file_check(filepath)
    print('password_list = ', password_list)

    for password in password_list.readlines():
        password = password.strip('\n')
        print(colored('[-] Trying: ' + password, 'red'))
        hashed = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
        if hashed == md5_hash:
            print(colored('[+] The password is: ' + str(password), 'green'))
            quit()

    print('Password not in the list')