import socket


def return_banner(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        sock.connect((host, int(port)))
        sock.settimeout(100)
        banner = sock.recv(1024)
        print('[+] {}/tcp open'.format(port))
        print(banner)
    except Exception:
        print('[+] {}/tcp closed'.format(port))
    finally:
        sock.close()
