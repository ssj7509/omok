import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont
import tkinter.messagebox as tkmsg
from tkinter import filedialog,simpledialog
from tk_header import *

import math,random
import analyzer_v2 as anl
import benchmark_learning as bml
import randomforest_learning as rfl

def setRootWindow(uimain):
    win=uimain.root=tk.Tk()
    win.withdraw()
    setIcons(uimain)
    setIntroWindow(uimain)

def setIntroWindow(uimain):
    win=uimain.introwin=tk.Toplevel(uimain.root)
    win.title("Intro")
    win.geometry("600x400+300+130")
    win.resizable(False,False)
    win.protocol("WM_DELETE_WINDOW",lambda:closeWindow(uimain,win))
    
    WD=uimain.introwidgets
    WD["icons"]=uimain.icons

    WD["intro_Font1"]=tkfont.Font(family="맑은 고딕",size=20)
    WD["intro_Font2"]=tkfont.Font(family="맑은 고딕",size=20,slant="italic")

    WD["intro_Label1"]=tk.Label(win,text="Omok Simulator",font=WD["intro_Font2"])
    WD["intro_Label1"].pack()

    WD["start_Button"]=tk.Button(win,text="START",command=lambda:startMainWindow(uimain))
    WD["start_Button"].pack()

def startMainWindow(uimain):
    setMainWindow(uimain)
    uimain.introwin.destroy()    

def setMainWindow(uimain):
    win=uimain.mainwin=tk.Toplevel(uimain.root)
    win.title("Omok Simulator")
    win.geometry("900x600+200+130")
    win.resizable(False,False)
    win.protocol("WM_DELETE_WINDOW",lambda:closeWindow(uimain,win))

    WD=uimain.mainwidgets
    WD["icons"]=uimain.icons

    WD["xyList"],WD["recordList"]=[],[]
    WD["xyObjDict"]={}
    WD["xyNormalDict"]={}
    WD["xyBanDict"]={}
    WD["xyTriggerDict"]={}
    WD["elementDict"]={}
    WD["cursor"],WD["checkPoint"]=0,0
    WD["end"]=0

    WD["menubar"]=tk.Menu(win)
    WD["menu"]=tk.Menu(WD["menubar"],tearoff=0)
    WD["menu"].add_command(label="새 게임",command=lambda:newGame(WD))
    WD["menu"].add_command(label="초기화",command=lambda:clearGame(WD))
    WD["menu"].add_separator()
    WD["menu"].add_command(label="저장",command=lambda:saveGame(WD))
    WD["menu"].add_command(label="다른 이름으로 저장",command=lambda:saveOtherGame(WD))
    WD["menu"].add_separator()
    WD["menu"].add_command(label="기보 불러오기",command=lambda:openGame(win,WD))
    WD["menu"].add_command(label="문자열 기보 변환",command=lambda:convertString(WD))
    WD["menu"].add_command(label="기보 Y축 대칭 변환",command=lambda:convertY(win,WD))
    WD["menu"].add_separator()
    WD["menu"].add_command(label="종료",command=lambda:closeWindow(uimain,win))
    
    WD["menubar"].add_cascade(labe="상위메뉴",menu=WD["menu"])
    win.config(menu=WD["menubar"])

    setBoardWidgets(win,WD)

    WD["mainSeparator1"]=ttk.Separator(win,orient="vertical")
    WD["mainSeparator1"].place(x=MSP1,relheight=1)

    '''
    WD["mainSeparator2"]=ttk.Separator(win,orient="vertical")
    WD["mainSeparator2"].place(x=MSP2,relheight=1)
    '''

    setOptVars(WD)
    setOptionMenuWidgets(win,WD)

def setOptionMenuWidgets(win,WD):
    mwin=WD["optMainFrame"]=tk.Frame(win,bd=1,relief="sunken")
    WD["optMainFrame"].place(x=OMX,y=OMY,width=OMW,height=OMH)

    nwin=WD["optNorthFrame"]=tk.Frame(mwin,height=OMSP)
    WD["optNorthFrame"].pack(side="top",fill="x",anchor="n")

    swin=WD["optSouthFrame"]=tk.Frame(mwin)
    WD["optSouthFrame"].pack(side="top",expand=True,fill="both")

    setOptNorthFrame(nwin,WD)
    setOptSouthFrame(swin,WD)

    for i in range(1,5):
        WD[f"optNorthCheckButton{i}"].config(command=lambda:selectNorthOption(WD))

    WD["optSeparator1"]=ttk.Separator(mwin,orient="horizontal")
    WD["optSeparator1"].place(y=OMSP,relwidth=1)

