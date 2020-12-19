import socket


def connect_scan(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.settimeout(100)
        print('[+] {}/tcp open'.format(port))
    except:
        print('[+] {}/tcp closed'.format(port))
    finally:
        sock.close()
