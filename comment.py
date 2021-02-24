import re
import urllib.request,urllib.error
import json

last = ['6716706003418103507','6716701977205046126','6716733350338901296','6716709711492873145','6716753294460916527','6716972825301197893','6716701666792995004','6718121320958325174','6717734443999757821']
        #2                     3                     4                     5                     6                     7                     8                    9                     10
urllist = []
datalist = []

def main():
    #基础网页
    baseurl = "https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=0&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=1613986644139"
    data = getData(baseurl)
    savaDate(datalist)

#爬取网页
def getData(baseurl):
    #逐一解析数据
    for i in range(0, 9):
        source = int(baseurl[-3:]) + i
        url = "https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + \
              last[i - 1] + "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=1613986644" + str(source)
        urllist.append(url)
    #print(urllist)
    Analysis(urllist)
    return urllist

#解析数据
def Analysis(urllist):
    for i in range(0,len(urllist)):
        html = askURL(urllist[i])
        data = re.findall((re.compile(r'"content":"(.*?)"')), html)
        #print(data)
        datalist.extend(data)
    return datalist

#得到指定url的网页内容
def askURL(url):
    head = {  # 模拟浏览器头部信息
     "user-agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }  # 用户代理
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)#网页信息
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

#保存数据
def savaDate(datalist):
    with open("在一起.txt","w",encoding="utf-8") as f:
        for i in datalist:
            f.write(i + "\n")
    print("ok")

def txtToJson():
    with open("在一起.txt", 'r', encoding="utf-8") as file:
        seq = re.compile(":")
        result = []
        for line in file:
            list = seq.split(line.strip())
            item = {
                "details": list[0]
            }
            result.append(item)
    with open('comments.json', 'w',encoding="utf-8") as dump_f:
        dump_f.write(json.dumps(result,indent=2,ensure_ascii=False))

if __name__ == "__main__":
    main()
    txtToJson()
    print("爬取完毕")