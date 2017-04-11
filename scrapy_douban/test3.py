# -*- coding:utf-8 _*_

import urllib,urllib.request,re

user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
headers={'User_Agent':user_agent}

page=0
for page in range(0,271,18):
	url='https://www.douban.com/photos/album/1622832404/?start='+str(page)
	try:
		request=urllib.request.Request(url,headers=headers)
		response=urllib.request.urlopen(request)
		content=response.read().decode('utf-8')
		pattern=re.compile('<img width="\d*" src="(.*)"')
		items=re.findall(pattern,content)
		#print(items)
		for item in items:
			print(item)
			urllib.request.urlretrieve(item)
	except urllib.request.URLError as e:
		if hasattr(e,'code'):
			print(e.code)
		if hasattr(e,'reason'):
			print(e.reason)

	
	
