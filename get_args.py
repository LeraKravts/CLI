import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--xpath', default='//*', help='a part of html page')
args = parser.parse_args()
print(args.xpath)

