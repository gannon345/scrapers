# -*- coding: iso-8859-1 -*-

from urllib import urlopen
from bs4 import BeautifulSoup
import re
import worm_cleanup


url = "http://parahumans.wordpress.com/category/stories-arcs-1-10/arc-1-gestation/1-01/"

f = open('wormtest.html', 'w')
f.seek(0)
f.write("Worm, by Wildbow\n\n\n")

while True:

    html = urlopen(url).read()
    soup = BeautifulSoup(html)
    title = soup.find("h1", class_="entry-title")
    text = soup.find("div", class_="entry-content")
    print title.get_text()

    next_chapter = soup.find_all("a", text=re.compile('.*Next.Chapter.*'))

    str_title = str(title)
    str_text = str(text)

    f.write("\n\n\n")
    f.write(str_title)
    f.write("\n\n")
    f.write(str_text)
    f.write("\n\n\n\n")


    if len(str(next_chapter)) > 0:
        url = next_chapter[0]['href'].encode('utf-8)')
        print "Next chapter is:", url

    else:
        print "End of file. All tasks completed."
        f.close()
        break