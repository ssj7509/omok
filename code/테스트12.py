import turtle
import random
t=turtle.Turtle()
t.shape("turtle")
list_1=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
list_2=[]
for i in range(15):
    list_2.append(i+1)
ps=30;  cs=13
boardx=-270;  boardy=220;
set_boardx=0;  set_boardy=0;
t.up()
t.speed(0)
t.goto(boardx+set_boardx,boardy+set_boardy)
for i in range(1,16,1):                    
    t.write(i)
    t.down()
    t.fd(ps*16)
    t.write(i)
    t.up()
    t.backward(ps*16)
    t.right(90)
    t.fd(ps)
    t.left(90)
t.right(90)
t.goto(boardx+set_boardx+ps,boardy+set_boardy+ps)
for i in range(1,16,1):
    t.write(list_1[i-1])
    t.down()
    t.fd(ps*16)
    t.write(list_1[i-1])
    t.up()
    t.backward(ps*16)
    t.left(90)
    t.fd(ps)
    t.right(90)
t.goto(-290,-260)
t.left(90)

xlist=[];  ylist=[]
for i in range(0,15,1):                             
    xlist.append(boardx+set_boardx+ps*(i+1))
    ylist.append(boardy+set_boardy-ps*i)

now_list=[];  now_list_user=[];  now_list_turtle=[]
not_now_list=[];
edge=[]
for i in range(16):
    edge.append((boardx+set_boardx+ps*i,boardy+set_boardy+ps))
    edge.append((boardx+set_boardx+ps*(i+1),boardy+set_boardy-ps*15))
    edge.append((boardx+set_boardx,boardy+set_boardy-ps*i))
    edge.append((boardx+set_boardx+ps*16,boardy+set_boardy-ps*(i-1)))
now_list+=edge

ban_list=[];  ban_list_user=[];  ban_list_turtle=[]
elist=[]; tlist=[]; tlist_2=[]; plist=[]
turn_type=[1,2,3,4,5,6,7];  special_type=[];
final_list=[];

o_d_1=[]; o_d_2=[]; o_d_3=[]; o_d_4=[]
o_a_1=[]; o_a_2=[]; o_a_3=[]; o_a_4=[]
c_d_2=[]; c_d_3=[]; c_a_2=[]; c_a_3=[]
l_o_d_1_1=[]; l_o_d_1_2=[] 
l_o_d_2_1=[]; l_o_d_2_2=[]
l_o_a_2=[]; l_c_d_3=[]; l_o_d_3=[]
b_o_d_2=[]; b_o_d_3=[]; b_c_d_3=[]
o_d_2_2=[]; o_d_3_2=[]; o_a_2_2=[]; o_a_3_2=[]
c_d_2_2=[]; c_d_3_2=[] ;c_a_2_2=[]; c_a_3_2=[]
o_d_2_3=[]; o_d_3_3=[]; o_a_2_3=[]; o_a_3_3=[]
c_d_2_3=[]; c_d_3_3=[] ;c_a_2_3=[]; c_a_3_3=[]
t_a_23=[];  t_d_23=[]; t_a_22=[]; t_d_22=[]
t_a_H_Lv1=[]; t_a_H_Lv2=[]; t_d_H_Lv1=[]; t_d_H_Lv2=[]
t_a_i_Lv1=[]; t_a_i_Lv2=[]; t_d_i_Lv1=[]; t_d_i_Lv2=[]

while True:
    first=input("먼저 하시겠습니까?(1:예 2:아니요):")
    if first in ['1','2']:
        break
    print("다시 입력해주세요:")

def draw():
    t.down()
    t.begin_fill()
    t.circle(cs)
    t.up()
    t.end_fill()
def f(ty):
    if ty in [1,3,5]:
        return now_list_turtle
    elif ty in [2,4,6]:
        return now_list_user
def g(ty):
    if ty in [1,3,5]:
        return now_list_user
    elif ty in [2,4,6]:
        return now_list_turtle
def h(ty):
    if ty==1:
        return now_list_user
    elif ty==2:
        return now_list_turtle
    elif ty==3:
        return c_a_3_2
    elif ty==4:
        return c_d_3_2
    elif ty==5:
        return o_a_2_2
    elif ty==6:
        return o_d_2_2
