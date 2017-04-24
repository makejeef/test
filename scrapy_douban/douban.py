# coding=utf-8
import urllib,urllib.request,re,os

user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
headers={'User_Agent':user_agent}

class Tool:
	replaceIphoto=re.compile('lthumb')
	def replace(self,x):
		x=re.sub(self.replaceIphoto,'lphoto',x)


class DOUBAN:
	def __init__(self,baseUrl):
		self.baseUrl=baseUrl
		self.tool=Tool()
#得到网页url
	def getPage(self,url):
		try:
			request=urllib.request.Request(url)
			response=urllib.request.urlopen(request)
			return response.read().decode('utf-8')
		except urllib.request.URLError as e:
			if hasattr(e,'reason'):
				print(u'连接失败原因：',e.reason)
				return None
#得到相册页数
	def getPageNum(self,url):
		page=self.getPage(url)
		pattern=re.compile('<span class="thispage".*="(\d+)">1</span>')
		m=re.findall(pattern,page)
		num=int(m[0])
		return num

#得到图片url
	def getContent(self,url):
		items=[]
		for x in range(self.getPageNum(url)):
			pageurl=url+'?start='+str(x*18)
			page_response=self.getPage(pageurl)	
			pattern=re.compile('<img width=.*?src="(.*?)" />')
			items.extend(re.findall(pattern,page_response))
		return items
		print(items)

#小图换大图url
	def replaceName(self,url):
		items=self.getContent(url)
		pattern=re.compile('lthumb')
		sub_url=[re.sub(pattern,'lphoto',x) for x in items]
		return sub_url
#保存路径
	def mkdir(self,path):
		isExists=os.path.exists(path)
		if not isExists:
			os.mkdir(path)
			return True
		else:
			return False

#保存单张图片
	def save_single(self,url):
		#得到相册名
		'''pattern=re.compile('<title>(.*?)</title>')
		response=urllib.request.urlopen(urllib.request.Request(url)).read().decode('utf-8')
		name=re.findall(pattern,response)
		#print(name)
		pattern_=re.compile('-')
		name_final=re.sub(pattern_,'_',name[0])
		self.mkdir(name_final)
		#为相片命名
		'''
		items=self.replaceName(url)
		print(len(items))
		for item in items:
			pattern=re.compile('https.*?public/p(\d+)')
			x=re.findall(pattern,item)
			#print(x)
			filename=x[0]+'.jpg'
			urllib.request.urlretrieve(item,filename)
			
		
if __name__=='__main__':
	url=input('plz input the album url:')
	douban=DOUBAN(url)
	douban.save_single(url)
