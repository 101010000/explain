import urllib.request
import urllib.parse
from lxml import etree
import random
import json
def get_request(page):
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=9884162849547937827&ipn=rj&ct=201326592&is=&fp=result&fr=ala&word=%E5%A5%B3%E6%98%9F%E5%9B%BE%E7%89%87&queryWord=%E5%A5%B3%E6%98%9F%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&expermode=&nojc=&isAsync=&'
    # pn=60&rn=30
    # pn=90&rn=30
    # pn=120&rn=30
    data = {
        'pn':page*30,
        'rn':30
    }
    headers = {
        # 'Accept':'text/plain, */*; q=0.01',
        # 'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
        # 'Connection':'keep-alive',
        'Cookie':'newlogin=1; BIDUPSID=96A829FEC1E945E26B80F419125966FA; PSTM=1697088103; BAIDUID=0B95F954D8142D2E44FABDFD98F3EB93:FG=1; MCITY=-218%3A; BDUSS=l-RUJSYUFHejJuSGRpc0NIaGVzV29Rd3EzeXA1MTZ4ak9CLVEza3d0NURlVTlsSVFBQUFBJCQAAAAAAQAAAAEAAAB~00YrAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEPsJ2VD7CdlME; BDUSS_BFESS=l-RUJSYUFHejJuSGRpc0NIaGVzV29Rd3EzeXA1MTZ4ak9CLVEza3d0NURlVTlsSVFBQUFBJCQAAAAAAQAAAAEAAAB~00YrAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEPsJ2VD7CdlME; BAIDUID_BFESS=0B95F954D8142D2E44FABDFD98F3EB93:FG=1; ZFY=MJFIwNiB7tul6dBrZX8K5ZPOmO:AhPAov:AT9v201zTtw:C; BDRCVFR[Zh1eoDf3ZW3]=mk3SLVN4HKm; delPer=0; PSINO=6; H_PS_PSSID=26350; BA_HECTOR=212ga18k0l212l00a00galae1ijc3r41o; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BCLID=7888582590410690142; BCLID_BFESS=7888582590410690142; BDSFRCVID=2p-OJeC62lK740bqbCj6MR_WgqHdVYoTH6aoS2chG751hCc42BqaEG0Phx8g0KuMHRX8ogKKLgOTHULF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; BDSFRCVID_BFESS=2p-OJeC62lK740bqbCj6MR_WgqHdVYoTH6aoS2chG751hCc42BqaEG0Phx8g0KuMHRX8ogKKLgOTHULF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tbIO_K-atKK3fJrYhPIV-PAt-U4Xat0XKKOLVKoMHl7keq8CD4vvjT3Q-lQa3-IqBGrd-b3hWnb4oJ72y5jHhpJX-U7xt5LD2g72_IoP-RjpsIJMMbAWbT8U5tc7QqkOaKviahRjBMb1SqRDBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTD-Dhe4tX-NFJt5DeJU5; H_BDCLCKID_SF_BFESS=tbIO_K-atKK3fJrYhPIV-PAt-U4Xat0XKKOLVKoMHl7keq8CD4vvjT3Q-lQa3-IqBGrd-b3hWnb4oJ72y5jHhpJX-U7xt5LD2g72_IoP-RjpsIJMMbAWbT8U5tc7QqkOaKviahRjBMb1SqRDBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTD-Dhe4tX-NFJt5DeJU5; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=ala; ab_sr=1.0.1_MGMxOGEwMGZjMDAxMjg4N2VjOWZlZTMzZGI4NDgxM2VmNWJjZDBlZGQ0YjgzZDlmYTI2NjRmNWFjN2FjNDBhMTU0NjQ5M2E4ZmRmYWFhN2IzOWZkMTc5ZDhjZTY0OTIwMGEwZWNjZDhmMGVlYzZjMWYyODNiMmM5MmY4ZDE4Y2NhOTRiZWRjZjNlOTQ2M2NmNDU3OWI4YmEyOTkxNDRjNQ==',
        # 'Host':'image.baidu.com',
        # 'Referer':'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C5%AE%D0%C7%CD%BC%C6%AC&fr=ala&ala=1&alatpl=normal&pos=0&dyTabStr=MTEsMCwyLDMsNiw0LDEsNSw3LDgsOQ%3D%3D',
        # 'Sec-Ch-Ua':'"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
        # 'Sec-Ch-Ua-Mobile':'?0',
        # 'Sec-Ch-Ua-Platform':'"Windows"',
        # 'Sec-Fetch-Dest':'empty',
        # 'Sec-Fetch-Mode':'cors',
        # 'Sec-Fetch-Site':'same-origin',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
        # 'X-Requested-With':'XMLHttpRequest',
    }
    data = urllib.parse.urlencode(data)
    url = url + data
    request = urllib.request.Request(url=url, headers=headers)
    return request
def goto_response(request):
    # proxies_pool = [
    #     {"http":"127.0.0.1:7890"},
    # ]
    # proxies = random.choice(proxies_pool)
    # handler = urllib.request.ProxyHandler(proxies=proxies)
    # opener = urllib.request.build_opener(handler)
    # response = opener.open(request)
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content
def download(content,page):
    content = json.loads(content)
    for x in range(1,page+1):
        for i in range(0,30):
            try:
                if content['data'][i]['thumbURL'] == None:
                    url = content['data'][i]['replaceUrl'][0]
                else:
                    url = content['data'][i]['thumbURL']
                if '|' in content['data'][i]['fromPageTitle']:
                    name = content['data'][i]['fromPageTitle'].replace('|',' ')
                else:
                    name = content['data'][i]['fromPageTitle']
                urllib.request.urlretrieve(url=url, filename=f'./解析器/Xpath/img/img_{name}.jpg')
            except Exception as e:
                print(e)
            i += 1
        x += 1 
if __name__ == '__main__':
    start_Page = int(input("请输入起始页码:"))
    end_Page = int(input("请输入结束页码:"))
    for page in range(start_Page, end_Page+1):
        #请求对象的定制
        request = get_request(page)
        #模拟浏览器向服务器响应数据
        content = goto_response(request)
        #下载
        download(content,page)