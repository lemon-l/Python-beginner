'''
明确目的
找到数据对应的网页
分析网页的结构找到数据所在的标签位置

# beautiful soup;scrapy  爬虫用的

模拟HTTP请求，向服务器发送请求，获取到服务器返回给我们的html
用正则表达式提取我们要的数据
'''
#断点调试
from urllib import request

class Spider():
    url = "http://www.huitu.com/"

    def __fetch_content(self):
       r = request.uriopen(Spider.url)
       htmls = r.read()
       htmls = str(htmls,encoding = 'utf-8')
       a = 1

    def __analysis(self,htmls):
        pass

    def go(self):
        htmls = self.__fetch_content()
        self.__fetch_content()


spider = Spider()
spider.go()