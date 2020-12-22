# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# from scanning.port_scan import *

from get_target import *
#from ssh.ssh_login import *
#from ssh.ssh_command import *
#from ssh.ssh_bruteforce import *
#from ftp.anonymous_login import *
from ftp.ftp_bruteforce import *

if __name__ == '__main__':
    # 1. scan open ports
    # port_scan()

    # 2. SSH login and send command
    # host = '192.168.1.78'
    # user = 'msfadmin'
    # password = 'msfadmin'
    # host, user, password = get_target()
    # child = connect(user, host, password)
    # print(send_command(child))

    # 3. SSH Brute-Force attack
    #host, _, user, _ = get_target()
    #print(host, user)
    #ssh_bruteforce(user, host)

    # 4. Anonymous FTP Login
    # host, _, _, _ = get_target()
    # anonymous_login(host)

    # 5. FTP Brute-Force attack
    host, _, _, _ = get_target()
    ftp_bruteforce(host)
