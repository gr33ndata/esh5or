from argparse import ArgumentParser
from esh5or.sha5ra import sha5ra

def parse_cli():

    parser = ArgumentParser(description='esh5or')
    parser.add_argument(
        '-l', '--length', 
        nargs='?', default=10, const=10, 
        metavar='Length of the sha5ra',
        help='Specify how long you want your sha5ra to be'
    )

    return parser.parse_args()

def main(args):

    l = int(args.length)
    print sha5ra(l)


if __name__ == '__main__':

    args = parse_cli()
    main(args)