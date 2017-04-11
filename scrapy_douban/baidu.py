# _*_ coding:utf-8 _*_
import urllib,urllib.request,re

user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
headers={'User_Agent':user_agent}

class Baidu:
	def __init__(self,baseURL,seeLZ):
		self.baseURL=baseURL
		self.seeLZ='?seeLZ'+str(seeLZ)

	def getPage(self,pageNum):
		try:
			url=self.baseURL+self.seeLZ+'&pn'+str(pageNum)
			request=urllib.request.Request(url)
			response=urllib.request.urlopen(request)
			print(response.read())
			return response
		except urllib.request.URLError:
			if hasattr(e,'reason'):
				print(u'error',e.reason)
				return None
			
	def getTitle(self):
		page=self.getTitle(1)
		pattern=re.compile('<h1 class="core_title_text.*?>(.*?)</h1>',re.S)
		result=re.search(pattern,page)
		if request:
			return result.group(1).strip()
		else:
			return None
			
	def getPageNum(self):
		pattern=re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
		result=re.search(pattern,page)
		if result:
			return result.group(1).strip()
		else:
			return None

	def getContent(self,page):
		pattern=re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
		items=re.findall(pattern,page)
		for item in items:
			print(item)
class Tool:
	removeImg=re.compile('<img.*?>| {7}|')
	removeAddr=re.compile('<a.*?>|</a>')
	replaceLine=re.compile('<tr>|<div>|</div>|</p>')
	replaceTD=re.compile('<td>')
	replacePara=re.compile('<p.*?>')
	replaceBR=re.compile('<br><br>\<br>')
	removeExtraTag=re.compile('<.*?>')
baseURL='http://www.baidu.com/p/3138733512'
bdtb=Baidu(baseURL,1)
bdtb.getPage(1)
		
