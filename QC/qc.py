#!/usr/bin/python
"""
Questionable Content webcomic scraper by gannon345. Takes user input to specify a range of comics and downloads
the images to store as .png files. Files are named after the strip number in the URL.
"""
# For personal use only. Feel free to modify or use for non-commercial purposes. Author claims no rights to the website
# 'questionablecontent.net', webpages therein, images, or or other information associated.
# questionablecontent.net and all information within is copyrighted by Jeff Jacques.


import urllib2
import os
from time import sleep
import re
from bs4 import BeautifulSoup


def try_url(url):
    """For testing if the URL is a valid page"""
    try:
        req = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        urllib2.urlopen(req)
        return True
    except urllib2.URLError:
        return False


def write_file(address_url, filename):
    """Writes the file from address_url to a file, as specified by the string passed to filename"""
    if os.name == 'nt':
        f = open("Questionable Content - " + filename + ".png", 'wb')
    else:
        f = open("Questionable Content - " + filename + ".png", 'w+')
    write_req = urllib2.Request(address_url, headers={'User-Agent': 'Mozilla/5.0'})
    site = urllib2.urlopen(write_req)
    f.write(site.read())
    f.close()


def comic_soup(url):
    """takes the url passed in, reads it, and uses BeautifulSoup to parse the HTML and find the portion of the HTML
    containing the end-path with the actual comic image. Returns that div to get_comics() as a string so it can be
    parsed with regex to pull the actual address value out of the string."""
    bs_req = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib2.urlopen(bs_req).read()
    soup = BeautifulSoup(html)
    comicbody = soup.find("div", id="comic")
    return str(comicbody)


def get_comics(low_val, high_val):
    """gets the comics between the value ranges specified in main. The loop creates the url path, specifies multiple
    possible urls based on potential filetype (GIF, PNG, JPG), and then runs a check to see which URL is valid. Uses
    regex to get the comic path from the soup string returned from comic_soup(url). To alter the path used, change the
    values in the soup.find() item in comic_soup.
    After determining valid URL, write_file is called to download the file to local path."""
    comic = low_val
    last_comic = high_val

    while comic <= last_comic:
        comic_str = str(comic)

        extensions = (".jpg", ".gif", ".png")

        for ext in extensions:
            url = "http://www.questionablecontent.net/view.php?comic=" + comic_str
            url_check = try_url(url)

            if url_check:
                comicbody_text = comic_soup(url)

                image_location = re.compile('/comics/.+'+ext)
                image_link = re.search(image_location, comicbody_text)

                if image_link:
                    image_link_str = "http://questionablecontent.net/" + image_link.group()
                    print "Comic found. Writing comic #" + comic_str
                    write_file(image_link_str, comic_str)
                    sleep(2)
                    break

                else:
                    print "No match for comic %d on format %s" % (comic, ext)
                    print image_location
                    print image_link

            else:
                print "no comic found for format: %s on comic string %s" % (ext, comic_str)

        comic += 1


def main():
    comic_low = raw_input("\nEnter the first comic to download by number (1, 5, 75, etc.): ")
    comic_high = raw_input("Enter the last comic to download by number (10, 50, 1000, etc.): ")
    print "\n"

    try:
        if int(comic_low) <= int(comic_high):
            get_comics(int(comic_low), int(comic_high))
        else:
            print "invalid input\n\n"
    except ValueError:
        print "Input must be an integer value. "


if __name__ == '__main__':
    main()
