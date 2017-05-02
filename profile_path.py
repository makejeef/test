# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 21:07:28 2016

@author: makejeef
"""
from math import sqrt,asin,tan,pi,cos,sin
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
import seaborn as sns
import matplotlib
myfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')  


T=15 #环境温度
W=93500 #飞机起飞重量
N=2 #发动机数量
g=32.15 #英尺单位转换
k=1.688 #单位转化常量
p0=1.013e5 #大气压力
rho=1.225 #空气密度
temp0=288.15 #环境温度
#Flap_ID=15
B1=0.010507
C1=0.471774
R1=0.092489
#Flap_ID=5
B2=0.012098
C2=0.489900
R2=0.084985
#Flap_ID=INT
R3=0.076701
#Flap_ID=ZERO
R4=0.068416
#maxtakeoff
E1=12972
F1=-2.31038
Ga1=-0.008256
Gb1=4.1349e-8
H1=0
#maxclimb
E2=11561.8
F2=-2.94773
Ga2=-0.010534
Gb2=5.2756e-8
H2=0
#滑跑阶段
h1=0 #高度
theta1=1 #温度比
delta1=1 #气压比
sigma1=1 #密度比
V1=C1*sqrt(W) #校准速度 节
Vt1=V1/sqrt(sigma1)
Fn1=E1+F1*V1+Ga1*h1+Gb1*h1**2+H1*T
Sto=(B1*theta1*(W/delta1)**2)/(N*Fn1) #滑跑距离

#滑跑时间
a1=(V1*1.69*sqrt(sigma1))**2/(2*Sto)#平均加速度
t1=sqrt(2*Sto/a1)

#恒速爬升阶段
V2=V1
K1=1.01
h2=1000
delta2=(1.003e5-3.194*h2)/p0
sigma2=(1.213-3.139e-5*h2)/rho
Fn2=E1+F1*V2+Ga1*h2+Gb1*h2**2+H1*T
avg_W1=(W+W/delta2)/2
gama1=asin(K1*(N*Fn2/avg_W1-R1)) #弧度
Delta_S1=(h2-h1)/tan(gama1)#水平距离 英尺
#爬升时间
V2_x=V2*cos(gama1)
t2=Delta_S1/V2_x

#加速爬升
h3=1310
V3=154
delta3=(1.013e5-3.194*h3)/p0
theta3=(288.2-0.002*h3)/temp0
sigma3=(1.213-3.139e-5*h3)/rho
ROC1=1741
Fn3=E1+F1*V3+Ga1*h3+Gb1*h3**2+H1*T
Vt2=V2/sqrt(sigma2)
Vt3=V3/sqrt(sigma3)
avg_Vt1=(Vt2+Vt3)/2
avg_Fn1=(Fn3+Fn2)/2
avg_W1=(W/delta2+W/delta3)/2
a1=g*(N*avg_Fn1/avg_W1-R1)
G1=ROC1/(60*k*avg_Vt1)
Sseg1=0.95*k**2*(Vt3**2-Vt2**2)/(2*(a1-G1*g)) #单位英尺
tem_h3=h2+Sseg1*G1/0.95
#迭代之后得到h3=1310
#爬升时间
t3=(h3-h2)*60/ROC1
#第二阶段加速爬升

h4=1442.6
V4=164
delta4=(1.003e5-3.194*h4)/p0
theta4=(288.2-0.002*h4)/temp0
sigma4=(1.213-3.139e-5*h4)/rho
ROC2=1306
Fn4=E1+F1*V4+Ga1*h4+Gb1*h4**2+H1*T
Vt4=V4/sqrt(sigma4)
avg_Vt2=(Vt4+Vt3)/2
avg_Fn2=(Fn3+Fn4)/2
avg_W2=(W/delta3+W/delta4)/2
a2=g*(N*avg_Fn2/avg_W2-R2)
G2=ROC2/(60*k*avg_Vt2)
Sseg2=0.95*k**2*(Vt4**2-Vt3**2)/(2*(a2-G2*g))
tem_h4=tem_h3+Sseg2*G2/0.95
#迭代后得到tem_h4=1442.4
#爬升时间
t4=(h4-h3)*60/ROC2

#第三阶段加速爬升

h5=1742.53
V5=199
delta5=(1.003e5-3.194*h5)/p0
theta5=(288.2-0.002*h5)/temp0
sigma5=(1.213-3.139e-5*h5)/rho
ROC3=1000
Fn5=E2+F2*V5+Ga2*h5+Gb2*h5**2+H2*T
Vt5=V5/sqrt(sigma5)
avg_Vt3=(Vt4+Vt5)/2
avg_Fn3=(Fn5+Fn4)/2
avg_W3=(W/delta4+W/delta5)/2
a3=g*(N*avg_Fn3/avg_W3-R3)
G3=ROC3/(60*k*avg_Vt3)
Sseg3=0.95*k**2*(Vt5**2-Vt4**2)/(2*(a3-G3*g))
tem_h5=tem_h4+Sseg3*G3/0.95
#迭代后得到tem_h5=1742.6
#爬升时间
t5=(h5-h4)*60/ROC3

#第二阶段恒速爬升
V6=V5
K2=0.95
h6=3000
delta6=(1.003e5-3.194*h6)/p0
sigma6=(1.213-3.139e-5*h6)/rho
Fn6=E2+F2*V6+Ga2*h6+Gb2*h6**2+H2*T
avg_W4=(W/delta6+W/delta5)/2
gama2=asin(K2*(N*Fn6/avg_W4-R3)) #弧度
Delta_S2=(h6-h5)/tan(gama2)#水平距离 英尺
#爬升时间
V6_x=V6*cos(gama2)
t6=Delta_S2/V6_x


#第四阶段加速爬升

h7=3518.5
V7=250
delta7=(1.003e5-3.194*h7)/p0
theta7=(288.2-0.002*h7)/temp0
sigma7=(1.213-3.139e-5*h7)/rho
ROC4=1000
Fn7=E2+F2*V7+Ga2*h7+Gb2*h7**2+H2*T
Vt6=V6/sqrt(sigma6)
Vt7=V7/sqrt(sigma7)
avg_Vt5=(Vt7+Vt6)/2
avg_Fn5=(Fn6+Fn7)/2
avg_W5=(W/delta6+W/delta7)/2
a5=g*(N*avg_Fn5/avg_W5-R3)
G5=ROC4/(60*k*avg_Vt5)
Sseg4=0.95*k**2*(Vt7**2-Vt6**2)/(2*(a5-G5*g))
tem_h7=h6+Sseg4*G3/0.95
#迭代后得到tem_h7=3518.84
#爬升时间
t7=(h7-h6)*60/ROC4


#第三阶段恒速爬升
V8=V7
K2=0.95
h8=5500
delta8=(1.003e5-3.194*h8)/p0
sigma8=(1.213-3.139e-5*h8)/rho
Fn8=E2+F2*V8+Ga2*h8+Gb2*h8**2+H2*T
avg_W5=(W/delta7+W/delta8)/2
gama3=asin(K2*(N*Fn8/avg_W5-R3)) #弧度
Delta_S3=(h8-h7)/tan(gama3)#水平距离 英尺
#爬升时间
V8_x=V8*cos(gama3)
t8=Delta_S3/V8_x



#第四阶段恒速爬升
V9=V8
K2=0.95
h9=7500
delta9=(1.003e5-3.194*h9)/p0
sigma9=(1.213-3.139e-5*h9)/rho
Fn9=E2+F2*V9+Ga2*h8+Gb2*h9**2+H2*T
avg_W6=(W/delta9+W/delta8)/2
gama4=asin(K2*(N*Fn9/avg_W6-R3)) #弧度
Delta_S4=(h9-h8)/tan(gama4)#水平距离 英尺
#爬升时间
V9_x=V9*cos(gama4)
t9=Delta_S4/V9_x


#第五阶段恒速爬升
V10=V9
K2=0.95
h10=10000
delta10=(1.003e5-3.194*h10)/p0
sigma10=(1.213-3.139e-5*h10)/rho
Fn10=E2+F2*V10+Ga2*h10+Gb2*h10**2+H2*T
avg_W7=(W/delta9+W/delta10)/2
gama5=asin(K2*(N*Fn10/avg_W7-R3)) #弧度
Delta_S5=(h10-h9)/tan(gama5)#水平距离 英尺
#爬升时间
V10_x=V10*cos(gama5)
t10=Delta_S5/V10_x
t=t1+t2+t3+t4+t5+t6+t7+t8+t9+t10
s_final=Sto+Delta_S1+Sseg1+Sseg2+Sseg3+Delta_S2+Sseg4+Delta_S3+Delta_S4+Delta_S5

#作图
l1=Delta_S1
l2=l1+Sseg1
l3=l2+Sseg2
l4=l3+Sseg3
l5=l4+Delta_S2
l6=l5+Sseg4
l7=l6+Delta_S3
l8=l7+Delta_S4
l9=l8+Delta_S5
x_in1=5047.58
y_in1=890.25
x_out1=8276.52
y_out1=1310

x_mic1=4800
x_mic2=12800
y_mic=0

x_in2=11762.17
y_in2=1548.39
x_out2=16922.09
y_out2=1963.45

plot_x=[-Sto,0,l1,l2,l3,l4,l5]
plot_y=[0,h1,h2,h3,h4,h5,h6]
plt.plot(plot_x,plot_y)
plt.xlabel('跑道(英尺)',fontproperties=myfont)
plt.ylabel('飞行高度(英尺)',fontproperties=myfont)
plt.title('起飞剖面',fontproperties=myfont)
plot1=plt.plot(x_in1,y_in1,'go',label='in point')
plot2=plt.plot(x_out1,y_out1,'ro',label='out point')
plot3=plt.plot(x_in2,y_in2,'go',label='out point')
plot4=plt.plot(x_out2,y_out2,'ro',label='out point')
plot5=plt.plot(x_mic1,y_mic,'yo',label='mic location')
plot6=plt.plot(x_mic2,y_mic,'ko',label='mic location')


#作最小距离图
#theta = np.linspace(0,2*pi,36)
#r1=500
#x1 = 12800+r1*cos(theta)
#y1 = r1*sin(theta)

#plt.plot(x1,y1)

#坐标区间
pl.xlim(-10000,27000)
pl.ylim(-100,3000)
pl.show