import argparse
from html import text
from lxml import html


def cli_parser(document: str):
    parser = argparse.ArgumentParser()
    parser.add_argument('--xpath', default='//*', help='a part of html page')
    args = parser.parse_args()
    
    try:
        source_code = html.fromstring(document)
        tree = source_code.xpath(args.xpath)
        return tree[0].text_content()
    except IndexError:
        print('IndexError')
        
print(cli_parser(text))     
        
        

