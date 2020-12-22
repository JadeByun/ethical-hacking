import argparse


def get_target():
    parser = argparse.ArgumentParser(description='Usage of program: ' + '-H <target host> -p <target port> -u <target user> -P <target password>')
    parser.add_argument('-H', dest='host', required=True, help='specify target host')
    parser.add_argument('-p', dest='port', nargs='*', help='specify target ports separated by space')
    parser.add_argument('-u', dest='user', help='specify target user')
    parser.add_argument('-P', dest='password', help='enter a target password')

    args = parser.parse_args()
    host = args.host
    ports = args.port
    user = args.user
    password = args.password

    if host is None:
        print(parser.usage)
        exit(0)

    return host, ports, user, password
