# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 15:45:05 2016

@author: makejeef
"""

import xlrd
from math import log
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
myfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/simhei.ttf')  
#导入数据
data=xlrd.open_workbook('noise.xls')
table1=data.sheets()[1]
table2=data.sheets()[3]
nrows=table1.nrows#行数
ncols=table1.ncols#列数
time=table1.row_values(0)[1:]
#PNL_tem=table1.row_values(29)[1:]

sc=[]
for x in range(ncols):
    if x>=1:
        sc.append(table1.col_values(x))
    
spl=[]
M=[]
mrows=table2.nrows
mcols=table2.ncols
for x in range(mcols):  
    if x<=5:
        spl.append(table2.col_values(x))
    elif x>=6 and x<11:
        M.append(table2.col_values(x))
n=[]
for i in range(ncols):
    if i<68:
        n.append([])
        k=len(n)
        for j in range(nrows):
            if j>0 and j<25:
                if sc[i][j]==0:
                    n[k-1].append(0) 
                elif sc[i][j]>=spl[1][j]:
                    n[k-1].append(pow(10,(M[1][j]*(sc[i][j]-spl[3][j]))))
                elif sc[i][j]>=spl[2][j] and sc[i][j]<=spl[1][j]:
                    n[k-1].append(pow(10,M[0][j]*(sc[i][j]-spl[2][j])))
                elif sc[i][j]>=spl[5][j] and sc[i][j]<=spl[2][j]:
                    n[k-1].append(0.3*pow(10,M[3][j]*(sc[i][j]-spl[5][j])))
                elif sc[i][j]>=spl[4][j] and sc[i][j]<=spl[5][j]:
                    n[k-1].append(0.1*pow(10,M[2][j]*(sc[i][j]-spl[3][j])))
PNL=[]
for x in range(68):
    PNL.append(40+(10*log(0.85*max(n[x])+0.15*sum(n[x]),10)/log(2,10)))
#得出斜率
s=[]
for x in range(68):
    s.append([])
    i=len(s)
    for y in range(24):
         if y<3:
            s[i-1].append(0)
         else:
            s[i-1].append(round(sc[x][y]-sc[x][y-1],2))
#判定绝对值，圈出声压级
sc_1=[]
for x in range(68):
    sc_1.append([])
    i=len(sc_1)
    for y in range(25):
        if y<4:
            sc_1[i-1].append(sc[x][y])
        else :
            if abs(s[x][y-1]-s[x][y-2])>5:
                if s[x][y]>0 and s[x][y]>s[x][y-1]:
                    sc_1[i-1].append((sc[x][y]+sc[x][y+2])/2)  
                elif s[x][y]<=0 and s[x][y-1]>0:
                    sc_1[i-1].append((sc[x][y-1]+sc[x][y+1])/2)
                else:
                    sc_1[i-1].append(sc[x][y])
            else:
                sc_1[i-1].append(sc[x][y])
#重新计算斜率s_1和修正声压级       
s_1=[]
for x in range(68):
    s_1.append([])
    i=len(s_1)
    for y in range(25):
        if y<2:
            s_1[i-1].append(s[x][y])
        elif y<4:
            s_1[i-1].append(round(sc_1[x][4]-sc_1[x][3],2))
        elif y<24:
            s_1[i-1].append(round(sc_1[x][y]-sc_1[x][y-1],2))
        elif y==24:
            s_1[i-1].append(s_1[x][y-1])
#算出斜率平均值
ave_s=[]
for x in range(68):
	ave_s.append([])
	i=len(ave_s)
	for y in range(24):
         if y<3:
             ave_s[i-1].append(0)
         else:
             ave_s[i-1].append(round((s_1[x][y-1]+s_1[x][y]+s_1[x][y+1])/3,2))
#声压级最后结果
sc_2=[]
for x in range(68):
	sc_2.append([])
	i=len(sc_2)
	for y in range(25):
		if y<4:
			sc_2[i-1].append(sc_1[x][y])
		else:
			sc_2[i-1].append(round(sc_2[x][y-1]+ave_s[x][y-1]))
#比较原始声压级与最终声压级之差
F=[]
C=[]
for x in range(68):
    F.append([])
    C.append([])
    i=len(F)
    j=len(C)
    for y in range(25):
        if y>0 and y<12:
            F[i-1].append(sc[x][y]-sc_2[x][y])
            if (sc[x][y]-sc_2[x][y])>=1.5 and (sc[x][y]-sc_2[x][y])<3:
                C[j-1].append((sc[x][y]-sc_2[x][y])/3-0.5)
            elif (sc[x][y]-sc_2[x][y])>=3 and (sc[x][y]-sc_2[x][y])<20:
                C[j-1].append((sc[x][y]-sc_2[x][y])/6)
            elif (sc[x][y]-sc_2[x][y])>20:
                C[j-1].append(3.33)
            else:
                C[j-1].append(0)
        elif y>=12 and y<=22:
            F[i-1].append(sc[x][y]-sc_2[x][y])
            if (sc[x][y]-sc_2[x][y])>=1.5 and (sc[x][y]-sc_2[x][y])<3:
                C[j-1].append((sc[x][y]-sc_2[x][y])*2/3-1)
            elif (sc[x][y]-sc_2[x][y])>=3 and (sc[x][y]-sc_2[x][y])<20:
                C[j-1].append((sc[x][y]-sc_2[x][y])/3)
            elif (sc[x][y]-sc_2[x][y])>20:
                C[j-1].append(6.66)
            else:
                C[j-1].append(0)
        elif y>22 and y<25:
            F[i-1].append(sc[x][y]-sc_2[x][y])
            if (sc[x][y]-sc_2[x][y])>=1.5 and (sc[x][y]-sc_2[x][y])<3:
                C[j-1].append((sc[x][y]-sc_2[x][y])/3-0.5)
            elif (sc[x][y]-sc_2[x][y])>=3 and (sc[x][y]-sc_2[x][y])<20:
                C[j-1].append((sc[x][y]-sc_2[x][y])/6)
            elif (sc[x][y]-sc_2[x][y])>20:
                C[j-1].append(3.33)
            else:
                C[j-1].append(0)
#计算出纯音修正因子
c_fin=[]				
for x in range(68):
	c_fin.append(round(max(C[x]),2))
print(PNL,max(PNL))
print(c_fin)
#计算出纯音感觉噪声级
PNLT=[]
for x,y in zip(c_fin,PNL):
    PNLT.append(x+y)
print(PNLT,max(PNLT))

#作图
plt.plot(time,PNLT)
plt.xlabel('时间(秒)',fontproperties=myfont)
plt.ylabel('有效感觉噪声级(分贝)',fontproperties=myfont)
plt.title('飞跃噪声',fontproperties=myfont)
plot1=plt.plot(time[6],PNLT[6],'go',label='in point')
plot2=plt.plot(time[56],PNLT[56],'ro',label='out point')
plt.show()