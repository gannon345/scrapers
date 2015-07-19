# coding: utf-8

from urllib import urlopen
from bs4 import BeautifulSoup
import worm_cleanup

url = "http://parahumans.wordpress.com/category/stories-arcs-1-10/arc-1-gestation/1-01/"

f = open('wormtest.html', 'w')
f.seek(0)
f.write("Worm, by Wildbow\n\n\n")

html = urlopen(url).read()
soup = BeautifulSoup(html)
title = soup.find("h1", class_="entry-title")
text = soup.find("div", class_="entry-content")

str_title = str(title)
str_text = str(text)

f.write("\n\n\n")
f.write(str_title)
f.write("\n\n")
f.write(str_text)
f.write("\n\n\n\n")
f.close()
worm_cleanup.cleanup()


