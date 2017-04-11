import http.cookiejar
import urllib.request
cookie=http.cookiejar.MozillaCookieJar()
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
req=urllib.request.Request('https://douban.com')
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
response=opener.open(req)
print(response.read())
