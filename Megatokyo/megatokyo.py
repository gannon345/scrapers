#!/usr/bin/python
"""
Megatokyo webcomic scraper by /u/tomkatt. Takes user input to specify a range of comics and downloads
the images to store as .png files. Files are named after the strip number in the URL.
"""
# For personal use only. Feel free to modify or use for non-commercial purposes.
# Author claims no rights to the website 'megatokyo.com', webpages therein, images, or or other information associated.
#
# Megatokyo.com and all information within is copyrighted by Fred Gallagher. The Megatokyo name is trademarked
# by Fred Gallagher.


import urllib2
import os


def try_url(url):
    """For testing if the URL is a valid page"""
    try:
        urllib2.urlopen(url)
        return True
    except urllib2.URLError:
        return False


def write_file(address_url, filename):
    """Writes the file from address_url to a file, as specified by the string passed to filename"""
    if os.name == 'nt':
        f = open("Megatokyo - " + filename, 'wb')
    else:
        f = open("Megatokyo - " + filename, 'w+')
    site = urllib2.urlopen(address_url)
    f.write(site.read())
    f.close()


def get_comics(low_val, high_val):
    """gets the comics between the value ranges specified in main. The loop creates the url path, specifies multiple
    possible urls based on potential filetype (GIF, PNG, JPG), and then runs a check to see which URL is valid.
    After determining valid URL, write_file is called to download the file to local path."""
    comic = low_val
    last_comic = high_val

    while comic <= last_comic:
        comic_str = ""

        if comic <= 9:
            comic_str = "000" + str(comic)
        if comic >= 10 and comic <= 99:
            comic_str = "00" + str(comic)
        if comic >= 100 and comic <= 999:
            comic_str = "0" + str(comic)
        if comic >= 1000:
            comic_str = str(comic)

        url = "http://megatokyo.com/strips/" + comic_str + ".gif"
        url2 = "http://megatokyo.com/strips/" + comic_str + ".png"
        url3 = "http://megatokyo.com/strips/" + comic_str + ".jpg"
        url_check = try_url(url)
        url_check2 = try_url(url2)
        url_check3 = try_url(url3)

        if url_check:
            print "GIF found. Writing comic #" + comic_str
            comic_str = comic_str + ".gif"
            write_file(url, comic_str)

        elif url_check2:
            print "PNG found. Writing comic #" + comic_str
            comic_str = comic_str + ".png"
            write_file(url2, comic_str)

        elif url_check3:
            print "JPG found. Writing comic #" + comic_str
            comic_str = comic_str + ".jpg"
            write_file(url3, comic_str)

        else:
            print "no comic found."

        comic += 1


def main():
    comic_low = raw_input("\nEnter the first comic to download by number (1, 5, 75, etc.): ")
    comic_high = raw_input("Enter the last comic to download by number (10, 50, 1000, etc.): ")
    print "\n"

    try:
        if int(comic_low) < int(comic_high):
            get_comics(int(comic_low), int(comic_high))
        else:
            print "invalid input\n\n"
    except:
        print "Input must be an integer value. "


if __name__ == '__main__':
    main()

