from socket import *
from threading import *

from .get_target import *
from .connect_scan import *

def port_scan():
    target = get_target()
    target_host = target[0]
    target_ports = target[1]

    try:
        target_ip = gethostbyname(target_host)
    except:
        print('Unknown host {}'.format(target_host))

    try:
        target_name = gethostbyaddr(target_ip)
        print('[+] Scan results for: ' + target_name[0])
    except:
        print('[+] Scan results for: ' + target_ip)

    for target_port in target_ports:
        t = Thread(target=connect_scan, args=(target_ip, target_port))
        t.start()