def setOptVars(WD):
    WD["contentL1_1"]=[]
    WD["checkVarL1_1"]=[]
    WD["objL1_1"]=[]
    WD["setFuncP1_1"]={"varL":WD["checkVarL1_1"],"command":lambda:select1_1(WD)}
    WD["setFunc1_1"]=lambda:setBindObj(WD["optPageFrame1_1"],WD["optScale1_1"],WD["contentL1_1"],
                                       WD["objL1_1"],setCheckBox,WD["setFuncP1_1"],OBJW1_1,OBJH1_1)

    WD["contentL1_2"]=[]
    WD["checkVarL1_2"]=[]
    WD["objL1_2"]=[]
    WD["setFuncP1_2"]={"varL":WD["checkVarL1_2"],"command":None}
    WD["setFunc1_2"]=lambda:setBindObj(WD["optPageFrame1_2"],WD["optScale1_2"],WD["contentL1_2"],
                                       WD["objL1_2"],setCheckBox,WD["setFuncP1_2"],OBJW1_2,OBJH1_2)

    WD["contentL2_S"]=[]
    WD["checkVarL2_S"]=[]
    WD["objL2_S"]=[]
    WD["setFuncP2_S"]={"varL":WD["checkVarL2_S"],"command":None}
    WD["setFunc2_S"]=lambda:setBindObj(WD["optPageFrame2_S"],WD["optScale2_S"],WD["contentL2_S"],
                                       WD["objL2_S"],setCheckBox,WD["setFuncP2_S"],OBJW2_S,OBJH2_S)

    WD["optButtonContentL"]=WD["contentL1_1"]
    WD["optButtonVarL"]=WD["checkVarL1_1"]

def setOptNorthFrame(nwin,WD):
    WD["optNorthCheckVarL"]=[tk.IntVar()for _ in range(4)]
    
    WD["optNorthCheckButton1"]=tk.Checkbutton(nwin,text="1차원 공격",variable=WD["optNorthCheckVarL"][0])
    WD["optNorthCheckButton1"].place(x=OMCX1,y=OMCY1,width=OMCW1,height=OMCH1)

    WD["optNorthCheckButton2"]=tk.Checkbutton(nwin,text="1차원 방어",variable=WD["optNorthCheckVarL"][1])
    WD["optNorthCheckButton2"].place(x=OMCX2,y=OMCY2,width=OMCW2,height=OMCH2)

    WD["optNorthCheckButton3"]=tk.Checkbutton(nwin,text="2차원 공격",variable=WD["optNorthCheckVarL"][2])
    WD["optNorthCheckButton3"].place(x=OMCX3,y=OMCY3,width=OMCW3,height=OMCH3)

    WD["optNorthCheckButton4"]=tk.Checkbutton(nwin,text="2차원 방어",variable=WD["optNorthCheckVarL"][3])
    WD["optNorthCheckButton4"].place(x=OMCX4,y=OMCY4,width=OMCW4,height=OMCH4)

def setOptSouthFrame(swin,WD):
    WD["optButtonFrame"]=bwin=tk.Frame(swin,height=BFH)
    WD["optButtonFrame"].pack(side="bottom",anchor="s",fill="x")
    
    WD["optMainNotebook"]=ttk.Notebook(swin)
    WD["optMainNotebook"].pack(expand=True,fill="both")

    WD["optPageFrame1"]=tk.Frame(swin)
    WD["optMainNotebook"].add(WD["optPageFrame1"],text=f"{'1차 선택':^{NBT1}}")

    WD["optPageFrame2"]=tk.Frame(swin)
    WD["optMainNotebook"].add(WD["optPageFrame2"],text=f"{'겹침 선택':^{NBT2}}")

    setPage1(WD["optPageFrame1"],WD)
    setPage2(WD["optPageFrame2"],WD)

    WD["optSelectAllButton"]=tk.Button(bwin,text="모두 선택",command=lambda:optSelectAll(WD))
    WD["optSelectAllButton"].pack(side="left",fill="y")

    WD["optCancelAllButton"]=tk.Button(bwin,text="모두 해제",command=lambda:optCancelAll(WD))
    WD["optCancelAllButton"].pack(side="left",fill="y",padx=10)

    WD["optDeleteCheckButton"]=tk.Button(bwin,text="삭제",state="disabled",command=lambda:optDeleteCheck(WD))
    WD["optDeleteCheckButton"].pack(side="right",fill="y")

    WD["optMainNotebook"].bind("<<NotebookTabChanged>>",lambda e:optMainTab(e,WD))
    WD["optSubNotebook"].bind("<<NotebookTabChanged>>",lambda e:optSubTab(e,WD))

