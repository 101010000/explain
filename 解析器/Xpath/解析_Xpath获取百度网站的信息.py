#Xpath解析
#(1)本地文件--->etree.parse()
#(2)服务器响应数据--->etree.HTML()    response.read().decode("UTF-8")
import urllib.request
from lxml import etree

# 1.获取网页源码
url = "https://www.baidu.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.207.132.170 Safari/537.36"
}
#请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
#模拟浏览器向服务器响应
response = urllib.request.urlopen(request)
#获取响应数据
content = response.read().decode("UTF-8")
# print(content)

# 2.解析 etree.HTML()
#解析服务器响应的文件
tree = etree.HTML(content)
#获取想要的数据 xpath的返回值是一个列表类型的数据
result = tree.xpath("//input[@id='su']/@value")[0]

# 3.打印
print(result)