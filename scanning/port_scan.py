from socket import *
from threading import *
from get_target import *
from .return_banner import *


def port_scan():
    target = get_target()
    target_host = target[0]
    target_ports = target[1]

    try:
        target_ip = gethostbyname(target_host)
    except Exception:
        print('Unknown host {}'.format(target_host))

    try:
        target_name = gethostbyaddr(target_ip)
        print('[+] Scan results for: ' + target_name[0])
    except Exception:
        print('[+] Scan results for: ' + target_ip)
    
    for target_port in target_ports:
        t = Thread(target=return_banner, args=(target_ip, target_port))
        t.start()