def optMainTab(e,WD):
    main_index=WD["optMainNotebook"].index("current")

    if main_index:
        
        WD["optButtonContentL"]=WD["contentL2_S"]
        WD["optButtonVarL"]=WD["checkVarL2_S"]
        
        WD["optDeleteCheckButton"].config(state="normal")
    else:
        optSubTab(0,WD)

def optSubTab(e,WD):
    sub_index=WD["optSubNotebook"].index("current")

    WD["optButtonContentL"]=WD[f"contentL1_{sub_index+1}"]
    WD["optButtonVarL"]=WD[f"checkVarL1_{sub_index+1}"]

    WD["optDeleteCheckButton"].config(state=("disabled","normal")[sub_index])

def optSelectAll(WD):
    for var in WD["optButtonVarL"]:
        var.set(1)

    refreshOptPage(WD)

def optCancelAll(WD):
    for var in WD["optButtonVarL"]:
        var.set(0)

    refreshOptPage(WD)

def optDeleteCheck(WD):
    WD["optButtonContentL"],WD["optButtonVarL"]=map(lambda L:[x for i,x in enumerate(L) \
                                                if WD["optButtonVarL"][i].get()],
                                                (WD["optButtonContentL"],WD["optButtonVarL"]))

    print([v.get() for v in WD["optButtonVarL"]])
    print(WD["optButtonContentL"],WD["optButtonVarL"],sep="\n")

    refreshOptPage(WD)

def setPage1(pwin,WD):
    WD["optLineFrame"]=tk.Frame(pwin,height=LFH)
    WD["optLineFrame"].pack(anchor="n",fill="x")

    WD["optSubNotebook"]=ttk.Notebook(pwin)
    WD["optSubNotebook"].pack(expand=True,fill="both")

    WD["optPageFrame1_1"]=tk.Frame(pwin)
    WD["optSubNotebook"].add(WD["optPageFrame1_1"],text=f"{'옵션 선택':^{NBT1_1}}")

    WD["optPageFrame1_2"]=tk.Frame(pwin)
    WD["optSubNotebook"].add(WD["optPageFrame1_2"],text=f"{'선택된 목록':^{NBT1_2}}")

    setPage1_1(WD["optPageFrame1_1"],WD)
    setPage1_2(WD["optPageFrame1_2"],WD)

def setPage1_1(pwin,WD):
    WD["optScale1_1"]=tk.Scale(pwin,showvalue=False,command=lambda e:WD["setFunc1_1"]())
    WD["optScale1_1"].pack(side="right",fill="y")

def setPage1_2(pwin,WD):
    WD["optScale1_2"]=tk.Scale(pwin,showvalue=False,command=lambda e:WD["setFunc1_2"]())
    WD["optScale1_2"].pack(side="right",fill="y")

def setPage2(pwin,WD):
    WD["optPageFrame2_N"]=tk.Frame(pwin,height=OMFH2_N,bd=2,relief="groove")
    WD["optPageFrame2_N"].pack(anchor="n",fill="x")

    WD["optPageFrame2_M"]=tk.Frame(pwin,height=OMFH2_M)
    WD["optPageFrame2_M"].pack(anchor="n",fill="x")

    WD["optPageFrame2_S"]=tk.Frame(pwin)
    WD["optPageFrame2_S"].pack(expand=True,fill="both")

    setPage2_N(WD["optPageFrame2_N"],WD)
    setPage2_M(WD["optPageFrame2_M"],WD)
    setPage2_S(WD["optPageFrame2_S"],WD)

