import pexpect
# logs into remote systems and runs hostname

PROMPT = ['# ', '>>> ', '> ', '\$ ']


def connect(user, host, password):
    child = pexpect.spawn('ssh ' + user + '@' + host)
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
    child.expect(PROMPT, timeout=1)

    return child