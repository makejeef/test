#conding:utf-8
import urllib.request,re

def getpage(url):
	try:
		request=urllib.request.Request(url)
		response=urllib.request.urlopen(request)
		return response.read().decode('utf-8')
	except urllib.request.URLError as e:
		if hasattr(e,'reason'):
			print(u'连接失败原因：'e.reason)
			return None

def get_pagenum(url):
	response=getpage(url)
	pattern=re.compile('data-total-page="(\d)"')
	m=re.findall(pattern,response)
	num=int(m[0])
	return num
	print(num)


if __name__=='__main__':
	url=input('plz type this album url:')
	get_pagenum(url)