def setPage2_N(pwin,WD):
    WD["optNumLabel1"]=tk.Label(pwin,text="1.")
    WD["optNumLabel1"].place(x=OMNLX1,y=OMNLY1,width=OMNLW1,height=OMNLH1)

    WD["optNumLabel2"]=tk.Label(pwin,text="2.")
    WD["optNumLabel2"].place(x=OMNLX2,y=OMNLY2,width=OMNLW2,height=OMNLH2)
    
    WD["optComboBox1"]=ttk.Combobox(pwin,state="readonly")
    WD["optComboBox1"].place(x=OMCBX1,y=OMCBY1,width=OMCBW1,height=OMCBH1)

    WD["optComboBox2"]=ttk.Combobox(pwin,state="readonly")
    WD["optComboBox2"].place(x=OMCBX2,y=OMCBY2,width=OMCBW2,height=OMCBH2)

    WD["optAddButton"]=tk.Button(pwin,text="add",command=lambda:addButton2_S(WD))
    WD["optAddButton"].place(x=OMABX,y=OMABY,width=OMABW,height=OMABH)

def setPage2_M(pwin,WD):
    WD["optSeparator2_M"]=ttk.Separator(pwin,orient="horizontal")
    WD["optSeparator2_M"].place(y=OMSP2_M,relwidth=1)

def addButton2_S(WD):
    s1,s2=sorted(map(lambda obj:obj.current(),(WD["optComboBox1"],WD["optComboBox2"])))
    if not (s1+1 and s2+1):
        return

    content=(lambda T1,T2:((T1,T2),"\n\n".join((getContentName(T)for T in (T1,T2)))))(*map(lambda s:WD["contentL1_2"][s][0],(s1,s2)))
    
    if content in WD["contentL2_S"]:
        return

    WD["contentL2_S"].append(content)
    WD["checkVarL2_S"].append(tk.IntVar())

    WD["setFunc2_S"]()

def setPage2_S(pwin,WD):
    WD["optScale2_S"]=tk.Scale(pwin,showvalue=False,command=lambda e:WD["setFunc2_S"]())
    WD["optScale2_S"].pack(side="right",fill="y")

def select1_1(WD):
    refreshPage1_2(WD)

def selectNorthOption(WD):
    refreshPage1_1(WD)
    refreshPage1_2(WD)

def refreshOptPage(WD):
    refreshPage1_2(WD)
    refreshPage2_S(WD)

def refreshPage1_1(WD):
    WD["contentL1_1"]=sum(([[T,getContentName(T)]for T in L] \
                           for i,L in enumerate((D1_ATTACKL,D1_DEFENSEL)) \
                           if WD["optNorthCheckVarL"][i].get()),[])

    WD["checkVarL1_1"].clear()
    WD["checkVarL1_1"]+=[tk.IntVar()for _ in WD["contentL1_1"]]
    
    WD["setFunc1_1"]()

def refreshPage1_2(WD):
    WD["contentL1_2"].clear()
    WD["contentL1_2"]+=[WD["contentL1_1"][i] for i,var in enumerate(WD["checkVarL1_1"]) if var.get()]

    WD["checkVarL1_2"].clear()
    WD["checkVarL1_2"]+=[tk.IntVar()for _ in WD["contentL1_2"]]

    textL=[content[1]for content in WD["contentL1_2"]]

    WD["optComboBox1"].configure(values=textL)
    WD["optComboBox2"].configure(values=textL)
    
    WD["setFunc1_2"]()

def refreshPage2_S(WD):
    WD["setFunc2_S"]()
 
def setBindObj(pwin,scale,contentL,objL,set_func,p,tW,tH):
    for obj in objL:
        obj.destroy()
    objL.clear()

    pH=pwin.winfo_height()
    q,r=divmod(pH,tH)

    scaleN=scale.get()
    start_index,corr_val=divmod(scaleN,tH)
    
    scale.config(to=(0,(len(contentL)-q)*tH-r)[len(contentL)>q])
    
    for i,si in enumerate(range(start_index,start_index+min(math.ceil((pH+corr_val)/tH),len(contentL[start_index:])))):
        setObj(pwin,contentL,objL,set_func,p,i,si,corr_val,tW,tH)

    for obj in objL+[pwin]:
        obj.bind("<MouseWheel>",lambda e:scroll(e,scale))

def scroll(e,scale):
    scale.set(scale.get()-SCRSPD*e.delta/120)

def setObj(pwin,contentL,objL,set_func,p,i,si,corr_val,tW,tH):
    tFrame=tk.Frame(pwin,bd=2,relief="groove")
    tFrame.place(x=0,y=i*tH-corr_val,width=tW,height=tH)

    objL+=[tFrame,setCheckBox(tFrame,contentL,objL,p,si)]
    

