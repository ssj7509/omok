import turtle
import random
t=turtle.Turtle()
t.shape("turtle")
list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
list_2=[]
for i in range(15):
    list_2.append(i+1)
t.up()
t.goto(-270,220)                                             #판깔기
t.speed(0)
for i in range(1,16,1):                    
    t.write(i)
    t.down()
    t.fd(480)
    t.write(i)
    t.up()
    t.backward(480)
    t.right(90)
    t.fd(30)
    t.left(90)
t.goto(-240,250)
t.right(90)
for i in range(1,16,1):
    t.write(list[i-1])
    t.down()
    t.fd(480)
    t.write(list[i-1])
    t.up()
    t.backward(480)
    t.left(90)
    t.fd(30)
    t.right(90)
t.goto(-290,-260)
t.left(90)

xlist=[]                                            
ylist=[]
x,y,a,b,c=(0,)*5
for i in range(1,10):
    globals()[f"a_{i}"]=0
    globals()[f"b_{i}"]=0

d=0
d_1=[]
e=0
x_1=0
y_1=0
x_2=0
y_2=0
x_3=0
y_3=0
x_4=0
y_4=0
i=1
f_1=[]
j=0
j_2=0
for i in range(0,15,1):                             
    xlist.append(-240+30*i)
    ylist.append(220-30*i)
coordinate_x=1                                    
coordinate_y=1
edge=[]
now_list=[]
now_list_user=[]
now_list_turtle=[]
reverse_list=[]
reverse_list_user=[]
reverse_list_turtle=[]
now_list_x=[]
now_list_y=[]
now_list_x_user=[]
now_list_y_user=[]
now_list_x_turtle=[]
now_list_y_turtle=[]
simulate=[0]
simulate_2=[1]
simulate_3=[2]
simulate_4=[3]
def prt(x):
    for i in range(len(x)):
        x_1=x[i]
        x_2=xlist.index(x_1[0])
        y_2=ylist.index(x_1[1])
        flist_2.append((list[x_2],list_2[y_2]))
def draw():
    t.down()
    t.begin_fill()
    t.circle(13)
    t.up()
    t.end_fill()
def user_turn():
    insert_4(simulate)
    insert_3(simulate)
    insert_2(simulate)
    turtle_turn_5_1(slist_12,slist_12)
    turtle_turn_5_1(slist_13,slist_13)
    turtle_turn_5_1(slist_13,slist_14)
    turtle_turn_5_1(slist_12,slist_14)
    turtle_turn_5_1(slist_14,slist_14)
    for i in range(len(ban_list_user)):
        x_1=ban_list_user
        x_2=x_1[i]
        x_3=xlist.index(x_2[0])
        x_4=ylist.index(x_2[1])
        ban_list_user_2.append((list[x_3],list_2[x_4]))
    if len(ban_list_user)>=1:
        print(ban_list_user_2,"은 금수 자리입니다.")
    while True:
        x=str(input("x좌표를 입력하시오:"))
        y=int(input("y좌표를 입력하시오:"))
        if x not in list or y not in list_2:
            print("좌표를 벗어났습니다.")
        elif (xlist[list.index(x)],ylist[y-1]) in now_list:
            print("이미 돌이 있는 자리입니다.")
        else:
            break
    slist_2.clear()
    slist_3.clear()
    slist_4.clear()
    slist_5.clear()
    slist_6.clear()
    slist_7.clear()
    slist_8.clear()
    slist_9.clear()
    slist_10.clear()
    slist_11.clear()
    slist_12.clear()
    slist_13.clear()
    slist_14.clear()
    slist_15.clear()
    slist_16.clear()
    slist_17.clear()
    slist_18.clear()
    slist_19.clear()
    slist_4_2.clear()
    slist_5_2.clear()
    slist_6_2.clear()
    slist_7_2.clear()
    slist_8_2.clear() 
    slist_9_2.clear()
    slist_12_2.clear()
    slist_13_2.clear()
    slist_14_2.clear()
    slist_4_3.clear()
    slist_5_3.clear()
    slist_6_3.clear()
    slist_7_3.clear()
    slist_8_3.clear() 
    slist_9_3.clear()
    slist_12_3.clear()
    slist_13_3.clear()
    slist_14_3.clear()
    ban_list.clear()
    ban_list_2.clear()
    ban_list_user.clear()
    ban_list_user_2.clear()
    special_list.clear()
    special_list.clear()
    coordinate_x=xlist[list.index(x)]
    coordinate_y=ylist[y-1]
    t.goto(coordinate_x,coordinate_y-15)
    t.fillcolor("black")
    now_list_x.append(coordinate_x)
    now_list_y.append(coordinate_y)
    now_list_x_user.append(coordinate_x)
    now_list_y_user.append(coordinate_y)
    now_list.append((coordinate_x,coordinate_y))
    reverse_list.append((coordinate_y,coordinate_x))
    now_list_user.append((coordinate_x,coordinate_y))
    reverse_list_user.append((coordinate_y,coordinate_x))
    now_list_x.sort()
    now_list_y.sort()
    now_list_x_user.sort()
    now_list_y_user.sort()
    now_list.sort()
    now_list_user.sort()
    reverse_list.sort()
    reverse_list_user.sort()
    draw()
c_1=0
while c_1!=1 and c_1!=2:
    c_1=int(input("먼저 하시겠습니까?\n(1:예,2:아니요)\n:"))
slist=[]
slist_2=[] 
slist_3=[] 
slist_4=[] 
slist_5=[]
slist_6=[]
slist_7=[]
slist_8=[] 
slist_9=[]
slist_10=[]
slist_11=[]
slist_12=[]
slist_13=[]
slist_14=[]
slist_15=[]
slist_16=[]
slist_17=[]
slist_18=[]
slist_19=[]
slist_4_2=[] 
slist_5_2=[]
slist_6_2=[]
slist_7_2=[]
slist_8_2=[] 
slist_9_2=[]
slist_12_2=[]
slist_13_2=[]
slist_14_2=[]
slist_4_3=[] 
slist_5_3=[]
slist_6_3=[]
slist_7_3=[]
slist_8_3=[] 
slist_9_3=[]
slist_12_3=[]
slist_13_3=[]
slist_14_3=[]
silist=[]
silist_2=[]
silist_3=[]
silist_4=[]
elist=[]
flist=[]  
flist_2=[]
flist_3=[]
flist_4=[]
ban_list=[]
ban_list_2=[]
ban_list_user=[]
ban_list_user_2=[]
special_list=[]
def f(c):
    if c==now_list_user or c==simulate or c==simulate_3:
        return now_list_turtle
    elif c==now_list_turtle or c==simulate_2 or c==simulate_4:
        return now_list_user
def g(c):
    if c==now_list_user or c==simulate or c==simulate_3:
        return now_list_user
    elif c==now_list_turtle or c==simulate_2 or c==simulate_4:
        return now_list_turtle
def h(c):
    if c==now_list_user:
        return now_list_user
    elif c==now_list_turtle:
        return now_list_turtle
    elif c==simulate:
        return slist_9_2
    elif c==simulate_2:
        return slist_8_2
    elif c==simulate_3:
        return slist_7_2
    elif c==simulate_4:
        return slist_5_2
def k(c):
    if c==simulate:
        return slist_9_3
    elif c==simulate_2:
        return slist_8_3
    elif c==simulate_3:
        return slist_7_3
    elif c==simulate_4:
        return slist_5_3
def turtle_turn_2(x,y):
    coordinate_x=x
    coordinate_y=y
    t.goto(coordinate_x,coordinate_y-15)
    t.fillcolor("yellow")
    now_list_x_turtle.append(coordinate_x)
    now_list_y_turtle.append(coordinate_y)
    now_list.append((coordinate_x,coordinate_y))
    now_list_turtle.append((coordinate_x,coordinate_y))
    reverse_list.append((coordinate_x,coordinate_y))
    reverse_list_turtle.append((coordinate_y,coordinate_x))
    now_list_x_turtle.sort()
    now_list_y_turtle.sort()
    now_list.sort()
    now_list_turtle.sort()
    reverse_list.sort()
    reverse_list_turtle.sort()
