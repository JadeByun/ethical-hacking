import socket


def connect_scan(target_host, target_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_host, target_port))
        print('[+] {}/tcp open'.format(target_port))
    except:
        print('[+] {}/tcp closed'.format(target_port))
    finally:
        sock.close()