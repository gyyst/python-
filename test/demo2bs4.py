import re

from bs4 import BeautifulSoup


file=open("./百度一下，你就知道.html","rb")

html=file.read()
bs=BeautifulSoup(html,"html.parser")
# print(bs.head)
#1.Tag标签及其内容，第一个

#print(bs.title.string)
#2.NavigableString  字符串

#print(type(bs))
#3.BeautifulSoup  整个文档


#print(type(bs.a.string))
#4.Comment 标注


#print(bs.head.contents[0])

#find_all字符串过滤：会查找与字符串完全匹配的内容
#t_list=bs.find_all("a")

#正则表达式搜索：使用search()搜索
#t_list=bs.find_all(re.compile("a"))


#方法：传入一个函数，根据函数的要求来搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
# t_list=bs.find_all(name_is_exists)

#2.kwargs    参数href class_
# t_list=bs.find_all(class_=True)
# for item in t_list:
#     print(item)

#limit


#css选择器
#print(bs.select("title"))
#print(bs.select(".mnav"))#通过类名来查找
#print(bs.select("#u1"))#通过id来查找
#print(bs.select("a[class='bri'])"))
print(bs.select("head > title"))

file.close()