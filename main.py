# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# from scanning.port_scan import *

from sftp.get_target import *
# from sftp.ssh_login import *
# from sftp.ssh_command import *
from sftp.ssh_bruteforce import *

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
    host, user, _ = get_target()
    bruteforce(user, host)
