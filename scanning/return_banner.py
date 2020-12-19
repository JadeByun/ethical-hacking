import socket


def return_banner(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        sock.connect((host, int(port)))
        sock.settimeout(100)
        banner = sock.recv(1024)
<<<<<<< HEAD
        print(f'[+] {host}/{port}: {banner}')
    except:
=======
        print('[+] {}/tcp open'.format(port))
        print(banner)
    except Exception:
>>>>>>> a48c94d650a3b4821857a0686335261c453e27b9
        print('[+] {}/tcp closed'.format(port))
    finally:
        sock.close()
