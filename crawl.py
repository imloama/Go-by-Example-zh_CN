# -*- coding: utf-8 -*-
"""
    crawl.py
    ~~~~~~~~~~~~~
    
    :author: G_will <g_will@ieqi.com> 
"""

import urllib2
import re
import time

def crawl():
    site_url = 'https://gobyexample.com/'
    
    page_url_patten = re.compile(r'<li><a href="(.*)">.*</a></li>')
    site_index_str = urllib2.urlopen(site_url).read()
    page_url_list = re.findall(page_url_patten, site_index_str)
    
    for page_url_suffix in page_url_list:
        time.sleep(5)
        print '----> Crawl', page_url_suffix
        page_url = site_url + page_url_suffix
        page_str = urllib2.urlopen(page_url).read()
        with open(page_url_suffix+'.html', 'w') as f:
            f.write(page_str)
            
if __name__ == '__main__':
    crawl()
