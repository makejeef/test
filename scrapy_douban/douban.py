# coding=utf-8
import urllib,urllib.request,re,os

user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
headers={'User_Agent':user_agent}

class Tool:
	replaceIphoto=re.compile('lthumb')
	def replace(self,x):
		x=re.sub(self.replaceIphoto,'lphoto',x)


class DOUBAN:
	def __init__(self,baseUrl,startNum):
		self.baseUrl=baseUrl
		self.startNum='start='+str(startNum*18)
		self.tool=Tool()
#得到网页url
	def getPage(self,pageNum):
		try:
			url=self.baseUrl+self.startNum
			request=urllib.request.Request(url)
			response=urllib.request.urlopen(request)
			return response.read().decode('utf-8')
		except urllib.request.URLError as e:
			if hasattr(e,'reason'):
				print(u'连接失败原因：',e.reason)
				return None
#得到图片url
	def getContent(self,pageNum):
		page=self.getPage(pageNum)
		pattern=re.compile('<img width=.*?src="(.*?)" />')
		items=re.findall(pattern,page)
		return items

#小图换大图url
	def replaceName(self,imageUrl):
		pattern=re.compile('lthumb')
		x=re.sub(pattern,'lphoto',imageUrl)
		return x
#保存路径
	def mkdir(self,path):
		isExists=os.path.exists(path)
		if not isExists:
			os.mkdir(path)
			return True
		else:
			return False

#保存单张图片
	def save_single(self,url,pageNum):
		self.mkdir(pageNum)
		pattern=re.compile('public/p(.*?).jpg')
		x=re.findall(pattern,url)
		filename=x[0]+'.jpg'
		urllib.request.urlretrieve(url,filename)

#保存图片
	def saveImg(self,pageNum):
		urls=self.getContent(pageNum)
		for url in urls:
			url=self.replaceName(url)
			print(url)
			self.save_single(url,pageNum)
		
baseUrl='https://www.douban.com/photos/album/1622832404/?'
douban=DOUBAN(baseUrl,0)
douban.saveImg(0)
