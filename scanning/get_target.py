import argparse


def get_target():
    parser = argparse.ArgumentParser(description='Usage of program: ' + '-H <target host> -p <target port>')
    parser.add_argument('-H', dest='targetHost', required=True, help='specify target host')
    parser.add_argument('-p', dest='targetPort', nargs='*', help='specify target ports separated by space')

    args = parser.parse_args()
    target_host = args.targetHost
    target_ports = args.targetPort
    if target_host is None or target_ports[0] is None:
        print(parser.usage)
        exit(0)

    return target_host, target_ports
