#coding:utf-8
import httplib
import re
def get_fake_hearders():
    headers = {
    'Connection' : 'keep-alive',
    'Cache-Control' : 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
    }
def get_html(host, uri, headers):
    try:
        httpClient = httplib.HTTPConnection(host, 80)
        httpClient.request('GET', uri, headers)
        response = httpClient.getresponse()
        print response.status
        return response.read()
    finally:
        if httpClient:
            httpClient.close()
def get_city_list(html):
    reg = re.compile(r'http://\w+\.esf\.sina\.com\.cn')
    result = reg.findall(html)
    #print reduce(lambda x, y: x + "\n" + y, result)
    return result
def remove_duplicate(l):
    l2 = list(set(l))
    print reduce(lambda x, y: x + "\n" + y, l2)
    return l2
if __name__ == '__main__':
    headers = get_fake_hearders();
    page = get_html('esf.sina.com.cn', '', headers)
    city_list = remove_duplicate(get_city_list(page))
    print len(city_list)
