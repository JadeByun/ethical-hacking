import argparse
import getpass


class Password(argparse.Action):

    def __call__(self, parser, namespace, values, option_string):
        if values is None:
            values = getpass.getpass()

        setattr(namespace, self.dest, values)


def get_target():
    parser = argparse.ArgumentParser(description='Usage of program: ' + '-H <SSH host> -u <SSH user> -p <SSH password>')
    parser.add_argument('-H', dest='host', required=True, help='specify SSH host')
    parser.add_argument('-u', dest='user', help='specify SSH user')
    parser.add_argument('-p', action=Password, dest='password', help='enter a SSH password')

    args = parser.parse_args()
    host = args.host
    user = args.user
    password = args.password

    if host is None or user is None or password is None:
        print(parser.usage)
        exit(0)

    return host, user, password
