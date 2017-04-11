# _*_ coding:utf-8 _*_
import urllib,urllib.request,re

user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
headers={'User_Agent':user_agent}

class Tool:
	removeImg=re.compile('<img.*?>| {7}|')#img和七位空格
	removeAddr=re.compile('<a.*?>|</a>')#超链接
	replaceLine=re.compile('<tr>|<div>|</div>|</p>')#换行标钱
	replaceTD=re.compile('<td>')#制表位
	replacePara=re.compile('<p.*?>')#段落开头
	replaceBR=re.compile('<br><br>\<br>')#换行符
	removeExtraTag=re.compile('<.*?>')#其余标签
	def replace(self,x):
		x=re.sub(self.removeImg,"",x)
		x=re.sub(self.removeAddr,"",x)
		x=re.sub(self.replaceLine,"\n",x)
		x=re.sub(self.replaceTD,"\t",x)
		x=re.sub(self.replacePara,"\n  ",x)
		x=re.sub(self.replaceBR,"\n",x)
		x=re.sub(self.removeExtraTag,"",x)
		return x.strip()

class Baidu:
	def __init__(self,baseURL,seeLZ):
		self.baseURL=baseURL
		self.seeLZ='?seeLZ'+str(seeLZ)
		self.tool=Tool()

#获取网页代码，页码
	def getPage(self,pageNum):
		try:
			url=self.baseURL+self.seeLZ+'&pn'+str(pageNum)
			request=urllib.request.Request(url)
			response=urllib.request.urlopen(request)
			print(response.read())
			return response
		except urllib.request.URLError:
			if hasattr(e,'reason'):
				print(u'连接失败原因：',e.reason)
				return None
			
#标题
	def getTitle(self):
		page=self.getTitle(1)
		pattern=re.compile('<h1 class="core_title_text.*?>(.*?)</h1>',re.S)
		result=re.search(pattern,page)
		if result:
			return result.group(1).strip()
		else:
			return None

#页数
	def getPageNum(self):
		pattern=re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
		result=re.search(pattern,page)
		if result:
			return result.group(1).strip()
		else:
			return None

#每一层楼内容
	def getContent(self,page):
		pattern=re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
		items=re.findall(pattern,page)
		#for item in items:
		#	print(item)
		print(self.tool.replace(items[1]))
baseURL='http://tieba.baidu.com/p/3138733512'
bdtb=Baidu(baseURL,1)
bdtb.getPage(1)
		
