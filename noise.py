#!usr/bin/env python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('NPDtable.csv')
df=df[df['NPD_ID']=='BR710']
df=df[df['Noise metric']=='EPNL']
df=df[df['Op type']=='D']

x=df['Power setting']
y1=df['L_200ft']
y2=df['L_400ft']
y3=df['L_630ft']
y4=df['L_1000ft']
y5=df['L_2000ft']
y6=df['L_4000ft']
y7=df['L_6300ft']
y8=df['L_10000ft']
y9=df['L_16000ft']
y10=df['L_25000ft']
z1=np.polyfit(x,y1,1)
z2=np.polyfit(x,y2,1)
z3=np.polyfit(x,y3,1)
z4=np.polyfit(x,y4,1)
p1=np.poly1d(z1)
p2=np.poly1d(z2)
p3=np.poly1d(z3)
p4=np.poly1d(z4)
print(p1,p2,p3,p4)
yvals1=np.polyval(z1,x)
yvals2=np.polyval(z2,x)
yvals3=np.polyval(z3,x)
yvals4=np.polyval(z4,x)
plot1=plt.plot(x,y1,'*',label='original values')
plot2=plt.plot(x,yvals1,'r',label='ployfit values')
plot3=plt.plot(x,y2,'*',label='original values')
plot4=plt.plot(x,yvals2,'g',label='ployfit values')
plot5=plt.plot(x,y3,'*',label='original values')
plot6=plt.plot(x,yvals3,'b',label='ployfit values')
plot7=plt.plot(x,y4,'*',label='original values')
plot8=plt.plot(x,yvals4,'r',label='ployfit values')
plt.xlabel('Thrust')
plt.ylabel('EPNL')
plt.legend(loc=4)
plt.title('noise')
plt.show()
sns.regplot(x=x,y=y1,data=df)
