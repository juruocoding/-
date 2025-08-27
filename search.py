import requests
def search_net(text_utf8):
    try:
#        r=rqst.get('http://www.baidu.com/s')
        #http://wwww.baidu.com/s?wd=keyword
        print(text_utf8)
        s_text=text_utf8.replace( "\\","hw")
        print(s_text)
        # url="https://wyw.hwxnet.com/view/"+s_text+".html"
        # print(url)
        # r=requsts.get(url)
        # print(r.status_code)
        # print(r.request.url)
        # print(r.text[:1000])
    except:
        print("请求失败")
print("\xE6\x96\xB0")
search_net("\xE6\x96\xB0")