from lxml import html
import requests

page = requests.get('http://www.google.com/finance?q=f&ei=N4U9VIivJ4ebrAHP6oDYDQ')
tree = html.fromstring(page.text)
info = tree.xpath('//td[@class="val"]/text()')
labels = ["Range",
          "52 week",
          "Open",
          "Vol / Avg.",
          "Mkt cap",
          "P/E",
          "Div/yield",
          "EPS",
          "Shares",
          "Beta",
          "Inst. own"]

dictionary = dict(zip(labels, info))

print float(dictionary["Beta"]) * float( dictionary["Range"][0:dictionary["Range"].index(" ")] )