def k(ty):
    if ty==1:
        return now_list_user
    elif ty==2:
        return now_list_turtle
    elif ty==3:
        return c_a_3_3
    elif ty==4:
        return c_d_3_3
    elif ty==5:
        return o_a_2_3
    elif ty==6:
        return o_d_2_3
def spoint(ty,T):
    if ((first==1 and ty in [1,4,6]) or (first==2 and ty in [2,3,5,7])):
        if T in f(ty)+edge:
            return True
    else:
        if T in now_list:
            return True
    return False
def endline(ty,T):
    if ((first==1 and ty in [1,4,6]) or (first==2 and ty in [2,3,5,7])) and T in g(ty):
        return False
    else:
        return True
def inlist(L_1,L_2):
    for i in range(len(L_1)):
        count=0
        for j in range(len(L_2)):
            if L_1[i] in list_2[j]:
                count+=1
        if count==0:
            return False
    return True
def notlist(L_1,L_2):
    for i in range(len(L_2)):
        if L_2[i] in L_1:
            return False
    return True
def turtle_turn():
    def goto_point(x,y):
        t.goto(x,y-ps/2)
        t.fillcolor("yellow")
        now_list.append((x,y))
        now_list_turtle.append((x,y))
        now_list.sort()
        now_list_turtle.sort()
    def classify_list(T,ty,nt,idn,tt):
        if T[0]>=boardx+ps and T[0]<=boardx+15*ps and T[1]>=boardy-14*ps and T[1]<=boardy and ((T not in now_list) or (tt==2)):
            if nt==1:
                if ty==1:
                    o_d_1.append(T)
                    if 3 in elist:
                        l_o_d_1_1.append(T)
                    elif 4 in elist:
                        l_o_d_1_2.append(T)
                elif ty==2:
                    o_a_1.append(T)   
                elif ty in [3,4,5,6] and (T[0],T[1],idn) not in h(ty):
                    if ty==3:
                        t_a_23.append(T)
                    elif ty==4:
                        t_d_23.append(T)
                    elif ty==5:
                        t_a_22.append(T)
                    elif ty==6:
                        t_d_22.append(T)
            elif nt==2:
                if ty==1:
                    if 1 in elist:
                        if tt==1:
                            if 3 in elist:
                                l_o_d_2_1.append(T)
                            elif 4 in elist:
                                l_o_d_2_2.append(T)
                            o_d_2.append(T)
                            o_d_2_2.append((T[0],T[1],idn))
                        elif tt==2:
                            o_d_2_3.append((T[0],T[1],idn))
                    elif 2 in elist:
                        if tt==1:
                            c_d_2.append(T)
                            c_d_2_2.append((T[0],T[1],idn))
                        elif tt==2:
                            c_d_2_3.append((T[0],T[1],idn))
                elif ty==2:
                    if 1 in elist:
                        if tt==1:
                            if 3 in elist:
                                l_o_a_2.append(T)
                            o_a_2.append(T)
                            o_a_2_2.append((T[0],T[1],idn))
                        elif tt==2:
                            o_a_2_3.append((T[0],T[1],idn))
                    elif 2 in elist:
                        if tt==1:
                            c_a_2.append(T)
                            c_a_2_2.append((T[0],T[1],idn))
                        elif tt==2:
                            c_a_2_3.append((T[0],T[1],idn))
                elif ty==7:
                    if 1 in elist:
                        b_o_d_2.append(T)
            elif nt==3:
                if ty==1:
                    if 1 in elist:
                        if tt==1:
                            if 3 in elist:
                                l_o_d_3.append(T)
                            o_d_3.append(T)
                            o_d_3_2.append((T[0],T[1],idn))
                        elif tt==2:
                            o_d_3_3.append((T[0],T[1],idn))
                    elif 2 in elist:
                        if tt==1:
                            if 3 in elist:
                                l_c_d_3.append(T)
                            c_d_3.append(T)
                            c_d_3_2.append((T[0],T[1],idn))
                        elif tt==2:
                            c_d_3_3.append((T[0],T[1],idn))
                elif ty==2:
                    if 1 in elist:
                        if tt==1:
                            o_a_3.append(T)
                            o_a_3_2.append((T[0],T[1],idn))
                        elif tt==2:
                            o_a_3_3.append((T[0],T[1],idn))
                    elif 2 in elist:
                        if tt==1:
                            c_a_3.append(T)
                            c_a_3_2.append((T[0],T[1],idn))
                        elif tt==2:
                            c_a_3_3.append((T[0],T[1],idn))
                elif ty==7:
                    if 1 in elist:
                        if tt==1:
                            b_o_d_3.append(T)
                    elif 2 in elist:
                        if tt==1:
                            b_c_d_3.append(T)
            elif nt==4:
                if ty==1:
                    o_d_4.append(T)
                elif ty==2:
                    o_a_4.append(T)
    def special_classify(L,ty,idn):
        pass
    def logical_f(L,ty,nt,ft,idn):
        if nt==1:
            if notlist([L[1],L[2]],now_list):
                if spoint(ty,L[3]) and notlist([L[4],L[6],L[8]],now_list) and endline(ty,L[10]):
                    if ty==1:
                        classify_list(L[1],ty,nt,idn,1)
                    classify_list(L[6],ty,nt,idn,1)
                    elist.append(4)
                    classify_list(L[4],ty,nt,idn,1)
                    elist.append(3)
                    classify_list(L[2],ty,nt,idn,1)
                    elist.clear()
                elif spoint(ty,L[4]) and notlist([L[3],L[5],L[7]],now_list) and endline(ty,L[9]):
                    if ty==1:
                        classify_list(L[2],ty,nt,idn,1)
                    classify_list(L[5],ty,nt,idn,1)
                    elist.append(4)
                    classify_list(L[3],ty,nt,idn,1)
                    elist.append(3)
                    classify_list(L[1],ty,nt,idn,1)
                    elist.clear()
                elif notlist([L[3],L[4]],now_list):
                    if spoint(ty,L[5]) and notlist([L[6]],now_list) and endline(ty,L[8]):
                        if ty==1:
                            classify_list(L[3],ty,nt,idn,1)
                        elist.append(4)
                        classify_list(L[1],ty,nt,idn,1)
                        classify_list(L[4],ty,nt,idn,1)
                        elist.append(3)
                        classify_list(L[2],ty,nt,idn,1)
                        elist.clear()
                        if (spoint(ty,L[8]) and ty==1) or (notlist([L[8]],now_list) and endline(ty,L[10])):
                            classify_list(L[6],ty,nt,idn,1)
                    elif spoint(ty,L[6]) and notlist([L[5]],now_list) and endline(ty,L[7]):
                        if ty==1:
                            classify_list(L[4],ty,nt,idn,1)
                        elist.append(4)
                        classify_list(L[2],ty,nt,idn,1)
                        classify_list(L[3],ty,nt,idn,1)
                        elist.append(3)
                        classify_list(L[1],ty,nt,idn,1)
                        elist.clear()
                        if (spoint(ty,L[7]) and ty==1) or (notlist([L[7]],now_list) and endline(ty,L[9])):
                            classify_list(L[5],ty,nt,idn,1)
                    elif notlist([L[5],L[6]],now_list):
                        classify_list(L[3],ty,nt,idn,1)
                        classify_list(L[4],ty,nt,idn,1)
                        elist.append(3)
                        classify_list(L[1],ty,nt,idn,1)
                        classify_list(L[2],ty,nt,idn,1)
                        elist.clear()
                        if ty==2:
                            if notlist([L[8]],now_list):
                                classify_list(L[6],ty,nt,idn,1)
                            if notlist([L[7]],now_list):
                                classify_list(L[5],ty,nt,idn,1)
        elif nt==2:
            if ft==1:
                if L[2] in g(ty):
                    if L[1] in f(ty)+edge and notlist([L[4],L[6],L[8]],now_list) and endline(ty,L[10]):
                        elist.append(2)
                        classify_list(L[4],ty,nt,idn,1)
                        classify_list(L[6],ty,nt,idn,1)
                        classify_list(L[8],ty,nt,idn,1)
                        elist.clear()
                    elif L[4] in f(ty)+edge and notlist([L[1],L[3],L[5]],now_list) and endline(ty,L[7]):
                        elist.append(2)
                        classify_list(L[1],ty,nt,idn,1)
                        classify_list(L[3],ty,nt,idn,1)
                        classify_list(L[5],ty,nt,idn,1)
                        elist.clear()
                    elif spoint(ty,L[3]) and notlist([L[1],L[4],L[6]],now_list):
                        if spoint(ty,L[8]):
                            elist.append(2)
                            classify_list(L[1],ty,nt,idn,1)
                            classify_list(L[4],ty,nt,idn,1)
                            classify_list(L[6],ty,nt,idn,1)
                            elist.clear()
                        elif notlist([L[8]],now_list) and endline(ty,L[10]):
                            elist.append(1)
                            if ty==1:
                                classify_list(L[1],ty,nt,idn,1)
                                classify_list(L[8],ty,nt,idn,1)
                            elist.append(4)
                            classify_list(L[6],ty,nt,idn,1)
                            elist.append(3)
                            classify_list(L[4],ty,nt,idn,1)
                            elist.clear()
                    elif spoint(ty,L[6]) and notlist([L[1],L[3],L[4]],now_list):
                        if spoint(ty,L[5]):
                            elist.append(2)
                            classify_list(L[1],ty,nt,idn,1)
                            classify_list(L[3],ty,nt,idn,1)
                            classify_list(L[4],ty,nt,idn,1)
                            elist.clear()
                        elif notlist([L[5]],now_list) and endline(ty,L[7]):
                            elist.append(1)
                            if ty==1:
                                classify_list(L[4],ty,nt,idn,1)
                                classify_list(L[5],ty,nt,idn,1)
                            elist.append(4)
                            classify_list(L[3],ty,nt,idn,1)
                            elist.append(3)
                            classify_list(L[1],ty,nt,idn,1)
                            elist.clear()
                    elif notlist([L[1],L[3],L[4],L[6]],now_list):
                        if spoint(ty,L[5]):
                            if spoint(ty,L[3]):
                                elist.append(1)
                                if ty==1:
                                    classify_list(L[3],ty,nt,idn,1)
                                    classify_list(L[6],ty,nt,idn,1)
                                elist.append(3)
                                classify_list(L[1],ty,nt,idn,1)
                                classify_list(L[4],ty,nt,idn,1)
                                elist.clear()
                            elif notlist([L[8]],now_list) and endline(ty,L[10]):
                                elist.append(1)
                                if ty==1:
                                    classify_list(L[3],ty,nt,idn,1)
                                elist.append(4)
                                classify_list(L[6],ty,nt,idn,1)
                                if ty==2:
                                    elist.append(3)
                                classify_list(L[1],ty,nt,idn,1)
                                elist.append(3)
                                classify_list(L[4],ty,nt,idn,1)
                                elist.clear()
                        elif spoint(ty,L[8]) and notlist([L[5]],now_list) and endline(ty,L[7]):
                            elist.append(1)
                            if ty==1:
                                classify_list(L[6],ty,nt,idn,1)
                            elist.append(4)
                            classify_list(L[3],ty,nt,idn,1)
                            if ty==2:
                                elist.append(3)
                            classify_list(L[4],ty,nt,idn,1)
                            elist.append(3)
                            classify_list(L[1],ty,nt,idn,1)
                            elist.clear()
                        elif notlist([L[5],L[8]],now_list):
                            elist.append(1)
                            if ty==1:
                                classify_list(L[3],ty,nt,idn,1)
                                classify_list(L[6],ty,nt,idn,1)
                            elif ty==2:
                                if endline(ty,L[10]):
                                    classify_list(L[6],ty,nt,idn,1)
                                if endline(ty,L[7]):
                                    classify_list(L[3],ty,nt,idn,1)
                            elist.append(3)
                            classify_list(L[1],ty,nt,idn,1)
                            classify_list(L[4],ty,nt,idn,1)
                            elist.clear()  
            elif ft==2:
                if L[4] in g(ty) and notlist([L[2]],now_list):
                    if L[1] in f(ty)+edge and notlist([L[6],L[8]],now_list) and endline(ty,L[10]):
                        elist.append(2)
                        classify_list(L[2],ty,nt,idn,1)
                        classify_list(L[6],ty,nt,idn,1)
                        classify_list(L[8],ty,nt,idn,1)
                        elist.clear()
                    elif L[6] in f(ty)+edge and notlist([L[1],L[3]],now_list) and endline(ty,L[5]):
                        elist.append(2)
                        classify_list(L[1],ty,nt,idn,1)
                        classify_list(L[2],ty,nt,idn,1)
                        classify_list(L[3],ty,nt,idn,1)
                        elist.clear()
                    elif notlist([L[1],L[6]],now_list):
                        if spoint(ty,L[3]):
                            if spoint(ty,L[8]):
                                elist.append(2)
                                classify_list(L[1],ty,nt,idn,1)
                                classify_list(L[2],ty,nt,idn,1)
                                classify_list(L[6],ty,nt,idn,1)
                                elist.clear()
                            elif notlist([L[8]],now_list) and endline(ty,L[10]):
                                elist.append(1)
                                if ty==1:
                                    classify_list(L[1],ty,nt,idn,1)
                                    classify_list(L[8],ty,nt,idn,1)
                                elist.append(4)
                                classify_list(L[6],ty,nt,idn,1)
                                elist.append(3)
                                classify_list(L[2],ty,nt,idn,1)
                                elist.clear()
                        elif spoint(ty,L[8]) and notlist([L[3]],now_list) and endline(ty,L[5]):
                            elist.append(1)
                            if ty==1:
                                classify_list(L[3],ty,nt,idn,1)
                                classify_list(L[6],ty,nt,idn,1)
                            elist.append(4)
                            classify_list(L[1],ty,nt,idn,1)
                            elist.append(3)
                            classify_list(L[2],ty,nt,idn,1)
                            elist.clear()
                        elif notlist([L[3],L[8]],now_list) and (endline(ty,L[5]) or endline(ty,L[10])):
                            elist.append(1)
                            if ty==1:
                                classify_list(L[3],ty,nt,idn,1)
                                classify_list(L[8],ty,nt,idn,1)
                            elist.append(4)
                            if endline(ty,L[5]):
                                classify_list(L[1],ty,nt,idn,1)
                            if endline(ty,L[10]):
                                classify_list(L[6],ty,nt,idn,1)
                            elist.append(3)
                            classify_list(L[2],ty,nt,idn,1)
                            elist.clear()
            # spoint 계속하기
            elif ft==3:
                if L[6] in g(ty) and notlist([L[2],L[4]],now_list):
                    if L[1] in f(ty)+edge and notlist([L[8]],now_list) and endline(ty,L[10]):
                        elist.append(2)
                        classify_list(L[2],ty,nt,idn,1)
                        classify_list(L[4],ty,nt,idn,1)
                        classify_list(L[8],ty,nt,idn,1)
                        elist.clear()
                    elif L[8] in f(ty)+edge and notlist([L[1]],now_list) and endline(ty,L[3]):
                        elist.append(2)
                        classify_list(L[1],ty,nt,idn,1)
                        classify_list(L[2],ty,nt,idn,1)
                        classify_list(L[4],ty,nt,idn,1)
                    elif notlist([L[1],L[8]],now_list) and (endline(ty,L[3]) or endline(ty,L[10])):
                        elist.append(1)
                        if ty==1:
                            if endline(ty,L[3]):
                                classify_list(L[1],ty,nt,idn,1)
                            if endline(ty,L[10]):
                                classify_list(L[8],ty,nt,idn,1)
                        elist.append(3)
                        classify_list(L[2],ty,nt,idn,1)
                        classify_list(L[4],ty,nt,idn,1)
                        elist.clear()
            elif ft==4:
                if L[8] in g(ty) and notlist([L[2],L[4],L[6]],now_list) and endline(ty,L[1]) and endline(ty,L[10]):
                    elist.append(2)
                    classify_list(L[2],ty,nt,idn,1)
                    classify_list(L[4],ty,nt,idn,1)
                    classify_list(L[6],ty,nt,idn,1)
                    elist.clear()
        elif nt==3:
            if ft==1:
                if inlist([L[2],L[4]],g(ty)):
                    if L[1] in f(ty)+edge and notlist([L[6],L[8]],now_list) and endline(ty,L[10]):
                        elist.append(2)
                        classify_list(L[8],ty,nt,idn,1)
                        elist.append(3)
                        classify_list(L[6],ty,nt,idn,1)
                        elist.clear()
                    elif L[6] in f(ty)+edge and notlist([L[1],L[3]],now_list) and endline(ty,L[5]):
                        elist.append(2)
                        classify_list(L[3],ty,nt,idn,1)
                        elist.append(3)
                        classify_list(L[1],ty,nt,idn,1)
                        elist.clear()
                    elif notlist([L[1],L[6]],now_list):
                        if L[3] in f(ty)+edge:
                            if L[8] in f(ty)+edge:
                                elist.append(2)
                                classify_list(L[1],ty,nt,idn,1)
                                classify_list(L[6],ty,nt,idn,1)
                                elist.clear()
                            elif notlist([L[8]],now_list) and endline(ty,L[10]):
                                elist.append(1)
                                if ty==1:
                                    classify_list(L[1],ty,nt,idn,1)
                                    classify_list(L[8],ty,nt,idn,1)
                                    elist.append(3)
                                classify_list(L[6],ty,nt,idn,1)
                                elist.clear()
                        elif L[8] in f(ty)+edge and notlist([L[3]],now_list) and endline(ty,L[5]):
                            elist.append(1)
                            if ty==1:
                                classify_list(L[3],ty,nt,idn,1)
                                classify_list(L[6],ty,nt,idn,1)
                                elist.append(3)
                            classify_list(L[1],ty,nt,idn,1)
                            elist.clear()
                        elif notlist([L[3],L[8]],now_list) and (endline(ty,L[5]) or endline(ty,L[10])):
                            elist.append(1)
                            if not endline(ty,L[5]):
                                if ty==1:
                                    classify_list(L[1],ty,nt,idn,1)
                                elist.append(3)
                                classify_list(L[6],ty,nt,idn,1)
                            elif not endline(ty,L[10]):
                                if ty==1:
                                    classify_list(L[6],ty,nt,idn,1)
                                elist.append(3)
                                classify_list(L[1],ty,nt,idn,1)
                            elif endline(ty,L[5]) and endline(ty,L[10]):
                                classify_list(L[1],ty,nt,idn,1)
                                classify_list(L[6],ty,nt,idn,1)
                            elist.clear()
            elif ft==2:
                if inlist([L[2],L[6]],g(ty)) and notlist([L[4]],now_list):
                    if L[1] in f(ty)+edge and notlist([L[8]],now_list) and endline(ty,L[10]):
                        elist.append(2)
                        classify_list(L[8],ty,nt,idn,1)
                        elist.append(3)
                        classify_list(L[4],ty,nt,idn,1)
                        elist.clear()
                    elif L[8] in f(ty)+edge and notlist([L[1]],now_list) and endline(ty,L[3]):
                        elist.append(2)
                        classify_list(L[1],ty,nt,idn,1)
                        elist.append(3)
                        classify_list(L[4],ty,nt,idn,1)
                        elist.clear()
                    elif notlist([L[1],L[8]],now_list) and (endline(ty,L[3]) and endline(ty,L[10])):            #not endline, ty==1상황 추가
                        elist.append(1)
                        if ty==1:
                            classify_list(L[1],ty,nt,idn,1)
                            classify_list(L[8],ty,nt,idn,1)
                        elist.append(3)
                        classify_list(L[4],ty,nt,idn,1)
                        elist.clear()
            elif ft==3:
                if inlist([L[2],L[8]],now_list) and notlist([L[4],L[6]],now_list) and endline(ty,L[1]) and endline(ty,L[10]):
                    elist.append(2)
                    classify_list(L[4],ty,nt,idn,1)
                    classify_list(L[6],ty,nt,idn,1)
                    elist.clear()
        elif nt==4:
            if ft==1:
                if inlist([L[2],L[4],L[6],L[8]],g(ty)):
                    if notlist([L[8]],now_list) and endline(ty,L[1]) and endline(ty,L[10]):
                        classify_list(L[8],ty,nt,idn,1)
                    if notlist([L[1]],now_list) and endline(ty,L[8]) and endline(ty,L[3]):
                        classify_list(L[1],ty,nt,idn,1)
            elif ft==2:
                if inlist([L[2],L[4],L[8]],g(ty)) and notlist([L[6]],now_list) and endline(ty,L[1]) and endline(ty,L[10]):
                    classify_list(L[6],ty,nt,idn,1)
    def setlist(ts1,ts2,ts3,ts4,x,y):
        ts1.append((x,y))
        ts2.append((x,y))
        ts3.append((x,y))
        ts4.append((x,y))
        for i in range(1,6):
            ts1.append((x-ps*i,y))
            ts1.append((x+ps*i,y))
            ts2.append((x,y-ps*i))
            ts2.append((x,y+ps*i))
            ts3.append((x-ps*i,y-ps*i))
            ts3.append((x+ps*i,y+ps*i))
            ts4.append((x-ps*i,y+ps*i))
            ts4.append((x+ps*i,y-ps*i))
    def listinsert(ts1,ts2,ts3,ts4,ty,nt,ft,idn):
        logical_f(ts1,ty,nt,ft,idn)
        logical_f(ts2,ty,nt,ft,idn+1)
        logical_f(ts3,ty,nt,ft,idn+2)
        logical_f(ts4,ty,nt,ft,idn+3)
    def swap_lists(ts1,ts2,ts3,ts4,n1,n2):
        def swap(n1,n2,L):
            tmp=L[n1]
            L[n1]=L[n2]
            L[n2]=tmp
        swap(n1,n2,ts1)
        swap(n1,n2,ts2)
        swap(n1,n2,ts3)
        swap(n1,n2,ts4)
    def insert_lists(ty):
        for i in range(len(h(ty))):
            ts1, ts2, ts3, ts4 = [],[],[],[]
            x=h(ty)[i][0]
            y=h(ty)[i][1]
            setlist(ts1,ts2,ts3,ts4,x,y)
            if ty in  [3,4,5,6]:
                idn=h(ty)[i][2]
            else:
                idn=60*i
            listinsert(ts1,ts2,ts3,ts4,ty,1,0,idn)
            
            listinsert(ts1,ts2,ts3,ts4,ty,2,1,idn+4)
            listinsert(ts1,ts2,ts3,ts4,ty,2,2,idn+8)
            listinsert(ts1,ts2,ts3,ts4,ty,2,3,idn+12)
            listinsert(ts1,ts2,ts3,ts4,ty,2,4,idn+16)
            
            listinsert(ts1,ts2,ts3,ts4,ty,3,1,idn+20)
            listinsert(ts1,ts2,ts3,ts4,ty,3,2,idn+24)
            swap_lists(ts1,ts2,ts3,ts4,2,4)
            listinsert(ts1,ts2,ts3,ts4,ty,3,2,idn+28)
            swap_lists(ts1,ts2,ts3,ts4,2,4)
            listinsert(ts1,ts2,ts3,ts4,ty,3,3,idn+32)
            swap_lists(ts1,ts2,ts3,ts4,2,4)
            listinsert(ts1,ts2,ts3,ts4,ty,3,3,idn+36)
            swap_lists(ts1,ts2,ts3,ts4,4,6)
            listinsert(ts1,ts2,ts3,ts4,ty,3,3,idn+40)
            swap_lists(ts1,ts2,ts3,ts4,4,6)
            swap_lists(ts1,ts2,ts3,ts4,2,4)

            listinsert(ts1,ts2,ts3,ts4,ty,4,1,idn+44)
            listinsert(ts1,ts2,ts3,ts4,ty,4,2,idn+48)
            swap_lists(ts1,ts2,ts3,ts4,4,6)
            listinsert(ts1,ts2,ts3,ts4,ty,4,2,idn+52)
            swap_lists(ts1,ts2,ts3,ts4,2,6)
            listinsert(ts1,ts2,ts3,ts4,ty,4,2,idn+56)

    def prioritize():
        pass
