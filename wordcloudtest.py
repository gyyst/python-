import jieba  #分词
from matplotlib import pyplot as plt  #绘图，数据可视化
from wordcloud import WordCloud   #词云
from PIL import Image  #图片处理
import numpy as np   #矩阵运算
import sqlite3   #数据库

#准备词云所需要的词
con=sqlite3.connect("movie.db")
cur=con.cursor()
sql='select introduction from movie250'
data=cur.execute(sql)
text=""
for item in data:
    text=text+item[0]

cur.close()
con.close()
# 分词
cut=jieba.cut(text)
string=' '.join(cut)
print(len(string))

img=Image.open('static/assets/img/tree.jpg')
img_array=np.array(img)#将图片转换为数组
wc=WordCloud(
    background_color='white',
    mask=img_array,
    font_path="msyh.ttc",
    scale=10

)
wc.generate_from_text(string)


#绘制图片

fig=plt.figure(1)
plt.imshow(wc)
plt.axis('off')#不显示坐标轴
#plt.show()

#输出词云文件
plt.savefig('static/assets/img/word.jpg',dpi=500)