win.update()
for k in twin.keys():
    print(f"{k} : {twin.cget(k)}")
print(twin.winfo_rootx())

#체크박스 선택
def check_img(event):
    tn=coreL.index(event.widget)//3+scale_corelist.get()
    coreVarL[tn].set(1-coreVarL[tn].get())
    
WD["canvas"].create_line(5, 100, 100, 100, arrow='last', arrowshape=f'{8} {10} {5}')

scr_obj.set(scr_obj.get()-event.delta/120)

scr_obj.config(to=0 if len_data<=objN else len_data-objN)
scrN=scr_obj.get()