def setCheckBox(fwin,contentL,objL,p,si):
    tobj=tk.Checkbutton(fwin,text=contentL[si][1],variable=p["varL"][si],
                        command=p["command"],anchor="w",justify="left")
    tobj.pack(expand=True,fill="both")

    return tobj


def setBoardWidgets(win,WD):
    WD["canvas"]=tk.Canvas(win,relief="sunken",bd=1)
    WD["canvas"].place(x=BX,y=BY,width=BW,height=BH)
    WD["canvas"].bind("<ButtonRelease-1>",lambda e:clickCanvas(e,WD))
    
    setBoard(win,WD)

    WD["playButton1"]=tk.Button(win,text="흑 착수",command=lambda:userPlay(WD,0))
    WD["playButton1"].place(x=PX1,y=PY1,width=PW1,height=PH1)

    WD["playButton2"]=tk.Button(win,text="백 착수",command=lambda:userPlay(WD,1))
    WD["playButton2"].place(x=PX2,y=PY2,width=PW2,height=PH2)

    WD["undoButton"]=tk.Button(win,image=WD["icons"]["left"],command=lambda:undo(WD))
    WD["undoButton"].place(x=LBX,y=LBY,width=LBW,height=LBH)
    WD["redoButton"]=tk.Button(win,image=WD["icons"]["right"],command=lambda:redo(WD))
    WD["redoButton"].place(x=RBX,y=RBY,width=RBW,height=RBH)

    WD["countLabel"]=tk.Label(win,text="0 / 0")
    WD["countLabel"].place(x=CLX,y=CLY)
    
    WD["checkLabel"]=tk.Label(win,text="check point : None")
    WD["checkLabel"].place(x=CKLX,y=CKLY)

    WD["turnLabel"]=tk.Label(win,text="turn : BLACK")
    WD["turnLabel"].place(x=TLX,y=TLY)

    WD["optRadioVal"]=tk.IntVar()

    WD["optRadioButton2"]=tk.Radiobutton(win,text="비활성화",value=0,variable=WD["optRadioVal"],
                                         anchor="w",command=lambda:refreshWindow(WD))
    WD["optRadioButton2"].place(x=ORBX2,y=ORBY2,width=ORBW2,height=ORBH2)
    
    WD["optRadioButton1"]=tk.Radiobutton(win,text="옵션메뉴 활성화",value=1,variable=WD["optRadioVal"],
                                         anchor="w",command=lambda:refreshWindow(WD))
    WD["optRadioButton1"].place(x=ORBX1,y=ORBY1,width=ORBW1,height=ORBH1)

    '''
    WD["redButton"]=tk.Button(win,text="red mark",command=lambda:test_red(WD))
    WD["redButton"].place(x=MRX,y=MRY,width=TBW,height=TBH)

    WD["blueButton"]=tk.Button(win,text="blue mark",command=lambda:test_blue(WD))
    WD["blueButton"].place(x=MBX,y=MBY,width=TBW,height=TBH)

    WD["orangeButton"]=tk.Button(win,text="orange mark",command=lambda:test_orange(WD))
    WD["orangeButton"].place(x=MOX,y=MOY,width=TBW,height=TBH)

    WD["delButton"]=tk.Button(win,text="delete mark",command=lambda:test_del(WD))
    WD["delButton"].place(x=TDX,y=TDY,width=TBW,height=TBH)
    '''

    WD["aiButton"]=tk.Button(win,text="자동",command=lambda:aiPlay(WD))
    WD["aiButton"].place(x=TDX,y=TDY,width=TBW,height=TBH)
    
    
def clickCanvas(e,WD):
    x=round(e.x/(BW/16))
    y=round(e.y/(BH/16))

    if all(map(lambda v:v>0 and v<16,(x,y))):
        if WD.get("checkCircle"):
            WD["canvas"].delete(WD["checkCircle"])
        WD["checkCircle"]=insert_Circle(WD,x,y,CR,"red")
        WD["checkX"],WD["checkY"]=x,y

def userPlay(WD,n):
    t=WD["cursor"]%2
    if not WD.get("checkCircle") or n!=t:
        return
    x,y=WD["checkX"],WD["checkY"]
    if (x,y) in WD["xyList"][:WD["cursor"]]:
        return
    addStone(WD,x,y)

