# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import seaborn as sns
import folium
#import webbrowser
from folium.plugins import HeatMap

#posi=pd.read_excel("2015Cities-CHINA.xlsx")
posi=pd.read_excel("2015Cities-CHINA_4.xlsx")

num = 130

lat = np.array(posi["lat"][0:num])                        # 获取维度之纬度值
lon = np.array(posi["lon"][0:num])                        # 获取经度值
pop = np.array(posi["pop"][0:num],dtype=float)    # 获取人口数，转化为numpy浮点型
gdp = np.array(posi["GDP"][0:num],dtype=float)    # 获取数，gdp转化为numpy浮点型
gdp_ave = np.array(posi["GDP_Average"][0:num]/10,dtype=float)    # 获取数，平均gdp转化为numpy浮点型
print(posi["GDP_Average"][0:num])
#exit(0)

#data1 = [[lat[i],lon[i],pop[i]] for i in range(num)]    #将数据制作成[lats,lons,population]的形式
#data1 = [[lat[i],lon[i],gdp[i]] for i in range(num)]    #将数据制作成[lats,lons,gdp]的形式
data1 = [[lat[i],lon[i],gdp_ave[i]] for i in range(num)]    #将数据制作成[lats,lons,gdp_ave]的形式

map_generate = folium.Map(location=[35,110],zoom_start=5)    #绘制Map，开始缩放程度是5倍
HeatMap(data1).add_to(map_generate)  # 将热力图添加到前面建立的map里

#file_path = r"/Users/fuchuang/Downloads/polulation.html"
file_path = r"/Users/fuchuang/Downloads/gdp_average.html"
map_generate.save(file_path)     # 保存为html文件

