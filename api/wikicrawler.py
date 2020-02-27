#!/usr/bin/env python

import sys
import requests
import wikipedia
from urllib.parse import urljoin

def extract_links(url):
    page = wikipedia.page(url)
    links = []

    for link in page.links:
        links.append({"page":link})
    
    # print(page.links[0])
    # for link in links:
    #     print link

    return links

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\nUsage:\n\t{} <Search Word>\n".format(sys.argv[0]))
        sys.exit(1)
    for link in extract_links(sys.argv[-1]):
        print("[{}]".format(link["page"]))
