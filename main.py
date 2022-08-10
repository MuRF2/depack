import tarfile
import argparse


version_number = '0.1'


def arguments():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h', '--help',
                        action='help',
                        default=argparse.SUPPRESS,
                        help='depack is an easy to use unpack tool.')
    parser.add_argument('-v', '--version',
                        action='version',
                        default=argparse.SUPPRESS,
                        version="Version {} is installed.".format(version_number),
                        help='show version number')
    parser.add_argument('-f', '--file',
                        type=str,
                        nargs=1,
                        help="file path")
    parser.add_argument('-d', '--destination',
                        type=str,
                        nargs=1,
                        help="destination")
    parser.add_argument("main_operator",
                        type=str,
                        choices=["unpack"],
                        help="main operator to be selected")
    return parser.parse_args()


def extract(s_path, d_path):
    try:
        with tarfile.open(s_path) as file:
            file.extractall(d_path)
    except FileNotFoundError:
        print('File not found')


if __name__ == '__main__':
    if arguments().main_operator == 'unpack':
        try:
            extract(arguments().file.pop(), arguments().destination.pop())
        except AttributeError:
            pass