def aiPlay(WD):
    if WD["cursor"]==0:
        addStone(WD,8,8)
        return

    turn_group,turn=anl.main_play(WD["xyList"][:WD["cursor"]])
    xyT,arrayT=anl.get_result(turn_group[turn].D1)

    xyL=bml.get_xy(xyT,arrayT,"11")
    x,y=random.choice(xyL)

    print(f"({x+1},{y+1}),{turn_group[turn].D1[(x,y)].max_abs}")

    addStone(WD,x+1,y+1)

def addStone(WD,x,y):
    if WD["end"]:
        return
    WD["xyObjDict"][f"stone{x}_{y}"]=insert_Circle(WD,x,y,SR,("black","white")[WD["cursor"]%2])
    if WD["cursor"]==len(WD["xyList"]):
        WD["xyList"].append((x,y))
    checkCursor(WD,x,y)
    refreshCount(WD)

def undo(WD):
    if not WD["cursor"]:
        return
    WD["canvas"].delete(WD["xyObjDict"][(lambda x,y:f"stone{x}_{y}")(*WD["xyList"][WD["cursor"]-1])])
    WD["cursor"]-=1
    if WD["checkPoint"] and WD["cursor"]==WD["checkPoint"]:
        WD["xyList"]=WD["recordList"].copy()
        WD["checkPoint"]=0
    refreshCount(WD)
    
def redo(WD):
    cursor,xyL=WD["cursor"],WD["xyList"]
    if cursor>=len(xyL):
        return
    x,y=xyL[cursor]
    addStone(WD,x,y)

def checkCursor(WD,x,y):
    WD["cursor"]+=1
    
    cursor,recordL,xyL=WD["cursor"],WD["recordList"],WD["xyList"]
    if not WD["checkPoint"] and cursor<=len(recordL) and (x,y)!=recordL[cursor-1]:
        WD["checkPoint"]=cursor-1
        WD["xyList"]=xyL[:cursor-1]+[(x,y)]
        
    if (x,y)!=xyL[cursor-1]: 
        WD["xyList"]=xyL[:cursor-1]+[(x,y)]
    
def setBoard(win,WD):
    for i in range(1,16):
        WD[f"row_Line{i+1}"]=insert_Line(WD,1,i,15,i,1,"black",0)
        WD[f"column_Line{i+1}"]=insert_Line(WD,i,1,i,15,1,"black",0)

        WD[f"row_Text1{i+1}"]=insert_Text(WD,BTL,i,f"{16-i}","black")
        WD[f"row_Text2{i+1}"]=insert_Text(WD,16-BTR,i,f"{16-i}","black")

        WD[f"column_Text1{i+1}"]=insert_Text(WD,i,BTT,chr(i+64),"black")
        WD[f"column_Text2{i+1}"]=insert_Text(WD,i,16-BTB,chr(i+64),"black")

    WD["mark_Circle1"]=insert_Circle(WD,4,4,MR,"black")
    WD["mark_Circle2"]=insert_Circle(WD,12,4,MR,"black")
    WD["mark_Circle3"]=insert_Circle(WD,4,12,MR,"black")
    WD["mark_Circle4"]=insert_Circle(WD,12,12,MR,"black")
    WD["mark_Circle5"]=insert_Circle(WD,8,8,MR,"black")

def openGame(win,WD):
    fname=WD["fname"]=selectFile(win,WD)
    if not fname:
        return
    clearGame(WD)
    with open(fname,'r') as f:
        s=f.read()
    if not s:
        return
    WD["xyList"]=[(lambda x,y:(int(x),16-int(y)))(*xy.split(','))for xy in s.split("\n")]
    WD["recordList"]=WD["xyList"].copy()
    setStone(WD)
    refreshCount(WD)

def selectFile(win,WD):
    return filedialog.askopenfilename(initialdir="./기보",
                                      title="기보 선택",
                                      filetypes=(("txt files","*.txt"),("all files","*.*")),
                                      master=win)
def setStone(WD):
    for i,(x,y) in enumerate(WD["recordList"]):
        WD["xyObjDict"][f"stone{x}_{y}"]=insert_Circle(WD,x,y,SR,("black","white")[i%2])
    WD["cursor"]=len(WD["recordList"])

def clearGame(WD):
    for x,y in WD["xyList"]:
        WD["canvas"].delete(WD["xyObjDict"][f"stone{x}_{y}"])
    WD["xyList"].clear()
    WD["recordList"].clear()
    WD["cursor"],WD["checkPoint"]=0,0
    refreshCount(WD)

