import urllib.request
import http.cookiejar
cookie=http.cookiejar.CookieJar()
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('http://www.douban.com')
for item in cookie:
	print('Name='+item.name)
	print('Value='+item.value)
