import requests
from lxml import html
from html_doc import text
from ctiparser import cti_parser


path = str.encode(cti_parser())
response = text
source_code = html.fromstring(text)
tree = source_code.xpath(path)
print(tree[0].text_content())