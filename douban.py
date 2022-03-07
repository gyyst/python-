import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup
import re
import xlwt
import sqlite3


def main():
    baseurl="https://movie.douban.com/top250?start="
    datalist=getdata(baseurl)
    #savepath=".\\豆瓣电影top250.xls"
    #savedata(datalist,savepath)
    dbpath="movie.db"
    savedata2DB(datalist,dbpath)



#影片详情链接的规则
findlink=re.compile(r'<a href="(.*?)">')   #创建正则表达式规则

#影片图片
findImSrc=re.compile(r'<img .*src="(.*?)"',re.S) #让换行符包含在字符中

#影片片名
findTitle= re.compile(r'<span class="title">(.*)</span>')

#影片评分
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')

#评价人数
findJudge=re.compile(r'<span>(\d*)人评价</span>')

#找到概况
findInq=re.compile(r'<span class="inq">(.*)</span>')

#找到影片的相关内容
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)


def getdata(baseurl):
    datalist=[]
    for i in range(0,10):
        url=baseurl+str(i*25)
        html=askurl(url)
        soup=BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):    #查找符合要求的字符串，形成列表
            #print(item) #测试查看电影item信息
            data=[]       #保存一部电影的全部信息
            item=str(item)

            #影片详情链接
            link=re.findall(findlink,item)[0]        #通过正则表达式查找指定字符串
            data.append(link)
            imgSrc=re.findall(findImSrc,item)[0]
            data.append(imgSrc)
            titles=re.findall(findTitle,item)
            if(len(titles)==2):
                ctitle=titles[0]
                data.append(ctitle)
                otitle=titles[1].replace("/","")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')

            rating=re.findall(findRating,item)[0]
            data.append(rating)

            judgenum=re.findall(findJudge,item)[0]
            data.append(judgenum)

            inq=re.findall(findInq,item)
            if len(inq)!=0:
                inq=inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")

            bd=re.findall(findBd,item)[0]
            bd=re.sub('<br(\s+)?/>(\s+)?'," ",bd)
            bd=re.sub("/"," ",bd)
            data.append(bd.strip())

            datalist.append(data)

    print(datalist)
    return datalist

def savedata(datalist,savepath):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)
    col=('电影详情链接',"图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print("%d"%(i+1))
        data=datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])

    book.save(savepath)

def savedata2DB(datalist,dbpath):
    init_db(dbpath)
    conn=sqlite3.connect(dbpath)
    cursor=conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index==4 or index==5:
                continue
            data[index]='"'+data[index]+'"'
        sql='''
                insert into movie250(
                info_link,pic_link,cname,ename,score,rated,introduction,info
                )
                values(%s)'''%",".join(data)
        print(sql)
        cursor.execute(sql)
        conn.commit()
    cursor.close()
    conn.close()


    print("")

def init_db(dbpath):
    sql='''
        create table movie250(
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        introduction text,
        info text
        
        )
    
    '''
    conn=sqlite3.connect(dbpath)
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

def askurl(url):
    head={
        "User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

if __name__ =="__main__":
    main()
    print("爬取完毕")