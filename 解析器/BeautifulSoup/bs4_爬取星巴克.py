from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.starbucks.com.cn/menu/'
headers = {
    # 'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
    # 'Referer':'https://www.starbucks.com.cn/',
    'Host':'www.starbucks.com.cn',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
    'Cookie':'sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218b5f2ec719581-0594f6f09e7233-745d5771-1327104-18b5f2ec71b94e%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThiNWYyZWM3MTk1ODEtMDU5NGY2ZjA5ZTcyMzMtNzQ1ZDU3NzEtMTMyNzEwNC0xOGI1ZjJlYzcxYjk0ZSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218b5f2ec719581-0594f6f09e7233-745d5771-1327104-18b5f2ec71b94e%22%7D; ZHh6ku4z=AxvHLl-LAQAAv_YJA-EmzE9ZWI3Rj4VxWwxa2BrZBGu6p5SYubc8urGUyE8-AXdiNQAXTtQxwH8AAEB3AAAAAA|1|0|19d4215d8528f088939776f25713c35576753ac7',
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

soup = BeautifulSoup(content,'lxml')

for i in range(len(soup.select('a>div[class="preview circle"]',limit=10))): #限制10张图片
    try:
        url = soup.select('a>div[class="preview circle"]')[i].attrs['style'].split('(')[1].split(')')[0][1:-1]
        obj_url = "https://www.starbucks.com.cn/" + url
        print(obj_url)
        obj_name = soup.select('a>strong')[i].get_text()
        # urllib.request.urlretrieve(url=obj_url,filename=f"./解析器/BeautifulSoup/img/img_{obj_name}.jpg")
    except Exception as e:
        print(e)