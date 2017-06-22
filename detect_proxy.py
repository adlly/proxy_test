#-*- coding: UTF-8 -*-
import urllib2

url = 'http://www.ip181.com/'
proxy_support = urllib2.ProxyHandler({'http': '121.40.108.76'})
opener = urllib2.build_opener(proxy_support)
opener.add_handler = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36')]
urllib2.install_opener(opener)
response = urllib2.urlopen(url)
print response.read().decode('gbk')