def turtle_turn_3(x,y,c,d,j,j_2):
    if x>=-240 and x<=180 and y>=-200 and y<=220 and (((x,y) not in now_list) or (j_2==2)):
        if d==1:
            if c==now_list_user:
                slist_2.append(9)
                slist_10.append((x,y))
                if 3 in elist:
                    slist_17.append((x,y))
            elif c== now_list_turtle:
                slist_2.append(10)
                slist_11.append((x,y))
            elif c==simulate:
                silist.append((x,y))
            elif c==simulate_3:
                silist_3.append((x,y))
            elif c==simulate_2 or c==simulate_4:
                if 4 in elist:
                    flist_4.append((x,y))
                flist_4.sort()
                for i in range(len(flist_4)):
                    x_1=flist_4[i]
                    x_2=x_1[0]
                    y_2=x_1[1]
                    if c==simulate_2:
                        silist_2.append((x_2,y_2))
                    elif c==simulate_4:
                        silist_4.append((x_2,y_2))
                flist_4.clear()
        elif d==2:
            if c==now_list_user:
                slist_2.append(3)
                if j_2==1:
                    slist_5.append((x,y))
                    slist_5_2.append((x,y,j))
                elif j_2==2:
                    slist_5_3.append((x,y,j))
                if 3 in elist:
                    slist_16.append((x,y))
            elif c==now_list_turtle:
                slist_2.append(6)
                if j_2==1:
                    slist_7.append((x,y))
                    slist_7_2.append((x,y,j))
                elif j_2==2:
                    slist_7_3.append((x,y,j))
            elif c==simulate:
                if j_2==1:
                    slist_13.append((x,y))
                    slist_13_2.append((x,y,j))
                elif j_2==2:
                    slist_13_3.append((x,y,j))
        elif d==3:
            if c==now_list_user:
                if 1 in elist:
                    if 3 in elist:
                        slist_15.append((x,y))
                    slist_2.append(2)
                    if j_2==1:
                        slist_4.append((x,y))
                        slist_4_2.append((x,y,j))
                    elif j_2==2:
                        slist_4_3.append((x,y,j))
                else:
                    slist_2.append(7)
                    if j_2==1:
                        slist_8.append((x,y))
                        slist_8_2.append((x,y,j))
                        if 3 in elist:
                            slist_19.append((x,y))
                    elif j_2==2:
                        slist_8_3.append((x,y,j))
            elif c==now_list_turtle:
                if 1 in elist:
                    slist_2.append(5)
                    if j_2==1:
                        slist_6.append((x,y))
                        slist_6_2.append((x,y,j))
                    elif j_2==2:
                        slist_6_3.append((x,y,j))
                else:
                    slist_2.append(8)
                    if j_2==1:
                        slist_9.append((x,y))
                        slist_9_2.append((x,y,j))
                    elif j_2==2:
                        slist_9_3.append((x,y,j))
            elif c==simulate:
                if 1 in elist:
                    if j_2==1:
                        slist_12.append((x,y))
                        slist_12_2.append((x,y,j))
                    elif j_2==2:
                        slist_12_3.append((x,y,j))
                else:
                    if j_2==1:
                        slist_14.append((x,y))
                        slist_14_2.append((x,y,j))
                    elif j_2==2:
                        slist_14_3.append((x,y,j))
        elif d==4:
            if c==now_list_user:
                if c_1==1 and 4 in elist:
                    ban_list_user.append((x,y))
                slist_2.append(1)
                slist_3.append((x,y))
            elif c==now_list_turtle:
                if c_1==2 and 4 in elist:
                    ban_list.append((x,y))
                slist_2.append(4)
                slist_18.append((x,y))
            elif c==simulate:
                if c_1==1 and 4 in elist:
                    ban_list_user.append((x,y))

def turtle_turn_3_1(x,y,c,d,j,j_2):
    if c==simulate_2 or c==simulate_4:
        turtle_turn_3(x,y,c,d,j,j_2)
