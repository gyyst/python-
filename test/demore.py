import re



#正则表达式：字符串模式判断字符串是否符合一定的标准

#创建模式对象
# pat=re.compile("AA")#标准
# b=pat.search("CBAAACDSAAAAA")  #search方法查找比对

#b=re.search("asd","Aasd")#前面的是标准，后面的是要校验的字符串

#b=re.findall("a",'asddsaASDACasa')
#b=re.findall("[a-z]+","asddsaASDACasa")

b=re.sub("a","A","avcdcasd")#找到a用A来替换,在第三个字符串中




print(b)