from lxml import html
import requests

page = requests.get('http://www.google.com/finance?q=f&ei=N4U9VIivJ4ebrAHP6oDYDQ')
tree = html.fromstring(page.text)

info = tree.xpath('//td[@class="val"]/text()')


print 'Info: ', info

