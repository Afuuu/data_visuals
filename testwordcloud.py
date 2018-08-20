#!/usr/bin/env python


from os import path
from PIL import Image
#from Pillow  import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__)

#text = open(path.join(d, 'douban_movie.txt'),encoding='utf-8').read() #豆瓣top电影标签
#text = open(path.join(d, 'xuzhimo.txt'),encoding='utf-8').read() #徐志摩的情诗
text = open(path.join(d, '90love.txt'),encoding='utf-8').read() #90后的情诗

#结巴分词，切分生成字符串
#cut_text = " ".join(jieba.cut(text))
cut_text = text

mode_png = np.array(Image.open(path.join(d, "alice_color.png")))
#alice_coloring = np.array(Image.open(path.join(d, "heart1.jpeg")))

# 设置停用词
stopwords = set(STOPWORDS)
stopwords.add("我们")
stopwords.add("电影")

# 通过 mask 参数 来设置词云形状
wc = WordCloud(background_color="white", max_words=2000, mask=mode_png,
               stopwords=stopwords, max_font_size=40, random_state=42, font_path='SimHei.ttf')


# 生成词云
wc.generate(cut_text)

# create coloring from image
image_colors = ImageColorGenerator(mode_png)

# 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
plt.figure('生成词云图')
plt.imshow(wc)#, interpolation="bilinear")
plt.axis("off") #是否显示坐标轴

#plt.figure('figurefc2')
#plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
#plt.axis("off")

#plt.figure('模型图')
#plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
#plt.axis("off")

plt.show()

