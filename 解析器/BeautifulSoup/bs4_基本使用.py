from bs4 import BeautifulSoup
#默认打开文件是gbk，所以需要指定编码utf-8
soup = BeautifulSoup(open(r'D:\VS code examples\python\example\python爬虫\解析器\BeautifulSoup\bs4_基本使用.html',encoding='utf-8'),'lxml')
#根据标签名查找节点
#找到的是第一个符合条件的数据
# print(soup.a)
#获取标签的属性和属性值
# print(soup.a.attrs)

#bs4的一些函数
#(1).find()
#返回的是第一个符合条件的数据
# print(soup.find('a'))
#根据title的值来找到对应的标签对象
# print(soup.find('a',title="a2"))
#根据class的值来找到对应的标签对象 
# print(soup.find('a',class_='a3'))#不支持class（注意）class需要添加下划线

#(2).find_all()
# print(soup.find_all('a'))
#如果想要获取的是多个标签的数据，那么需要在find_all()的参数中添加的是列表的数据
#print(soup.find_all(['a','span']))
#limit参数限制返回的数据的数量
# print(soup.find_all('li',limit=2))

#(3).select() (推荐使用)
#1.select()方法返回的是一个列表，并且会返回多个数据
# print(soup.select('a'))
#2.可以通过.代表class #代表id 把此操作当中类选择器
# print(soup.select('.a3'))
#3.print(soup.select('#l1'))
#4.属性选择器
#查找li标签中有l1的标签
# print(soup.select('li[id]'))
#查找li标签中有l2的标签
# print(soup.select('li[id="l2"]'))
#5.层级(层次)选择器
#    后代选择器
#    div下的li
# print(soup.select('div li'))
#    子代选择器
#    某标签的第一级子标签
# print(soup.select('div > ul > li'))

#节点信息
#    获取节点内容
# obj = soup.select('#d1')
# 如果标签对象中 只有内容 那么string和get_text()都可以获取
# 如果标签对象中 除了内容还有标签 那么string不可以获取 get_text()都可以获取
# print(obj[0].string)
# print(obj[0].get_text())#推荐使用
#    节点的属性
obj = soup.select("#d1")[0]
#name是标签的名字
# print(obj.name)
#attrs是 标签的属性值 以字典形式返回
# print(obj.attrs)
#获取节点的属性
print(obj.attrs.get('class')) #推荐使用
print(obj.get('class'))
print(obj['class'])