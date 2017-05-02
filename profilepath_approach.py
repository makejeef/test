# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 21:24:18 2017

@author: makejeef
"""

from math import sqrt,asin,tan,pi,cos,sin,atan
import matplotlib.pyplot as plt
import pylab as pl
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
myfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')  


T=15 #环境温度
W=93500 #飞机起飞重量
N=2 #发动机数量
g=32.15 #英尺单位转换
k=1.688 #单位转化常量
p0=1.013e5 #大气压力
rho=1.225 #空气密度
temp0=288.15 #环境温度
#第一阶段下降
h1=6000
h2=3000
v1=250
v2=162.5
gama=pi/60
s1=(h1-h2)/tan(gama)
a1=((v2/cos(gama))**2-(v1/cos(gama))**2)/(2*s1/cos(gama))

#第二阶段下降
h2=3000
h3=1500
v2=162.5
v3=152.5
gama=pi/60
s2=(h2-h3)/tan(gama)
a2=((v3/cos(gama))**2-(v2/cos(gama))**2)/(2*s2/cos(gama))

#第三阶段下降
h3=1500
h4=1000
v3=152.5
v4=142.5
gama=pi/60
s3=(h3-h4)/tan(gama)
a3=((v4/cos(gama))**2-(v3/cos(gama))**2)/(2*s3/cos(gama))

#第三阶段下降
h4=1000
h5=0
v4=142.5
v5=135.2
gama=pi/60
s4=(h4-h5)/tan(gama)
a4=((v5/cos(gama))**2-(v4/cos(gama))**2)/(2*s4/cos(gama))

#作图
l1=s1
l2=l1+s2
l3=l2+s3
l4=l3+s4

#描点
x_mic=110286.82
y_mic=0
alpha=atan(h4/(l4-l3))#进近角度
V_mic=sqrt(2*a4*sin(alpha)*4200+v5**2)#麦克风最近位置速度
V_start=V_mic-a4*1
S_10dB1=V_start*1+a4/2
S_10dB2=V_mic*4+a4*16/2

x_in=l4-(S_10dB1+4194.24)*cos(alpha)
y_in=(S_10dB1+4194.24)*sin(alpha)
x_out=l4-(4194.24-S_10dB2)*cos(alpha)
y_out=(4194.24-S_10dB2)*sin(alpha)

plot_x=[l3,l4]
plot_y=[h4,h5]
plt.plot(plot_x,plot_y)
plt.xlabel('跑道(英尺)',fontproperties=myfont)
plt.ylabel('飞行高度(英尺)',fontproperties=myfont)
plt.title('进近剖面',fontproperties=myfont)
#plot1=plt.plot(l4,h5,'go',label='in point')
plot1=plt.plot(x_in,y_in,'go',label='in point')
plot2=plt.plot(x_out,y_out,'ro',label='out point')
plot3=plt.plot(x_mic,y_mic,'ko',label='mic location')


#坐标区间
pl.ylim(-100,1000)
pl.show
