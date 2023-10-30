from lxml import etree
#Xpath解析
#(1)本地文件--->etree.parse()
#(2)服务器响应数据--->etree.HTML()    response.read().decode("UTF-8")
#xpath解析本地文件
tree = etree.parse("解析_Xpath.html")
# print(tree)
#查找ul下的li '//'获取所有子孙节点 '/'获取子节点
# li_list = tree.xpath("//li")

#查找所有有id属性的li
#text()获取标签中的内容
# li_list = tree.xpath("//li[@id]/text()")

#查找id为12的li标签 #注意引号
# li_list = tree.xpath("//li[@id='12']/text()")

#查找id为21的li标签的class的属性值
# li = tree.xpath("//li[@id='21']/@class")
# print(li)

#查找id中包含1的li标签 模糊查询
# li_list = tree.xpath("//li[contains(@id,'1')]/text()")

#查找id中以1为首的li标签 模糊查询
# li_list = tree.xpath("//li[starts-with(@id,'1')]/text()")
#逻辑运算 id='' and class='' ------ //title | //ul
li_list = tree.xpath("//li[contains(@id,'1') and starts-with(@class,'3')]/text()")
print(li_list)
print(len(li_list))

