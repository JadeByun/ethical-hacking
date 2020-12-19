import socket

def return_banner(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.settimeout(100)
        banner = sock.recv(1024)
        print('[+] {}/tcp open'.format(port))
        return banner
    except:
        print('[+] {}/tcp closed'.format(port))
    finally:
        sock.close()
