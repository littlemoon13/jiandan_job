from urllib import request
import re
import pymysql

import tomxin.getInfo
def getZJUT():
# if __name__ == '__main__':
    url = "http://zjut.jysd.com/"
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'校外资讯','</li></ul><ul class="css-con1">')
    title = tomxin.getInfo.get_content(info,'company.+?>','<')
    url = tomxin.getInfo.get_content(info,'company','"')
    i=0
    for u in url:
        r_city="浙江"
        r_school="浙江工业大学"
        r_title=title[i]
        r_trait = "ZJUT" + u[-6:]
        r_url = "http://zjut.jysd.com/company" + u
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'vContent cl infoContent">', '<div class="vCon cl">')
        print(r_title + "\n" + r_url)
        i += 1
