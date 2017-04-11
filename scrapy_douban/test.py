import urllib.request
import urllib.parse
values={}
values['username']='makejeef@126.com'
values['password']='7400233jeffla'
data=urllib.parse.urlencode(values)
url='https://www.douban.com/accounts/login?source=main'
geturl=url+'?'+data
request=urllib.request.Request(geturl)
response=urllib.request.urlopen(request)
print(response.read())
