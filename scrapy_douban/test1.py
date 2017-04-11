import urllib.request
import http.cookiejar
import urllib

filename='cookie.txt'
url='https://accounts.douban.com/login?alias=&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1001'
cookie=http.cookiejar.MozillaCookieJar(filename)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
postdata=urllib.parse.urlencode({
							'username':'makejeef@126.com',
							'password':'7400233jefflA'
							}).encode('UTF-8')
result=opener.open(url,postdata)
cookie.save(ignore_discard=True,ignore_expires=True)
gradeurl='https://www.douban.com/doulist/43888106/'
result=opener.open(gradeurl)
print(result.read())
