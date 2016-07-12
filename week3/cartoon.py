#coding=utf-8
import urllib
import re
import HTMLParser
import time
import os
import random

#显示下载进度
def schedule(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per




#爬取网页内所有URL
def getHtml(url):

    page = urllib.urlopen(url)
    html = page.read()
    #urls = html.replace(" ", "")
    #allurls = re.findall('<a.*?href=.*?<\/a>', html, re.I)
    allurls = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", html)
    downloadImg(html)
    for url in allurls:
        print 1111
        print url
        try:
            page1 = urllib.urlopen(url)
            html1 = page1.read()
            downloadImg(html1)
        except Exception as e:
            print("Error",e)




    else:
        print '显示完成'
    return html

#爬取并下载所有URL中的图片
def downloadImg(html):
    reg = r'img src="(http://.+?\.jpg)"' and r'src="(http://.+?\.jpg)"' #and  r'src="(http://.+?\.png)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    # 定义文件夹的名字
    t = time.localtime(time.time())
    foldername = str(t.__getattribute__("tm_year")) + "-" + str(t.__getattribute__("tm_mon")) + "-" + str(
        t.__getattribute__("tm_mday"))
    picpath = 'E:\\pic\\%s' % (foldername)  # 下载到的本地目录

    if not os.path.exists(picpath):  # 路径不存在时创建一个
        os.makedirs(picpath)

    for imgurl in imglist:
        num=int(time.time()*1000)
        target = picpath + '\\%s.jpg' %num
        print 'Downloading image to location: ' + target + '\nurl=' + imgurl
        image = urllib.urlretrieve(imgurl, target, schedule)


    return image;

#爬取首页内图片
'''
def getImg(html):
    #reg = r'img src="(http://.+?\.jpg)"'
    reg = r'img src="(http://.+?\.jpg)"' and r'src="(http://.+?\.jpg)"' and  r'src="(http://.+?\.png)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1
'''

if __name__ == '__main__':

    html = getHtml("http://comic.qq.com/pic/")

#downloadImg(html)
print "Download has finished."

#print getImg(addr)