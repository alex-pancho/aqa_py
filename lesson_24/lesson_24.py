import requests
import lxml.html
from lxml.html import fromstring, fragment_fromstring
from lxml import etree
from io import StringIO

# # отримати вміст
# r = requests.get('https://www.babyshop.com')
# # перетвоюємо його в зрозуміле дерево через lxml
# tree = fromstring(r.content)
# # добуваємо дані по xpath
# mainmenu = tree.xpath('//*[@class="text-base babyshop:font-bold md:text-lg"]/text()')
# # дивимся, що вийшло
# print(mainmenu)

broken_html = """<html><head>
<title>test<body><h1>page title</h3>
<a rel='my@mail.com'>click me</a>
<p class='abc' > some text
<div id="xyz"> text </div>
""" # неевірний покоцаний хтмл
parser = etree.HTMLParser()  # наслідуєм клас хтмл парсер
tree = etree.parse(StringIO(broken_html), parser)  # перетворюєм в зрозумілу структуру
result = etree.tostring(tree.getroot(),
    pretty_print=True, method="html")  # звороне перетворення - обєкт дерева у строку
print(result)

# string = "<title>test  <br> page"  # поправити кусок хтмл
# result = fragment_fromstring(string, create_parent='div')
# print(etree.tostring(result))
#result2 = requests.get('https://www.babyshop.com').content
tree = lxml.html.fromstring(result)
result = tree.find_class("abc")
print(result[0].attrib, result[0].text)

result2 = tree.find_rel_links("my@mail.com")
print(result2[0].attrib, result2[0].text)

result3 = tree.get_element_by_id("xyz")
print(result3.attrib, result3.text)
# comment
