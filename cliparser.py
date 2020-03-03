from lxml import html
from html import text
import argparse


def cli_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--xpath', default='//*', help='a part of html page')
    args = parser.parse_args()
    path = args.xpath

    source_code = html.fromstring(text)
    tree = source_code.xpath(path)
    return print(tree[0].text_content())