def turtle_turn_4(a_0,b_0,a_1,b_1,a_2,b_2,a_3,b_3,a_4,b_4,a_5,b_5,a_6,b_6,a_7,b_7,a_8,b_8,a_9,b_9,c,d,e,j):
    if d==1:
        if (a_4,b_4) not in now_list and (a_5,b_5) not in now_list and (c==now_list_user or c==now_list_turtle):
            if (a_3,b_3) in f(c)+edge and (a_6,b_6) not in now_list and (a_7,b_7) not in now_list and (a_9,b_9) not in now_list:
                elist.append(3)
                turtle_turn_3(a_5,b_5,c,d,j,1)
                elist.clear()
                turtle_turn_3(a_6,b_6,c,d,j,1)
                if c==now_list_user:
                    elist.append(3)
                    turtle_turn_3(a_4,b_4,c,d,j,1)
                    elist.clear()
                elif c==now_list_turtle:
                    turtle_turn_3(a_7,b_7,c,d,j,1)
            elif (a_2,b_2) in f(c)+edge and (a_9,b_9) in f(c)+edge and (a_3,b_3) not in now_list and (a_6,b_6) not in now_list and (a_7,b_7) not in now_list:
                elist.append(3)
                turtle_turn_3(a_4,b_4,c,d,j,1)
                turtle_turn_3(a_5,b_5,c,d,j,1)
                elist.clear()
                turtle_turn_3(a_6,b_6,c,d,j,1)
                if c==now_list_user:
                    turtle_turn_3(a_3,b_3,c,d,j,1)
            elif (a_7,b_7) in f(c)+edge and (a_8,b_8) in f(c)+edge and (a_2,b_2) not in now_list and (a_3,b_3) not in now_list and (a_6,b_6) not in now_list:
                turtle_turn_3(a_3,b_3,c,d,j,1)
                elist.append(3)
                turtle_turn_3(a_4,b_4,c,d,j,1)
                turtle_turn_3(a_5,b_5,c,d,j,1)
                elist.clear()
                if c==now_list_user:
                    turtle_turn_3(a_6,b_6,c,d,j,1)
            elif (a_6,b_6) in f(c)+edge and (a_3,b_3) not in now_list and (a_2,b_2) not in now_list and (a_8,b_8) not in now_list:
                turtle_turn_3(a_3,b_3,c,d,j,1)
                elist.append(3)
                turtle_turn_3(a_4,b_4,c,d,j,1)
                elist.clear()
                if c==now_list_user:
                    elist.append(3)
                    turtle_turn_3(a_5,b_5,c,d,j,1)
                    elist.clear()
                elif c==now_list_turtle:
                    turtle_turn_3(a_2,b_2,c,d,j,1)
            elif (a_3,b_3) not in now_list and (a_6,b_6) not in now_list:
                if (a_2,b_2) in f(c)+edge and (a_7,b_7) not in now_list and (a_9,b_9) not in now_list:
                    elist.append(3)
                    turtle_turn_3(a_4,b_4,c,d,j,1)
                    turtle_turn_3(a_5,b_5,c,d,j,1)
                    elist.clear()
                    turtle_turn_3(a_6,b_6,c,d,j,1)
                    if c==now_list_user:
                        turtle_turn_3(a_3,b_3,c,d,j,1)
                    elif c==now_list_turtle:
                        turtle_turn_3(a_7,b_7,c,d,j,1)
                elif (a_7,b_7) in f(c)+edge and (a_2,b_2) not in now_list and (a_8,b_8) not in now_list:
                    turtle_turn_3(a_3,b_3,c,d,j,1)
                    elist.append(3)
                    turtle_turn_3(a_4,b_4,c,d,j,1)
                    turtle_turn_3(a_5,b_5,c,d,j,1)
                    elist.clear()
                    if c==now_list_user:
                        turtle_turn_3(a_6,b_6,c,d,j,1)
                    elif c==now_list_turtle:
                        turtle_turn_3(a_2,b_2,c,d,j,1)
                elif (a_2,b_2) not in now_list and (a_7,b_7) not in now_list:
                    if (a_9,b_9) in f(c)+edge and (a_8,b_8) not in now_list:
                        turtle_turn_3(a_3,b_3,c,d,j,1)
                        turtle_turn_3(a_6,b_6,c,d,j,1)
                        elist.append(3)
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        elist.clear()
                        if c==now_list_turtle:
                            turtle_turn_3(a_2,b_2,c,d,j,1)
                    elif (a_8,b_8) in f(c)+edge and (a_9,b_9) not in now_list:
                        turtle_turn_3(a_3,b_3,c,d,j,1)
                        turtle_turn_3(a_6,b_6,c,d,j,1)
                        elist.append(3)
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        elist.clear()
                        if c==now_list_turtle:
                            turtle_turn_3(a_7,b_7,c,d,j,1)
                    elif (a_8,b_8) not in now_list and (a_9,b_9) not in now_list:
                        turtle_turn_3(a_3,b_3,c,d,j,1)
                        turtle_turn_3(a_6,b_6,c,d,j,1)
                        elist.append(3)
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        elist.clear()
                        if c==now_list_turtle:
                            turtle_turn_3(a_2,b_2,c,d,j,1)
                            turtle_turn_3(a_7,b_7,c,d,j,1)
        elif c==simulate or c==simulate_2 or c==simulate_3 or c==simulate_4:
            if (a_2,b_2) in f(c) and (a_2,b_2,j) not in k(c):
                if (a_8,b_8) not in now_list and (a_3,b_3) not in now_list and (a_4,b_4) not in now_list and (a_5,b_5) not in now_list:
                    elist.append(4)
                    turtle_turn_3(a_3,b_3,c,d,j,1)
                    turtle_turn_3(a_4,b_4,c,d,j,1)
                    turtle_turn_3_1(a_0,b_0,c,d,j,1)
                    turtle_turn_3_1(a_5,b_5,c,d,j,1)
                    turtle_turn_3_1(a_8,b_8,c,d,j,1)
                    elist.clear()
            if (a_3,b_3) in f(c) and (a_3,b_3,j) not in k(c):
                if ((a_2,b_2) not in now_list and (a_4,b_4) not in now_list and (a_5,b_5) not in now_list) and ((a_8,b_8) not in now_list or (a_6,b_6) not in now_list):
                    elist.append(4)
                    if (a_8,b_8) in g(c)+edge:
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3_1(a_0,b_0,c,d,j,1)
                        turtle_turn_3_1(a_2,b_2,c,d,j,1)
                        turtle_turn_3_1(a_6,b_6,c,d,j,1)
                    elif (a_6,b_6) in g(c)+edge:
                        elist.append(4)
                        turtle_turn_3(a_2,b_2,c,d,j,1)
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3_1(a_0,b_0,c,d,j,1)
                        turtle_turn_3_1(a_5,b_5,c,d,j,1)
                        turtle_turn_3_1(a_8,b_8,c,d,j,1)
                    elif (a_8,b_8) not in now_list and (a_6,b_6) not in now_list:
                        turtle_turn_3(a_2,b_2,c,d,j,1)
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3_1(a_0,b_0,c,d,j,1)
                    elist.clear()
            if (a_4,b_4) in f(c) and (a_4,b_4,j) not in k(c):
                if ((a_3,b_3) not in now_list and (a_5,b_5) not in now_list):
                    if ((a_2,b_2) not in now_list and ((a_8,b_8) not in now_list or (a_6,b_6) not in now_list)) or ((a_6,b_6) not in now_list and ((a_2,b_2) not in now_list or (a_7,b_7) not in now_list)):
                        elist.append(4)
                        turtle_turn_3_1(a_0,b_0,c,d,j,1)
                        turtle_turn_3_1(a_3,b_3,c,d,j,1)
                        turtle_turn_3_1(a_5,b_5,c,d,j,1)
                        elist.clear()
                        if (a_2,b_2) not in now_list and ((a_8,b_8) not in now_list or (a_6,b_6) not in now_list):
                            if (a_8,b_8) in g(c)+edge:
                                turtle_turn_3(a_3,b_3,c,d,j,1)
                            elif (a_6,b_6) in g(c)+edge:
                                turtle_turn_3(a_2,b_2,c,d,j,1)
                                turtle_turn_3(a_3,b_3,c,d,j,1)
                            elif (a_8,b_8) not in now_list and (a_6,b_6) not in now_list:
                                turtle_turn_3(a_2,b_2,c,d,j,1)
                                turtle_turn_3(a_3,b_3,c,d,j,1)
                        if (a_6,b_6) not in now_list and ((a_2,b_2) not in now_list or (a_7,b_7) not in now_list):
                            if (a_2,b_2) in g(c)+edge:
                                turtle_turn_3(a_5,b_5,c,d,j,1)
                                turtle_turn_3(a_6,b_6,c,d,j,1)
                            elif (a_7,b_7) in g(c)+edge:
                                turtle_turn_3(a_5,b_5,c,d,j,1)
                            elif (a_2,b_2) not in now_list and (a_7,b_7) not in now_list:
                                turtle_turn_3(a_5,b_5,c,d,j,1)
                                turtle_turn_3(a_6,b_6,c,d,j,1)

            if (a_7,b_7) in f(c) and (a_7,b_7,j) not in k(c):
                if (a_9,b_9) not in now_list and (a_6,b_6) not in now_list and (a_5,b_5) not in now_list and (a_4,b_4) not in now_list:
                    elist.append(4)
                    turtle_turn_3(a_6,b_6,c,d,j,1)
                    turtle_turn_3(a_5,b_5,c,d,j,1)
                    turtle_turn_3_1(a_0,b_0,c,d,j,1)
                    turtle_turn_3_1(a_4,b_4,c,d,j,1)
                    turtle_turn_3_1(a_9,b_9,c,d,j,1)
            if (a_6,b_6) in f(c) and (a_6,b_6,j) not in k(c):
                if ((a_7,b_7) not in now_list and (a_5,b_5) not in now_list and (a_4,b_4) not in now_list) and ((a_9,b_9) not in now_list or (a_3,b_3) not in now_list):
                    if (a_9,b_9) in g(c)+edge:
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3_1(a_0,b_0,c,d,j,1)
                        turtle_turn_3_1(a_3,b_3,c,d,j,1)
                        turtle_turn_3_1(a_7,b_7,c,d,j,1)
                    elif (a_3,b_3) in g(c)+edge:
                        turtle_turn_3(a_7,b_7,c,d,j,1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3_1(a_0,b_0,c,d,j,1)
                        turtle_turn_3_1(a_4,b_4,c,d,j,1)       #여기할차례 (같은번호 중복이면 걸러내는 함수 만들기)
                        turtle_turn_3_1(a_9,b_9,c,d,j,1)
                    elif (a_9,b_9) not in now_list and (a_3,b_3) not in now_list:
                        turtle_turn_3(a_7,b_7,c,d,j,1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3_1(a_0,b_0,c,d,j,1)
            if (a_5,b_5) in f(c) and (a_5,b_5,j) not in k(c):
                if ((a_6,b_6) not in now_list and (a_4,b_4) not in now_list):
                    if ((a_7,b_7) not in now_list and ((a_9,b_9) not in now_list or (a_3,b_3) not in now_list)) or ((a_3,b_3) not in now_list and ((a_7,b_7) not in now_list or (a_2,b_2) not in now_list)):
                        elist.append(4)
                        turtle_turn_3_1(a_0,b_0,c,d,j,1)
                        turtle_turn_3_1(a_6,b_6,c,d,j,1)
                        turtle_turn_3_1(a_4,b_4,c,d,j,1)
                        elist.clear()
                        if (a_7,b_7) not in now_list and ((a_9,b_9) not in now_list or (a_3,b_3) not in now_list):
                            if (a_9,b_9) in g(c)+edge:
                                turtle_turn_3(a_6,b_6,c,d,j,1)
                            elif (a_3,b_3) in g(c)+edge:
                                turtle_turn_3(a_7,b_7,c,d,j,1)
                                turtle_turn_3(a_6,b_6,c,d,j,1)
                            elif (a_9,b_9) not in now_list and (a_3,b_3) not in now_list:
                                turtle_turn_3(a_7,b_7,c,d,j,1)
                                turtle_turn_3(a_7,b_7,c,d,j,1)
                                turtle_turn_3(a_6,b_6,c,d,j,1)
                        if (a_3,b_3) not in now_list and ((a_7,b_7) not in now_list or (a_2,b_2) not in now_list):
                            if (a_7,b_7) in g(c)+edge:
                                turtle_turn_3(a_4,b_4,c,d,j,1)
                                turtle_turn_3(a_3,b_3,c,d,j,1)
                            elif (a_2,b_2) in g(c)+edge:
                                turtle_turn_3(a_4,b_4,c,d,j,1)
                            elif (a_7,b_7) not in now_list and (a_2,b_2) not in now_list:
                                turtle_turn_3(a_4,b_4,c,d,j,1)
                                turtle_turn_3(a_3,b_3,c,d,j,1)
                        
    elif d==2:
        if e==1:
            if (a_1,b_1) in g(c) and (a_5,b_5) not in now_list and (a_6,b_6) not in now_list:
                if c==now_list_user:
                    if (a_4,b_4) in f(c)+edge and (a_7,b_7) not in now_list and (a_9,b_9) not in now_list:
                        elist.append(3)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3(a_6,b_6,c,d,j,1)
                        elist.clear()
                        turtle_turn_3(a_7,b_7,c,d,j,1)
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                    elif (a_7,b_7) in f(c)+edge and (a_4,b_4) not in now_list and (a_8,b_8) not in now_list:
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        elist.append(3)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3(a_6,b_6,c,d,j,1)
                        elist.clear()
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                    elif (a_4,b_4) not in now_list and (a_7,b_7) not in now_list:
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        elist.append(3)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3(a_6,b_6,c,d,j,1)
                        elist.clear()
                        turtle_turn_3(a_7,b_7,c,d,j,1)
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                elif c==now_list_turtle or c==simulate:
                    if (a_4,b_4) in f(c)+edge and (a_7,b_7) not in now_list and (a_9,b_9) not in now_list:
                        elist.append(3)
                        turtle_turn_3(a_6,b_6,c,d,j,1)
                        elist.clear()
                        turtle_turn_3(a_7,b_7,c,d,j,1)
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                    elif (a_7,b_7) in f(c)+edge and (a_4,b_4) not in now_list and (a_8,b_8) not in now_list:
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        elist.append(3)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        elist.clear()
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                    elif (a_4,b_4) not in now_list and (a_7,b_7) not in now_list:
                        if (a_8,b_8) in f(c)+edge and (a_9,b_9) not in now_list:
                            elist.append(3)
                            turtle_turn_3(a_5,b_5,c,d,j,1)
                            turtle_turn_3(a_6,b_6,c,d,j,1)
                            elist.clear()
                            turtle_turn_3(a_7,b_7,c,d,j,1)
                            turtle_turn_3(a_0,b_0,c,d,j,2)
                            turtle_turn_3(a_1,b_1,c,d,j,2)
                        elif (a_9,b_9) in f(c)+edge and (a_8,b_8) not in now_list:
                            turtle_turn_3(a_4,b_4,c,d,j,1)
                            elist.append(3)
                            turtle_turn_3(a_5,b_5,c,d,j,1)
                            turtle_turn_3(a_6,b_6,c,d,j,1)
                            elist.clear()
                            turtle_turn_3(a_0,b_0,c,d,j,2)
                            turtle_turn_3(a_1,b_1,c,d,j,2)
                        elif (a_8,b_8) not in now_list and (a_9,b_9) not in now_list:
                            turtle_turn_3(a_4,b_4,c,d,j,1)
                            elist.append(3)
                            turtle_turn_3(a_5,b_5,c,d,j,1)
                            turtle_turn_3(a_6,b_6,c,d,j,1)
                            elist.clear()
                            turtle_turn_3(a_7,b_7,c,d,j,1)
                            turtle_turn_3(a_0,b_0,c,d,j,2)
                            turtle_turn_3(a_1,b_1,c,d,j,2)
                        
        elif e==2:
            if ((a_1,b_1) in g(c) and (a_5,b_5) not in now_list and (a_4,b_4) not in now_list and (a_6,b_6) not in now_list) and ((a_8,b_8) not in now_list or (a_9,b_9) not in now_list):
                if c==now_list_user:
                    if (a_8,b_8) in f(c)+edge:
                        turtle_turn_3(a_9,b_9,c,d,j,1)
                        elist.append(3)
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3(a_6,b_6,c,d,j,1)
                        elist.clear()
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                    elif (a_9,b_9) in f(c)+edge:
                        turtle_turn_3(a_8,b_8,c,d,j,1)
                        elist.append(3)
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3(a_6,b_6,c,d,j,1)
                        elist.clear()
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                    elif (a_8,b_8) not in now_list and (a_9,b_9) not in now_list:
                        turtle_turn_3(a_8,b_8,c,d,j,1)
                        turtle_turn_3(a_9,b_9,c,d,j,1)
                        elist.append(3)
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3(a_6,b_6,c,d,j,1)
                        elist.clear()
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                elif c==now_list_turtle or c==simulate:
                    if (a_8,b_8) in f(c)+edge:
                        turtle_turn_3(a_6,b_6,c,d,j,1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                    elif (a_9,b_9) in f(c)+edge:
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                    elif (a_8,b_8) not in now_list and (a_9,b_9) not in now_list:
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3(a_6,b_6,c,d,j,1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
        elif e==3:
            if (a_1,b_1) in g(c) and (a_4,b_4) not in now_list and (a_5,b_5) not in now_list and (a_6,b_6) not in now_list and (a_7,b_7) not in now_list:
                if c==now_list_user:
                    turtle_turn_3(a_4,b_4,c,d,j,1)
                    turtle_turn_3(a_5,b_5,c,d,j,1)
                    turtle_turn_3(a_6,b_6,c,d,j,1)
                    turtle_turn_3(a_7,b_7,c,d,j,1)
                    turtle_turn_3(a_0,b_0,c,d,j,2)
                    turtle_turn_3(a_1,b_1,c,d,j,2)
                elif c==now_list_turtle or c==simulate:
                    turtle_turn_3(a_5,b_5,c,d,j,1)
                    turtle_turn_3(a_6,b_6,c,d,j,1)
                    turtle_turn_3(a_0,b_0,c,d,j,2)
                    turtle_turn_3(a_1,b_1,c,d,j,2)
    elif d==3:
        if e==1:
            if ((a_1,b_1) in g(c) and (a_2,b_2) in g(c)) and ((a_4,b_4) not in now_list or (a_5,b_5) not in now_list):
                if c==now_list_user:
                    if (a_4,b_4) in f(c)+edge and (a_9,b_9) not in now_list:
                        elist.append(2)
                        turtle_turn_3(a_9,b_9,c,d,j,1)
                        elist.append(3)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        elist.remove(3)
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                        turtle_turn_3(a_2,b_2,c,d,j,2)
                        elist.clear()
                    elif (a_5,b_5) in f(c)+edge and (a_8,b_8) not in now_list:
                        elist.append(2)
                        turtle_turn_3(a_8,b_8,c,d,j,1)
                        elist.append(3)
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        elist.remove(3)
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                        turtle_turn_3(a_2,b_2,c,d,j,2)
                        elist.clear()
                    elif ((a_4,b_4) not in now_list and (a_5,b_5) not in now_list) and ((a_8,b_8) in f(c)+edge and (a_9,b_9) in f(c)+edge):
                        elist.append(2)
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                        turtle_turn_3(a_2,b_2,c,d,j,2)
                        elist.clear()
                    elif ((a_4,b_4) not in now_list and (a_5,b_5) not in now_list) and ((a_8,b_8) not in now_list or (a_9,b_9) not in now_list):
                        elist.append(1)
                        if (a_8,b_8) in f(c)+edge:
                            turtle_turn_3(a_9,b_9,c,d,j,1)
                            elist.append(3)
                            turtle_turn_3(a_4,b_4,c,d,j,1)
                            turtle_turn_3(a_5,b_5,c,d,j,1)
                            elist.remove(3)
                            turtle_turn_3(a_0,b_0,c,d,j,2)
                            turtle_turn_3(a_1,b_1,c,d,j,2)
                            turtle_turn_3(a_2,b_2,c,d,j,2)
                        elif (a_9,b_9) in f(c)+edge:
                            turtle_turn_3(a_8,b_8,c,d,j,1)
                            elist.append(3)
                            turtle_turn_3(a_4,b_4,c,d,j,1)
                            turtle_turn_3(a_5,b_5,c,d,j,1)
                            elist.remove(3)
                            turtle_turn_3(a_0,b_0,c,d,j,2)
                            turtle_turn_3(a_1,b_1,c,d,j,2)
                            turtle_turn_3(a_2,b_2,c,d,j,2)
                        elif (a_8,b_8) not in now_list and (a_9,b_9) not in now_list:
                            elist.append(3)
                            turtle_turn_3(a_4,b_4,c,d,j,1)
                            turtle_turn_3(a_5,b_5,c,d,j,1)
                            elist.remove(3)
                            turtle_turn_3(a_0,b_0,c,d,j,2)
                            turtle_turn_3(a_1,b_1,c,d,j,2)
                            turtle_turn_3(a_2,b_2,c,d,j,2)
                        elist.clear()
                elif c==now_list_turtle or c==simulate:
                    if (a_4,b_4) in f(c)+edge and (a_9,b_9) not in now_list:
                        elist.append(2)
                        turtle_turn_3(a_9,b_9,c,d,j,1)
                        elist.append(3)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        elist.remove(3)
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                        turtle_turn_3(a_2,b_2,c,d,j,2)
                        elist.clear()
                    elif (a_5,b_5) in f(c)+edge and (a_8,b_8) not in now_list:
                        elist.append(2)
                        turtle_turn_3(a_8,b_8,c,d,j,1)
                        elist.append(3)
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        elist.remove(3)
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                        turtle_turn_3(a_2,b_2,c,d,j,2)
                        elist.clear()
                    elif ((a_4,b_4) not in now_list and (a_5,b_5) not in now_list) and ((a_8,b_8) in f(c)+edge and (a_9,b_9) in f(c)+edge):
                        elist.append(2)
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                        turtle_turn_3(a_2,b_2,c,d,j,2)
                        elist.clear()
                    elif ((a_4,b_4) not in now_list and (a_5,b_5) not in now_list) and ((a_8,b_8) not in now_list or (a_9,b_9) not in now_list):
                        if (a_8,b_8) in f(c)+edge:
                            elist.append(1)
                            turtle_turn_3(a_5,b_5,c,d,j,1)
                            turtle_turn_3(a_0,b_0,c,d,j,2)
                            turtle_turn_3(a_1,b_1,c,d,j,2)
                            turtle_turn_3(a_2,b_2,c,d,j,2)
                            elist.clear()
                            elist.append(2)
                            turtle_turn_3(a_4,b_4,c,d,j,1)
                            turtle_turn_3(a_9,b_9,c,d,j,1)
                            turtle_turn_3(a_0,b_0,c,d,j,2)
                            turtle_turn_3(a_1,b_1,c,d,j,2)
                            turtle_turn_3(a_2,b_2,c,d,j,2)
                            elist.clear()
                        elif (a_9,b_9) in f(c)+edge:
                            elist.append(1)
                            turtle_turn_3(a_4,b_4,c,d,j,1)
                            turtle_turn_3(a_0,b_0,c,d,j,2)
                            turtle_turn_3(a_1,b_1,c,d,j,2)
                            turtle_turn_3(a_2,b_2,c,d,j,2)
                            elist.clear()
                            elist.append(2)
                            turtle_turn_3(a_5,b_5,c,d,j,1)
                            turtle_turn_3(a_8,b_8,c,d,j,1)
                            turtle_turn_3(a_0,b_0,c,d,j,2)
                            turtle_turn_3(a_1,b_1,c,d,j,2)
                            turtle_turn_3(a_2,b_2,c,d,j,2)
                            elist.clear()
                        elif (a_8,b_8) not in now_list and (a_9,b_9) not in now_list:
                            elist.append(1)
                            turtle_turn_3(a_4,b_4,c,d,j,1)
                            turtle_turn_3(a_5,b_5,c,d,j,1)
                            turtle_turn_3(a_0,b_0,c,d,j,2)
                            turtle_turn_3(a_1,b_1,c,d,j,2)
                            turtle_turn_3(a_2,b_2,c,d,j,2)
                            elist.clear()
                            elist.append(2)
                            turtle_turn_3(a_8,b_8,c,d,j,1)
                            turtle_turn_3(a_9,b_9,c,d,j,1)
                            turtle_turn_3(a_0,b_0,c,d,j,2)
                            turtle_turn_3(a_1,b_1,c,d,j,2)
                            turtle_turn_3(a_2,b_2,c,d,j,2)
                            elist.clear()
        elif e==2:
            if ((a_1,b_1) in g(c) and (a_2,b_2) in g(c) and (a_5,b_5) not in now_list) and ((a_4,b_4) not in now_list or (a_6,b_6) not in now_list):
                if c==now_list_user:
                    if (a_4,b_4) in f(c)+edge:
                        elist.append(2)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3(a_6,b_6,c,d,j,1)
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                        turtle_turn_3(a_2,b_2,c,d,j,2)
                        elist.clear()
                    elif (a_6,b_6) in f(c)+edge:
                        elist.append(2)
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                        turtle_turn_3(a_2,b_2,c,d,j,2)
                        elist.clear()
                    elif (a_4,b_4) not in now_list and (a_6,b_6) not in now_list:
                        elist.append(1)
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3(a_6,b_6,c,d,j,1)
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                        turtle_turn_3(a_2,b_2,c,d,j,2)
                        elist.clear()
                elif c==now_list_turtle or c==simulate:
                    if (a_4,b_4) in f(c)+edge:
                        elist.append(2)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3(a_6,b_6,c,d,j,1)
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                        turtle_turn_3(a_2,b_2,c,d,j,2)
                        elist.clear()
                    elif (a_6,b_6) in f(c)+edge:
                        elist.append(2)
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                        turtle_turn_3(a_2,b_2,c,d,j,2)
                        elist.clear()
                    elif (a_4,b_4) not in now_list and (a_6,b_6) not in now_list:
                        elist.append(1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                        turtle_turn_3(a_2,b_2,c,d,j,2)
                        elist.clear()
                        elist.append(2)
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3(a_6,b_6,c,d,j,1)
                        turtle_turn_3(a_0,b_0,c,d,j,2)
                        turtle_turn_3(a_1,b_1,c,d,j,2)
                        turtle_turn_3(a_2,b_2,c,d,j,2)
                        elist.clear()
        elif e==3:
            if (a_1,b_1) in g(c) and (a_2,b_2) in g(c) and (a_4,b_4) not in now_list and (a_5,b_5) not in now_list and (a_8,b_8) not in g(c)+edge and (a_9,b_9) not in g(c)+edge:
                if c==now_list_user:
                    elist.append(2)
                    turtle_turn_3(a_4,b_4,c,d,j,1)
                    turtle_turn_3(a_5,b_5,c,d,j,1)
                    turtle_turn_3(a_0,b_0,c,d,j,2)
                    turtle_turn_3(a_1,b_1,c,d,j,2)
                    turtle_turn_3(a_2,b_2,c,d,j,2)
                    elist.clear()
                elif c==now_list_turtle or c==simulate:
                    elist.append(2)
                    turtle_turn_3(a_4,b_4,c,d,j,1)
                    turtle_turn_3(a_5,b_5,c,d,j,1)
                    turtle_turn_3(a_0,b_0,c,d,j,2)
                    turtle_turn_3(a_1,b_1,c,d,j,2)
                    turtle_turn_3(a_2,b_2,c,d,j,2)
                    elist.clear()
    elif d==4:
        if e==1:
            if ((a_1,b_1) in g(c) and (a_2,b_2) in g(c) and (a_3,b_3) in g(c)) and ((a_4,b_4) not in now_list or (a_5,b_5) not in now_list):
                if c==now_list_user:
                    if (a_4,b_4) in f(c)+edge:
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                    elif (a_5,b_5) in f(c)+edge:
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                    elif (a_4,b_4) not in now_list and (a_5,b_5) not in now_list:
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                elif c==now_list_turtle:
                    if (a_4,b_4) in f(c)+edge:
                        turtle_turn_3(a_5,b_5,c,d,j,1)
                    elif (a_5,b_5) in f(c)+edge:
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                    elif (a_4,b_4) not in now_list and (a_5,b_5) not in now_list:
                        turtle_turn_3(a_4,b_4,c,d,j,1)
                        turtle_turn_3(a_5,b_5,c,d,j,1)
        elif e==2:
            if (a_1,b_1) in g(c) and (a_2,b_2) in g(c) and (a_3,b_3) in g(c) and (a_4,b_4) not in now_list:
                if (a_8,b_8) in g(c) or (a_9,b_9) in g(c):
                    elist.append(4)
                    turtle_turn_3(a_4,b_4,c,d,j,1)
                elif (a_8) not in g(c) or (a_9,b_9) not in g(c):
                    turtle_turn_3(a_4,b_4,c,d,j,1)
                elist.clear()
def turtle_turn_5(x_4,y_4):
    if x_4==y_4:
        for i in range(len(x_4)):
            if x_4.count(x_4[i])>=2 and x_4[i] not in ban_list:
                #print("now1")
                flist.append(x_4[i])
    else:
        for i in range(len(y_4)):
            if y_4[i] in x_4 and y_4[i] not in ban_list:
                #print("now2")
                flist.append(y_4[i])
    if len(flist)>=1:
        slist.clear()
        for i in range(len(flist)):
            slist.append(flist[i])
    flist.clear()
def turtle_turn_5_1(x_4,y_4):
    if c_1==2:
        for i in range(len(x_4)):
            if x_4==y_4 and x_4.count(x_4[i])>=2:
                if x_4==slist_6 or x_4==slist_7 or x_4==slist_9:
                    ban_list.append(x_4[i])
                    while x_4[i] in slist:
                        slist.remove(x_4[i])
                elif x_4==slist_13:
                    special_list.append(5)
                elif x_4==slist_14:
                    special_list.append(3)
            elif x_4!=y_4 and x_4[i] in y_4:
                if x_4==slist_6:
                    ban_list.append(y_4[i])
                    while x_4[i] in slist:
                        slist.remove(x_4[i])
                elif x_4==slist_13:
                    special_list.append(4)
                elif x_4==slist_7:
                    special_list.append(7)
    else:
        for i in range(len(x_4)):
            if x_4==y_4 and x_4.count(x_4[i])>=2:
                if x_4==slist_12 or x_4==slist_13 or x_4==slist_14:
                    ban_list_user.append(x_4[i])
                elif x_4==slist_7:
                    special_list.append(1)
                elif x_4==slist_9:
                    special_list.append(2)
            elif x_4!=y_4 and x_4[i] in y_4:
                if x_4==slist_12:
                    ban_list_user.append(x_4[i])
                elif x_4==slist_13:
                    special_list.append(4)
                elif x_4==slist_7:
                    special_list.append(7)
def turtle_turn_5_2(x_4,y_4):
    if x_4==silist or x_4==silist_3:
        for i in range(len(x_4)):
            if len(x_4)>1 and x_4[i] not in ban_list:
                flist.append(x_4[i])
        if len(flist)>=1:
            if x_4==silist:
                special_list.append(6)
            else:
                special_list.append(9)
            x_4.clear()
            for i in range(len(flist)):
                x_4.append(flist[i])
            flist.clear()
    elif x_4==silist_2 or x_4==silist_4:
        for i in range(len(x_4)):
            if len(x_4)>1 and x_4[i] not in ban_list_user:
                flist.append(x_4[i])
        if len (flist)>=1:
            if x_4==silist_2:
                special_list.append(8)
            else:
                special_list.append(10)
            x_4.clear()
            for i in range(len(flist)):
                x_4.append(flist[i])
            flist.clear()
def turtle_turn_5_3(x_4):
    if len(flist_3)<1:
        slist.clear()
        for i in range(len(x_4)):
            if x_4[i] not in ban_list:
                slist.append(x_4[i])
def turtle_turn_5_4(x_4):
    for i in range(len(x_4)):
        x_1=x_4[i]
        x_2=x_1[0]
        y_2=x_1[1]
        for j in range(1500):
            if x_4==slist_7 and (x_4[0],x_4[1],j) in slist_6+slist_9:
                while (x_2,y_2) in slist_6+slist_9:
                    x_4.remove((x_2,y_2))
            elif x_4==slist_5 and (x_4[0],x_4[1],j) in slist_5+slist_8:            
                while (x_2,y_2) in slist_5+slist_8:
                    x_4.remove((x_2,y_2))
def turtle_turn_6():
    insert_4(simulate)
    insert_3(simulate)
    insert_2(simulate)
    turtle_turn_5_1(slist_6,slist_6)
    turtle_turn_5_1(slist_7,slist_7)
    turtle_turn_5_1(slist_7,slist_9)
    turtle_turn_5_1(slist_9,slist_9)
    turtle_turn_5_1(slist_6,slist_9)
    turtle_turn_5_1(slist_12,slist_12)
    turtle_turn_5_1(slist_13,slist_13)
    turtle_turn_5_1(slist_13,slist_14)
    turtle_turn_5_1(slist_12,slist_14)
    turtle_turn_5_1(slist_14,slist_14)
    turtle_turn_5_4(slist_5)
    turtle_turn_5_4(slist_7)
    insert_1(simulate)
    insert_1(simulate_2)
    if c_1==1:
        insert_1(simulate_3)
    else:
        insert_1(simulate_4)
    turtle_turn_5_2(silist,slist_9)
    turtle_turn_5_2(silist_2,slist_8)
    turtle_turn_5_2(silist_3,slist_7)
    turtle_turn_5_2(silist_4,slist_5)
    #print("방어4:",slist_3)
    #print("공격3:",slist_6)
    #print("방어3:",slist_4)
    #print("공격2:",slist_7)
    #print("방어2:",slist_5)
    #print("막힌방어3:",slist_8)
    #print("막힌공격3:",slist_9)
    #print("special_list:",special_list)
    #print("silist:",silist)
    #print("silist_2:",silist_2)
    #print("silist_3:",silist_3)
    #print("silist_4:",silist_4)
    turtle_turn_5_3(slist_18)
    if 4 in slist_2:
        #print("최상위 상태:공격4")
        flist_3.append(1)
    turtle_turn_5_3(slist_3)
    if len(flist_3)<1 and len(slist)>=1:
        #print("최상위 상태:방어4")
        flist_3.append(1)
        turtle_turn_5(slist_3,slist_3)
        turtle_turn_5(slist_3,slist_8)
        turtle_turn_5(slist_3,slist_4)
        turtle_turn_5(slist_3,slist_6)
        turtle_turn_5(slist_3,slist_9)
        turtle_turn_5(slist_3,slist_5)
        turtle_turn_5(slist_3,slist_7)
        turtle_turn_5(slist_3,slist_15)
        turtle_turn_5(slist_3,slist_16)
        turtle_turn_5(slist_3,slist_10)
        turtle_turn_5(slist_3,slist_11)
        turtle_turn_5(slist_3,slist_19)
        turtle_turn_5(slist_3,slist_17)
    turtle_turn_5_3(slist_6)
    if len(flist_3)<1 and len(slist)>=1:
        #print("최상위 상태:공격3")
        flist_3.append(1)
        turtle_turn_5(slist_6,slist_6)
        turtle_turn_5(slist_6,slist_9)
        turtle_turn_5(slist_6,slist_7)
        turtle_turn_5(slist_6,slist_4)
        turtle_turn_5(slist_6,slist_5)
        turtle_turn_5(slist_6,silist)
        turtle_turn_5(slist_6,slist_15)
        turtle_turn_5(slist_6,slist_16)
        turtle_turn_5(slist_6,slist_10)
        turtle_turn_5(slist_6,slist_11)
        turtle_turn_5(slist_6,slist_8)
        turtle_turn_5(slist_6,slist_19)
        turtle_turn_5(slist_6,slist_17)
    if len(flist_3)<1 and 2 in special_list:
        #print("최상위 상태:(특수)막힌33 공격")
        flist_3.append(1)
        turtle_turn_5(slist_9,slist_9)
    if len(flist_3)<1 and 7 in special_list:
        #print("최상위 상태:(특수)공격2*막힌공격3")
        flist_3.append(1)
        turtle_turn_5(slist_7,slist_9)
    turtle_turn_5_3(slist_4)
    if len(flist_3)<1 and len(slist)>=1:
        #print("최상위 상태:방어3")
        flist_3.append(1)
        turtle_turn_5(slist_4,slist_4)
        turtle_turn_5(slist_4,slist_8)
        turtle_turn_5(slist_4,slist_5)
        turtle_turn_5(slist_4,silist_2)
        turtle_turn_5(slist_4,silist_4)
        turtle_turn_5(slist_4,silist)
        turtle_turn_5(slist_4,silist_3)
        turtle_turn_5(slist_4,slist_7)
        turtle_turn_5(slist_4,slist_15)
        turtle_turn_5(slist_4,slist_16)
        turtle_turn_5(slist_4,slist_10)
        turtle_turn_5(slist_4,slist_11)
        turtle_turn_5(slist_4,slist_19)
        turtle_turn_5(slist_4,slist_17)
    if len(flist_3)<1 and 3 in special_list:
        #print("최상위 상태:(특수)막힌33 방어")
        flist_3.append(1)
        turtle_turn_5(slist_14,slist_14)
    if len(flist_3)<1 and 4 in special_list:
        #print("최상위 상태:(특수)방어2*막힌방어3")
        flist_3.append(1)
        turtle_turn_5(slist_13,slist_14)
    if len(flist_3)<1 and 1 in special_list:
        #print("최상위 상태:(특수)22공격")
        flist_3.append(1)
        turtle_turn_5(slist_7,slist_7)
    turtle_turn_5_3(silist)
    if len(flist_3)<1 and len(slist)>=1:
        #print("최상위 상태:(특수)공격2*막힌공격3 시도")
        flist_3.append(1)
        turtle_turn_5(silist,silist)
        turtle_turn_5(silist,slist_9)
        turtle_turn_5(silist,silist_3)
        turtle_turn_5(silist,slist_7)
        turtle_turn_5(silist,slist_5)
        turtle_turn_5(silist,slist_16)
        turtle_turn_5(silist,slist_11)
        turtle_turn_5(silist,slist_10)
        turtle_turn_5(silist,silist_2)
        turtle_turn_5(silist,silist_4)
        turtle_turn_5(silist,slist_8)
        turtle_turn_5(silist,slist_19)
        turtle_turn_5(silist,slist_17)
    if len(flist_3)<1 and 5 in special_list:
        #print("최상위 상태:(특수)22방어")
        flist_3.append(1)
        turtle_turn_5(slist_13,slist_13)
    turtle_turn_5_3(silist_3)
    if len(flist_3)<1 and len(slist)>=1:
        #print("최상위 상태:(특수)22공격 시도")
        flist_3.append(1)
        turtle_turn_5(silist_3,slist_9)
        turtle_turn_5(silist_3,silist_3)
        turtle_turn_5(silist_3,slist_7)
        turtle_turn_5(silist_3,slist_5)
        turtle_turn_5(silist_3,slist_16)
        turtle_turn_5(silist_3,slist_11)
        turtle_turn_5(silist_3,slist_10)
        turtle_turn_5(silist_3,silist_2)
        turtle_turn_5(silist_3,silist_4)
        turtle_turn_5(silist_3,slist_8)
        turtle_turn_5(silist_3,slist_19)
        turtle_turn_5(silist_3,slist_17)
    turtle_turn_5_3(slist_7)
    if len(flist_3)<1 and len(slist)>=1:
        #print("최상위 상태:공격2")
        flist_3.append(1)
        turtle_turn_5(slist_7,slist_9)
        turtle_turn_5(slist_7,slist_7)
        turtle_turn_5(slist_7,slist_5)
        turtle_turn_5(slist_7,slist_16)
        turtle_turn_5(slist_7,slist_10)
        turtle_turn_5(slist_7,slist_11)
        turtle_turn_5(slist_7,slist_8)
        turtle_turn_5(slist_7,slist_19)
        turtle_turn_5(slist_7,slist_17)
    turtle_turn_5_3(slist_5)
    if len(flist_3)<1 and len(slist)>=1:
        #print("최상위 상태:방어2")
        flist_3.append(1)
        turtle_turn_5(slist_5,slist_8)
        turtle_turn_5(slist_5,slist_5)
        turtle_turn_5(slist_5,silist_2)
        turtle_turn_5(slist_5,silist_4)
        turtle_turn_5(slist_5,slist_16)
        turtle_turn_5(slist_5,slist_10)
        turtle_turn_5(slist_5,slist_11)
        turtle_turn_5(slist_5,slist_19)
        turtle_turn_5(slist_5,slist_17)
    turtle_turn_5_3(slist_8)
    if len(flist_3)<1 and len(slist)>=1:
        #print("최상위 상태:막힌방어3")
        flist_3.append(1)
        turtle_turn_5(slist_8,silist_2)
        turtle_turn_5(slist_8,silist_4)
        turtle_turn_5(slist_8,slist_8)
        turtle_turn_5(slist_8,slist_11)
        turtle_turn_5(slist_8,slist_10)
        turtle_turn_5(slist_8,slist_19)
        turtle_turn_5(slist_8,slist_17)
    turtle_turn_5_3(slist_11)
    if len(flist_3)<1 and len(slist)>=1:
        #print("최상위 상태:공격1")
        flist_3.append(1)
        turtle_turn_5(slist_11,slist_11)
        turtle_turn_5(slist_11,slist_10)
        turtle_turn_5(slist_11,slist_17)
    turtle_turn_5_3(slist_10)
    if len(flist_3)<1 and len(slist)>=1:
        #print("최상위 상태:방어1")
        flist_3.append(1)
        turtle_turn_5(slist_10,slist_10)
        turtle_turn_5(slist_10,slist_17)
    for i in range(len(ban_list)):
        x_1=ban_list
        x_2=x_1[i]
        x_3=xlist.index(x_2[0])
        x_4=ylist.index(x_2[1])
        ban_list_2.append((list[x_3],list_2[x_4]))
    print("거북이 금수 자리:",ban_list_2)
    for i in range(len(ban_list_user)):
        x_1=ban_list_user
        x_2=x_1[i]
        x_3=xlist.index(x_2[0])
        x_4=ylist.index(x_2[1])
        ban_list_user_2.append((list[x_3],list_2[x_4]))
    print("유저 금수 자리:",ban_list_user_2)                           
    slist_2.clear()
    slist_3.clear()
    slist_4.clear()
    slist_5.clear()
    slist_6.clear()
    slist_7.clear()
    slist_8.clear()
    slist_9.clear()
    slist_10.clear()
    slist_11.clear()
    slist_12.clear()
    slist_13.clear()
    slist_14.clear()
    slist_15.clear()
    slist_16.clear()
    slist_17.clear()
    slist_18.clear()
    slist_19.clear()
    slist_4_2.clear()
    slist_5_2.clear()
    slist_6_2.clear()
    slist_7_2.clear()
    slist_8_2.clear() 
    slist_9_2.clear()
    slist_12_2.clear()
    slist_13_2.clear()
    slist_14_2.clear()
    slist_4_3.clear()
    slist_5_3.clear()
    slist_6_3.clear()
    slist_7_3.clear()
    slist_8_3.clear() 
    slist_9_3.clear()
    slist_12_3.clear()
    slist_13_3.clear()
    slist_14_3.clear()
    silist.clear()
    silist_2.clear()
    silist_3.clear()
    silist_4.clear()
    ban_list.clear()
    ban_list_2.clear()
    ban_list_user.clear()
    ban_list_user_2.clear()
    special_list.clear()
    flist_3.clear()
def insert_1(c):
    for i in range(len(h(c))):
        x_1=h(c)[i]
        x_2=x_1[0]
        y_2=x_1[1]
        j=i+1
        if c==simulate or c==simulate_2 or c==simulate_3 or c==simulate_4:
            j=x_1[2]
        turtle_turn_4(x_2,y_2,0,0,x_2-90,y_2,x_2-60,y_2,x_2-30,y_2,x_2+30,y_2,x_2+60,y_2,x_2+90,y_2,x_2-120,y_2,x_2+120,y_2,c,1,0,j)
        turtle_turn_4(x_2,y_2,0,0,x_2,y_2-90,x_2,y_2-60,x_2,y_2-30,x_2,y_2+30,x_2,y_2+60,x_2,y_2+90,x_2,y_2-120,x_2,y_2+120,c,1,0,j)
        turtle_turn_4(x_2,y_2,0,0,x_2-90,y_2-90,x_2-60,y_2-60,x_2-30,y_2-30,x_2+30,y_2+30,x_2+60,y_2+60,x_2+90,y_2+90,x_2-120,y_2-120,x_2+120,y_2+120,c,1,0,j)
        turtle_turn_4(x_2,y_2,0,0,x_2-90,y_2+90,x_2-60,y_2+60,x_2-30,y_2+30,x_2+30,y_2-30,x_2+60,y_2-60,x_2+90,y_2-90,x_2-120,y_2+120,x_2+120,y_2-120,c,1,0,j)
def insert_2(c):
    for i in range(len(g(c))):
        x_1=g(c)[i]
        x_2=x_1[0]
        y_2=x_1[1]
        j=i+301
        turtle_turn_4(x_2,y_2,x_2+30,y_2,0,0,0,0,x_2-60,y_2,x_2-30,y_2,x_2+60,y_2,x_2+90,y_2,x_2-90,y_2,x_2+120,y_2,c,2,1,j)
        turtle_turn_4(x_2,y_2,x_2,y_2+30,0,0,0,0,x_2,y_2-60,x_2,y_2-30,x_2,y_2+60,x_2,y_2+90,x_2,y_2-90,x_2,y_2+120,c,2,1,j)
        turtle_turn_4(x_2,y_2,x_2+30,y_2+30,0,0,0,0,x_2-60,y_2-60,x_2-30,y_2-30,x_2+60,y_2+60,x_2+90,y_2+90,x_2-90,y_2-90,x_2+120,y_2+120,c,2,1,j)
        turtle_turn_4(x_2,y_2,x_2+30,y_2-30,0,0,0,0,x_2-60,y_2+60,x_2-30,y_2+30,x_2+60,y_2-60,x_2+90,y_2-90,x_2-90,y_2+90,x_2+120,y_2-120,c,2,1,j)
    
        turtle_turn_4(x_2,y_2,x_2+60,y_2,0,0,0,0,x_2-30,y_2,x_2+30,y_2,x_2+90,y_2,0,0,x_2-60,y_2,x_2+120,y_2,c,2,2,j)
        turtle_turn_4(x_2,y_2,x_2,y_2+60,0,0,0,0,x_2,y_2-30,x_2,y_2+30,x_2,y_2+90,0,0,x_2,y_2-60,x_2,y_2+120,c,2,2,j)
        turtle_turn_4(x_2,y_2,x_2+60,y_2+60,0,0,0,0,x_2-30,y_2-30,x_2+30,y_2+30,x_2+90,y_2+90,0,0,x_2-60,y_2-60,x_2+120,y_2+120,c,2,2,j)
        turtle_turn_4(x_2,y_2,x_2+60,y_2-60,0,0,0,0,x_2-30,y_2+30,x_2+30,y_2-30,x_2+90,y_2-90,0,0,x_2-60,y_2+60,x_2+120,y_2-120,c,2,2,j)

        turtle_turn_4(x_2,y_2,x_2+90,y_2,0,0,0,0,x_2-30,y_2,x_2+30,y_2,x_2+60,y_2,x_2+120,y_2,1,0,0,0,c,2,3,j)
        turtle_turn_4(x_2,y_2,x_2,y_2+90,0,0,0,0,x_2,y_2-30,x_2,y_2+30,x_2,y_2+60,x_2,y_2+120,1,0,0,0,c,2,3,j)
        turtle_turn_4(x_2,y_2,x_2+90,y_2+90,0,0,0,0,x_2-30,y_2-30,x_2+30,y_2+30,x_2+60,y_2+60,x_2+120,y_2+120,1,0,0,0,c,2,3,j)
        turtle_turn_4(x_2,y_2,x_2+90,y_2-90,0,0,0,0,x_2-30,y_2+30,x_2+30,y_2-30,x_2+60,y_2-60,x_2+120,y_2-120,1,0,0,0,c,2,3,j)

def insert_3(c):
    for i in range(len(g(c))):
        x_1=g(c)[i]
        x_2=x_1[0]
        y_2=x_1[1]
        j=i+601
        turtle_turn_4(x_2,y_2,x_2+30,y_2,x_2+60,y_2,0,0,x_2-30,y_2,x_2+90,y_2,0,0,0,0,x_2-60,y_2,x_2+120,y_2,c,3,1,j)
        turtle_turn_4(x_2,y_2,x_2,y_2+30,x_2,y_2+60,0,0,x_2,y_2-30,x_2,y_2+90,0,0,0,0,x_2,y_2-60,x_2,y_2+120,c,3,1,j)
        turtle_turn_4(x_2,y_2,x_2+30,y_2+30,x_2+60,y_2+60,0,0,x_2-30,y_2-30,x_2+90,y_2+90,0,0,0,0,x_2-60,y_2-60,x_2+120,y_2+120,c,3,1,j)
        turtle_turn_4(x_2,y_2,x_2+30,y_2-30,x_2+60,y_2-60,0,0,x_2-30,y_2+30,x_2+90,y_2-90,0,0,0,0,x_2-60,y_2+60,x_2+120,y_2-120,c,3,1,j)

        turtle_turn_4(x_2,y_2,x_2+30,y_2,x_2+90,y_2,0,0,x_2-30,y_2,x_2+60,y_2,x_2+120,y_2,0,0,1,0,0,0,c,3,2,j)
        turtle_turn_4(x_2,y_2,x_2,y_2+30,x_2,y_2+90,0,0,x_2,y_2-30,x_2,y_2+60,x_2,y_2+120,0,0,1,0,0,0,c,3,2,j)
        turtle_turn_4(x_2,y_2,x_2+30,y_2+30,x_2+90,y_2+90,0,0,x_2-30,y_2-30,x_2+60,y_2+60,x_2+120,y_2+120,0,0,1,0,0,0,c,3,2,j)
        turtle_turn_4(x_2,y_2,x_2+30,y_2-30,x_2+90,y_2-90,0,0,x_2-30,y_2+30,x_2+60,y_2-60,x_2+120,y_2-120,0,0,1,0,0,0,c,3,2,j)

        turtle_turn_4(x_2,y_2,x_2+60,y_2,x_2+90,y_2,0,0,x_2-30,y_2,x_2+30,y_2,x_2+120,y_2,0,0,1,0,0,0,c,3,2,j)
        turtle_turn_4(x_2,y_2,x_2,y_2+60,x_2,y_2+90,0,0,x_2,y_2-30,x_2,y_2+30,x_2,y_2+120,0,0,1,0,0,0,c,3,2,j)
        turtle_turn_4(x_2,y_2,x_2+60,y_2+60,x_2+90,y_2+90,0,0,x_2-30,y_2-30,x_2+30,y_2+30,x_2+120,y_2+120,0,0,1,0,0,0,c,3,2,j)
        turtle_turn_4(x_2,y_2,x_2+60,y_2-60,x_2+90,y_2-90,0,0,x_2-30,y_2+30,x_2+30,y_2-30,x_2+120,y_2-120,0,0,1,0,0,0,c,3,2,j)

        turtle_turn_4(x_2,y_2,x_2+30,y_2,x_2+120,y_2,0,0,x_2+60,y_2,x_2+90,y_2,0,0,0,0,x_2-30,y_2,x_2+150,y_2,c,3,3,j)
        turtle_turn_4(x_2,y_2,x_2,y_2+30,x_2,y_2+120,0,0,x_2,y_2+60,x_2,y_2+90,0,0,0,0,x_2,y_2-30,x_2,y_2+150,c,3,3,j)
        turtle_turn_4(x_2,y_2,x_2+30,y_2+30,x_2+120,y_2+120,0,0,x_2+60,y_2+60,x_2+90,y_2+90,0,0,0,0,x_2-30,y_2-30,x_2+150,y_2+150,c,3,3,j)
        turtle_turn_4(x_2,y_2,x_2+30,y_2-30,x_2+120,y_2-120,0,0,x_2+60,y_2-60,x_2+90,y_2-90,0,0,0,0,x_2-30,y_2+30,x_2+150,y_2-150,c,3,3,j)

        turtle_turn_4(x_2,y_2,x_2+60,y_2,x_2+120,y_2,0,0,x_2+30,y_2,x_2+90,y_2,0,0,0,0,x_2-30,y_2,x_2+150,y_2,c,3,3,j)
        turtle_turn_4(x_2,y_2,x_2,y_2+60,x_2,y_2+120,0,0,x_2,y_2+30,x_2,y_2+90,0,0,0,0,x_2,y_2-30,x_2,y_2+150,c,3,3,j)
        turtle_turn_4(x_2,y_2,x_2+60,y_2+60,x_2+120,y_2+120,0,0,x_2+30,y_2+30,x_2+90,y_2+90,0,0,0,0,x_2-30,y_2-30,x_2+150,y_2+150,c,3,3,j)
        turtle_turn_4(x_2,y_2,x_2+60,y_2-60,x_2+120,y_2-120,0,0,x_2+30,y_2-30,x_2+90,y_2-90,0,0,0,0,x_2-30,y_2+30,x_2+150,y_2-150,c,3,3,j)

        turtle_turn_4(x_2,y_2,x_2+90,y_2,x_2+120,y_2,0,0,x_2+30,y_2,x_2+60,y_2,0,0,0,0,x_2-30,y_2,x_2+150,y_2,c,3,3,j)
        turtle_turn_4(x_2,y_2,x_2,y_2+90,x_2,y_2+120,0,0,x_2,y_2+30,x_2,y_2+60,0,0,0,0,x_2,y_2-30,x_2,y_2+150,c,3,3,j)
        turtle_turn_4(x_2,y_2,x_2+90,y_2+90,x_2+120,y_2+120,0,0,x_2+30,y_2+30,x_2+60,y_2+60,0,0,0,0,x_2-30,y_2+30,x_2+150,y_2-150,c,3,3,j)
        turtle_turn_4(x_2,y_2,x_2+90,y_2-90,x_2+120,y_2-120,0,0,x_2+30,y_2-30,x_2+60,y_2-60,0,0,0,0,x_2-30,y_2+30,x_2+150,y_2-150,c,3,3,j)

def insert_4(c):
    for i in range(len(g(c))):
        x_1=g(c)[i]
        x_2=x_1[0]
        y_2=x_1[1]
        j=i+901
        turtle_turn_4(x_2,y_2,x_2+30,y_2,x_2+60,y_2,x_2+90,y_2,x_2-30,y_2,x_2+120,y_2,0,0,0,0,1,0,0,0,c,4,1,j)
        turtle_turn_4(x_2,y_2,x_2,y_2+30,x_2,y_2+60,x_2,y_2+90,x_2,y_2-30,x_2,y_2+120,0,0,0,0,1,0,0,0,c,4,1,j)
        turtle_turn_4(x_2,y_2,x_2+30,y_2+30,x_2+60,y_2+60,x_2+90,y_2+90,x_2-30,y_2-30,x_2+120,y_2+120,0,0,0,0,1,0,0,0,c,4,1,j)
        turtle_turn_4(x_2,y_2,x_2+30,y_2-30,x_2+60,y_2-60,x_2+90,y_2-90,x_2-30,y_2+30,x_2+120,y_2-120,0,0,0,0,1,0,0,0,c,4,1,j)

        turtle_turn_4(x_2,y_2,x_2+30,y_2,x_2+60,y_2,x_2+120,y_2,x_2+90,y_2,0,0,0,0,0,0,x_2-30,y_2,x_2+150,y_2,c,4,2,j)
        turtle_turn_4(x_2,y_2,x_2,y_2+30,x_2,y_2+60,x_2,y_2+120,x_2,y_2+90,0,0,0,0,0,0,x_2,y_2-30,x_2,y_2+150,c,4,2,j)
        turtle_turn_4(x_2,y_2,x_2+30,y_2+30,x_2+60,y_2+60,x_2+120,y_2+120,x_2+90,y_2+90,0,0,0,0,0,0,x_2-30,y_2-30,x_2+150,y_2+150,c,4,2,j)
        turtle_turn_4(x_2,y_2,x_2+30,y_2-30,x_2+60,y_2-60,x_2+120,y_2-120,x_2+90,y_2-90,0,0,0,0,0,0,x_2-30,y_2+30,x_2+150,y_2-150,c,4,2,j)

        turtle_turn_4(x_2,y_2,x_2+30,y_2,x_2+90,y_2,x_2+120,y_2,x_2+60,y_2,0,0,0,0,0,0,x_2-30,y_2,x_2+150,y_2,c,4,2,j)
        turtle_turn_4(x_2,y_2,x_2,y_2+30,x_2,y_2+90,x_2,y_2+120,x_2,y_2+60,0,0,0,0,0,0,x_2,y_2-30,x_2,y_2+150,c,4,2,j)
        turtle_turn_4(x_2,y_2,x_2+30,y_2+30,x_2+90,y_2+90,x_2+120,y_2+120,x_2+60,y_2+60,0,0,0,0,0,0,x_2-30,y_2-30,x_2+150,y_2+150,c,4,2,j)
        turtle_turn_4(x_2,y_2,x_2+30,y_2-30,x_2+90,y_2-90,x_2+120,y_2-120,x_2+60,y_2-60,0,0,0,0,0,0,x_2-30,y_2+30,x_2+150,y_2-150,c,4,2,j)

        turtle_turn_4(x_2,y_2,x_2+60,y_2,x_2+90,y_2,x_2+120,y_2,x_2+30,y_2,0,0,0,0,0,0,x_2-30,y_2,x_2+150,y_2,c,4,2,j)
        turtle_turn_4(x_2,y_2,x_2,y_2+60,x_2,y_2+90,x_2,y_2+120,x_2,y_2+30,0,0,0,0,0,0,x_2,y_2-30,x_2,y_2+150,c,4,2,j)
        turtle_turn_4(x_2,y_2,x_2+60,y_2+60,x_2+90,y_2+90,x_2+120,y_2+120,x_2+30,y_2+30,0,0,0,0,0,0,x_2-30,y_2-30,x_2+150,y_2+150,c,4,2,j)
        turtle_turn_4(x_2,y_2,x_2+60,y_2-60,x_2+90,y_2-90,x_2+120,y_2-120,x_2+30,y_2-30,0,0,0,0,0,0,x_2-30,y_2+30,x_2+150,y_2-150,c,4,2,j)
def turtle_turn():
    if len(now_list_user)==0:
        x=-30
        y=10
        turtle_turn_2(x,y)
        draw()
    elif len(now_list_user)>=1:
        insert_4(now_list_turtle)
        insert_4(now_list_user)
        insert_3(now_list_turtle)
        insert_3(now_list_user)
        insert_2(now_list_turtle)
        insert_2(now_list_user)
        insert_1(now_list_user)
        insert_1(now_list_turtle)
        turtle_turn_6()
        #print("최종리스트:",slist)
        print("------------------------------------------------------------------------")
        x_3=random.choice(slist)
        x=x_3[0]
        y=x_3[1]
        turtle_turn_2(x,y)
        draw()
        slist.clear()
def end(b,c,d,e):            
    if len(set(b))>=1 and len(set(c))>=1:                          
        for i in range(0,len(d)-4,1):
            a=d[i]
            r=e[i]
            if (((a[0]+30,a[1]+30)) in d and ((a[0]+60,a[1]+60)) in d and ((a[0]+90,a[1]+90)) in d and ((a[0]+120,a[1]+120))) in d:
                f_1.append(1)
                break
            elif (((a[0]+30,a[1]-30)) in d and ((a[0]+60,a[1]-60)) in d and ((a[0]+90,a[1]-90)) in d and ((a[0]+120,a[1]-120))) in d:
                f_1.append(1)
                break
            elif (((a[0]+30,a[1])) in d and ((a[0]+60,a[1])) in d and ((a[0]+90,a[1])) in d and ((a[0]+120,a[1]))) in d:
                f_1.append(1)
                break
            elif (((r[0]+30,r[1])) in e and ((r[0]+60,r[1])) in e and ((r[0]+90,r[1])) in e and ((r[0]+120,r[1]))) in e:
                f_1.append(1)
                break
            else:
                f_1.append(0)
    else:
        f_1.append(0)
t.speed(5)
for i in range(15):
    edge.append((xlist[i],ylist[0]+30))
    edge.append((xlist[i],ylist[14]-30))
    edge.append((xlist[0]-30,ylist[i]))
    edge.append((xlist[14]+30,ylist[i]))
now_list=now_list+edge
if c_1==1:
    while 1 not in f_1:
        user_turn()
        end(now_list_x_user,now_list_y_user,now_list_user,reverse_list_user)
        if 1 in f_1:
            print("당신의 승리입니다")
            break
        turtle_turn()
        end(now_list_x_turtle,now_list_y_turtle,now_list_turtle,reverse_list_turtle)
        if 1 in f_1:
            print("거북이의 승리입니다")
            break      
else:
    while 1 not in f_1:
        turtle_turn()
        end(now_list_x_turtle,now_list_y_turtle,now_list_turtle,reverse_list_turtle)
        if 1 in f_1:
            print("거북이의 승리입니다")
            break
        user_turn()
        end(now_list_x_user,now_list_y_user,now_list_user,reverse_list_user)
        if 1 in f_1:
            print("당신의 승리입니다")
            break






