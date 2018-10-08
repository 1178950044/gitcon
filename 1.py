#coding=utf-8
import turtle as tr
import random
import datetime
import time

tr.screensize(1000,1000,)
d={1:'yellow',2:'red',3:'blue',4:'black'}
n=1  #循环次数
high=n*10-10

while 1:
    starttime = datetime.datetime.now()
    x = random.randint(50,100)
    y = random.randint(1,4)
    c1 = random.randint(-150,400)
    c2 = random.randint(-400,250)
    if c1+x>500:
        continue
    elif c1-x<-500:
        continue
    elif c2-x<-500:
        continue
    elif c2+x>500:
        continue
    tr.hideturtle()
    tr.penup()
    tr.goto(-450,470-high)
    tr.write(n)
    tr.goto(-420,470-high)
    tr.write(x)
    tr.goto(-390,470-high)
    tr.write(d[y])
    tr.goto(-350,470-high)
    tr.write("圆心:")
    tr.goto(-310,470-high)
    tr.write(c1)
    tr.goto(-280,470-high)
    tr.write(c2)
    tr.goto(c1,c2)
    tr.fillcolor(d[y])
    tr.pendown()
    tr.begin_fill()
    tr.circle(x)
    tr.end_fill()
    time.sleep(0.5)
    n=n+1
    high=n*10-10
    endtime = datetime.datetime.now()
    f2 = open('F:\\workspace\\untitled1\数据.txt', 'w+')
    f2.read()
    f2.write('次数：'+str(n)+'  ')
    f2.write('半径：'+str(x)+'  ')

    f2.write('颜色序号：'+str(y)+'  ')
    f2.write('圆心坐标：'+str(c1)+'，')
    f2.write(str(c2)+'  ')
    f2.write('开始：'+str(starttime)+'  ')
    f2.write('结束：'+str(endtime)+'  ')
    f2.write('\n')

    f2.close()
