import json
import jsonpath
import urllib.request
url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1698068995931_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers = {
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
    'Cookie':'t=4c2309c93005bfd5d42baa9a0cbfc01c; xlly_s=1; cna=a/28HcYVKyoCAXdiNb6u0smT; tb_city=110100; tb_cityName="sbG+qQ=="; cookie2=14eb919d02a3d2d132d267e09848ff7f; v=0; _tb_token_=fee33a50f36b5; tfstk=d1pWnXOLQz47Er1LUYi2lymMh3XIbUMaRkspjHezvTBRAvTeuu-yYLRfve8mx0XyvwTBuZYCt0bFJwTevQoqQA-kq9XpdVkZQszOK9EAumUkq3XhpozK_IKudGtyFGjb_Xaj2H3bH-ww5565p8Qh8Ks5Mj-RkNQsYg17o3_bpVpfQg2N5qnaOo1gdi_ZcmN3tyOcmuf..; isg=BHBwrABQ4UVcjr1BFd15HECAQT7CuVQDj_2q2mrB2kueJRDPEsmZk4wbfS1FtQzb; l=fBIzd5bnPM-4MZpwBO5Bnurza77TfIRb4sPzaNbMiIEGa1kPtFsNdNCtzWCeSdtjgTCv6etPw3HW8dLHR3xg5c0c07kqm0-t3xvtaQtJe',
    'Referer':'https://dianying.taobao.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
content = content.split('(')[1].split(")")[0]
with open('./解析器/Jsonpath/taopiaopiao.json','w',encoding='utf-8') as fp:
    fp.write(content)
obj = json.load(open('./解析器/Jsonpath/taopiaopiao.json','r',encoding='utf-8'))
city_list = jsonpath.jsonpath(obj,'$..regionName')
print(city_list)