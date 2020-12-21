PROMPT = ['# ', '>>> ', '> ', '\$ ']


def send_command(child):
    command = input('Enter the commands and options to manage a remote host: ')
    child.sendline(command)
    child.expect(PROMPT)
    print(child.before.decode())
