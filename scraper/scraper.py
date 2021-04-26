# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 10:44:54 2021

@author: Phantom
"""
import urllib.request
import lxml
from bs4 import BeautifulSoup
from multiprocessing import Pool

def scrape(url, tag="a", tag_class="ProjectCoverNeue-coverLink-102"):
    if url.startswith("https://www.behance.net/gallery"):
        tag = "img"
        tag_class = "ImageElement-image-2K6"

    search_page = urllib.request.urlopen(url, timeout=10)

    soup = BeautifulSoup(search_page, 'lxml')

    search_results = soup.find_all(tag, {"class":tag_class})

    href_list = []
    for img in search_results:
        src = img.get('src')
        href = img.get('href')

        if src:
            return src
        if href:
            print(href)
            href_list.append(href)

    src_list = []
    with Pool(6) as p:
        images = list(p.map(scrape, href_list))
        src_list+=images
    
    return src_list

if __name__ == '__main__':
    i = scrape("https://www.behance.net/gallery/117693203/Brochure-Design")
    print(i)


