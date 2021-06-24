%matplotlib inline
import matplotlib.pyplot as plt

list1=[[300 for i in range(31)] for j in range(31)]
list2=[[300 for i in range(31)] for j in range(31)]
list1[15][15]=350.0
dx=1.0
dy=1.0
dt=0.1
alpha=1.0 
c1x=(alpha*dt)/(dx*dx)
c1y=(alpha*dt)/(dy*dy)
# 2つの条件のuとvから、先に定数を2通り用意する
u=[0.3, 0.1]
v=[0, 0.2]
cu=[]
cv=[]
for k in range(2):
  cu.append((u[k]*dt)/(2*dx))
  cv.append((v[k]*dt)/(2*dy))

levels = [i for i in range(300,350)]
#fig = plt.figure(figsize=(5,4)) # colaboratoryでの出力に仕様変更
#ax = fig.add_subplot(111)
#im = ax.contourf(list1,levels,cmap="jet")
#fig.colorbar(im)

for istep in range(0,1001):
        if istep%200==0:
                print('step = '+str(istep))

#               f = open('output'+str(istep)+'.dat','w') #　colaboratoryではデータファイルの出力せず
#               for j in range(0,31):
#                       for i in range(0,31):
#                               f.write(str(i)+'   '+str(j)+'   '+str(list1[j][i])+'\n')
#               f.close
                
                fig = plt.figure(figsize=(5,4)) # colaboratoryでの出力に仕様変更
                ax = fig.add_subplot(111) #　colaboratoryでの出力に仕様変更
                im = ax.contourf(list1,levels,cmap="jet")
                fig.colorbar(im) #　colaboratoryでの出力に仕様変更
                plt.pause(0.001)
#               fname='figure'+str(istep)+'.png'　#　colaboratoryでは画像ファイルの出力せず
#               plt.savefig(fname)　#　colaboratoryでは画像ファイルの出力せず

        if istep<=500:  # istepが500以下の時は定数const_u, const_vにcv[0], cu[0]を代入
          const_u = cu[0]
          const_v = cv[0]
        else:  # istepが500より大きい時は定数const_u, const_vにcv[1], cu[1]を代入
          const_u = cu[1]
          const_v = cv[1]

        for j in range(1,30):
                for i in range(1,30):
                        list2[j][i]=list1[j][i]  \
                        -const_u * ( list1[j][i+1] - list1[j][i-1] ) \
                        -const_v * ( list1[j+1][i] - list1[j-1][i] ) \
                        +c1x*(list1[j][i+1]-2.0*list1[j][i]+list1[j][i-1])  \
                        +c1y*(list1[j+1][i]-2.0*list1[j][i]+list1[j-1][i])

        list2[15][15]=350.0

        for j in range(1,30):
                for i in range(1,30):
                        list1[j][i]=list2[j][i]
