import argparse


def cti_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--xpath', default='//*', help='a part of html page')
    args = parser.parse_args()
    return args


print(cti_parser())

