import ftplib

def anonymous_login(host):
    try:
        ftp = ftplib.FRP(host)
        ftp.login('anonymous', 'anonymous')
        print('[*] ' + host + ' FTP anonymous login succeeded.')
        ftp.quit()
        return True
    except Exception:
        print('[-] ' + host + ' FTP anonymous login failed.')
