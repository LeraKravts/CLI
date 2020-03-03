import argparse

from lxml import html


def cli_parser(document: str):
    parser = argparse.ArgumentParser()
    parser.add_argument('--xpath', default='//*', help='a part of html page')
    args = parser.parse_args()
   
    source_code = html.fromstring(document)
    tree = source_code.xpath(args.xpath)
    
    return print(tree[0].text_content())