def newGame(WD):
    clearGame(WD)
    WD["fname"]=""

def saveGame(WD):
    if not WD.get("fname"):
        saveOtherGame(WD)
    else:
        saveFile(WD,WD["fname"])

def saveOtherGame(WD):
    fname=getFileName()
    if fname:
        saveFile(WD,f"기보/{fname}.txt")

def getInputValue(s1,s2,s3):
    vname=tk.simpledialog.askstring(s1,s2)
    if not vname:
        tkmsg.showwarning(f"{s3} 오류",f"{s3}을 제대로 입력해주세요.")
    return vname

def getFileName():
    return getInputValue("기보 저장","저장할 파일 이름 입력","파일 이름")

def getStrValue():
    return getInputValue("기보 변환","변환할 문자열 입력","문자열")

def saveFile(WD,fname):
    WD["fname"]=fname
    currentL=WD["recordList"]=WD["xyList"][:WD["cursor"]]
    with open(fname,"w") as f:
        f.write('\n'.join(f"{x},{16-y}"for x,y in currentL))

def convertString(WD):
    s=getStrValue()
    if not s:
        return
    fname=getFileName()
    if not fname:
        return
    with open(f"기보/{fname}.txt",'w') as f:
        f.write('\n'.join(f"{x},{y}"for x,y in zip((ord(c)-96 for c in s if c.isalpha()),''.join((c,' ')[c.isalpha()]for c in s).split())))

def convertY(win,WD):
    fname=selectFile(win,WD)
    if not fname:
        return
    with open(fname,'r') as f:
        s=f.read()
    with open(fname,'w') as f:
        f.write('\n'.join((lambda x,y:f"{x},{16-int(y)}")(*xy.split(','))for xy in s.split('\n')))

def refreshWindow(WD):
    refreshCount(WD)
    clearOption(WD)

    if WD["optRadioVal"].get():
        refreshOption(WD)

def refreshOption(WD):
    clearOption(WD)

    if 1-WD["optRadioVal"].get():
        return
    
    turn_group,turn=anl.main_play(WD["xyList"][:WD["cursor"]])
    element_dict=get_D1_elements(turn_group,turn)

    opt_normalL,opt_triggerL=(getOption1_2,getOption2_S)[bool(WD["contentL2_S"])](WD,element_dict)
    banL=getBanL(turn_group[anl.BLACK].ban_dict)
    print(banL)

    setOptionMark(WD,opt_normalL,opt_triggerL)
    setBanL(WD,banL)

def getBanL(ban_dict):
    banL=[]
    for x,y in ban_dict.keys():
        banL.append((x,y))
    return banL

def getOption2_S(WD,element_dict):
    normalS,triggerS=set(),set()
  
    for (T1,T2),_ in WD["contentL2_S"]:
        if not(element_dict.get(T1) and element_dict.get(T2)):
            continue

        L1,L2=element_dict[T1],element_dict[T2]
        for i,info1 in enumerate(L1):
            for j,info2 in enumerate(L2):
                if info1["xyT"]==info2["xyT"] and anl.compare_parents(info1["parents"],info2["parents"]):
                    (normalS,triggerS)[bool(info1["targetL"])].add((info1["xyT"],tuple(info1["targetL"])))
                    (normalS,triggerS)[bool(info2["targetL"])].add((info2["xyT"],tuple(info2["targetL"])))

    return list(normalS),list(triggerS)

def getOption1_2(WD,element_dict):
    optionS=set()
    normalS,triggerS=set(),set()
    
    for T,_ in WD["contentL1_2"]:
        if not element_dict.get(T):
            continue
        
        for info in element_dict[T]:
            (normalS,triggerS)[bool(info["targetL"])].add((info["xyT"],tuple(info["targetL"])))

    return list(normalS),list(triggerS)

def setBanL(WD,banL):
    for x,y in banL:
        if not WD["xyBanDict"].get((x,y)):
            WD["xyBanDict"][(x,y)]=[]

        WD["xyBanDict"][(x,y)].append(insert_Line(WD,x+0.6,y+0.6,x+1.4,y+1.4,5,"red",0))
        WD["xyBanDict"][(x,y)].append(insert_Line(WD,x+0.6,y+1.4,x+1.4,y+0.6,5,"red",0))

def setOptionMark(WD,opt_normalL,opt_triggerL):
    for (x,y),targetL in opt_normalL:
        if not WD["xyNormalDict"].get((x,y)):
            WD["xyNormalDict"][(x,y)]=[]

        WD["xyNormalDict"][(x,y)].append(insert_Circle(WD,x+1,y+1,OR,"yellow"))

    for (x,y),targetL in opt_triggerL:
        if not WD["xyTriggerDict"].get((x,y)):
            WD["xyTriggerDict"][(x,y)]=[]

        for tx,ty in targetL:
            WD["xyTriggerDict"][(x,y)].append(insert_Line(WD,x+1,y+1,tx+1,ty+1,1,"blue",1))

def clearOption(WD):
    for objL in list(WD["xyNormalDict"].values())+list(WD["xyTriggerDict"].values())+\
        list(WD["xyBanDict"].values()):
        for obj in objL:
            WD["canvas"].delete(obj)
        objL.clear()

def getContentName(T):
    s=f"{T[0]+1}차원 : "
    if 1-T[1]:
        s+=f"{('열린','닫힌')[T[2]]} {('공격','트리거')[T[3]]} {T[4]}"
    else:
        s+=f"방어 {T[4]} :: {T[2]+1}등급"
    return s

def get_D1_elements(turn_group,turn):
    element_dict={}

    for space in turn_group[turn].D1.values():
        xyT=space.xyT
        for element in space.elementL:
            parents,lineT,prior_val,stance,shape,element_type=element.get_vars()
            targetL=element.targetL if element_type==anl.TRIGGER else []

            key=(anl.D1,stance,shape,element_type,prior_val)
            
            if not element_dict.get(key):
                element_dict[key]=[]
            element_dict[key].append({"parents":parents,"xyT":xyT,"targetL":targetL})

    return element_dict

def refreshCount(WD):
    cp=WD["checkPoint"]
    WD["countLabel"].config(text=f"{WD['cursor']}/{len(WD['xyList'])}")
    WD["checkLabel"].config(text=f"check point : {('None',cp)[bool(cp)]}")
    WD["turnLabel"].config(text=f"turn : {('BLACK','WHITE')[WD['cursor']%2]}")
    WD["end"]=bool(anl.end_check(WD["xyList"][:WD["cursor"]])[WD["cursor"]%2])

def insert_Circle(WD,x,y,r,color):
    return WD["canvas"].create_oval(x*BW/16-r,y*BH/16-r,x*BW/16+r,y*BH/16+r,fill=color)

def insert_Line(WD,x1,y1,x2,y2,w,color,arrow):
    return WD["canvas"].create_line(x1*BW/16,y1*BH/16,x2*BW/16,y2*BH/16,width=w,fill=color,arrow=(None,tk.LAST)[arrow])

def insert_Text(WD,x,y,s,color):
    return WD["canvas"].create_text(x*BW/16,y*BH/16,text=s,fill=color)

def test_red(WD):
    if not WD.get("checkCircle"):
        return
    x,y=WD["checkX"],WD["checkY"]
    WD["xyObjDict"][f"mark{x}_{y}"]=insert_Circle(WD,x,y,SR,"red")

def test_blue(WD):
    if not WD.get("checkCircle"):
        return
    x,y=WD["checkX"],WD["checkY"]

    WD["xyObjDict"][f"mark{x}_{y}"]=insert_Circle(WD,x,y,SR,"blue")

def test_orange(WD):
    if not WD.get("checkCircle"):
        return
    x,y=WD["checkX"],WD["checkY"]
    WD["xyObjDict"][f"mark{x}_{y}"]=insert_Circle(WD,x,y,SR,"orange")
    
def test_del(WD):
    if not WD.get("checkCircle"):
        return
    x,y=WD["checkX"],WD["checkY"]
    WD["canvas"].delete(WD["xyObjDict"][f"mark{x}_{y}"])

def closeWindow(uimain,win):
    win.destroy()
    uimain.root.destroy()

def setIcons(uimain):
    icons=uimain.icons

    icons["test_icon"]=tk.PhotoImage(file="icon/test1.png",master=uimain.root)
    icons["test_black"]=tk.PhotoImage(file="icon/black.png",master=uimain.root)
    icons["left"]=tk.PhotoImage(file="icon/왼쪽2.png",master=uimain.root)
    icons["right"]=tk.PhotoImage(file="icon/오른쪽2.png",master=uimain.root)

    
