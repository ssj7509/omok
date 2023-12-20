import simulator_tk as stk

#uimain.root.after(delay,lambda:after_test(*p))
#win.wm_attributes("-topmost", 1)

class mainUI:
    def __init__(self):
        self.root=None
        self.introwin=None
        self.mainwin=None
        self.introwidgets={}
        self.mainwidgets={}
        self.icons={}

        self.blackmode="user"
        self.whitemode="user"

        self.ai_delay=0

    def run(self):
        stk.setRootWindow(self)
        self.root.mainloop()

def verify_xy(entire,xyT):
    if any(n not in range(15) for n in xyT):
        return 1
    elif entire[BLACK].get(xyT) or entire[WHITE].get(xyT):
        return 2
    elif entire[BAN].get(xyT):
        return 3
    return 0

#별도 시뮬레이션 프로젝트로 이동, ai play로 통일
def user_play(entire,turn,input_xy):
    xy_code=verify_xy(entire,turn,input_xy)
    while True:
        xy_code=verify_xy(entire,turn,input_xy)
        if not xy_code:
            break

        #좌표 에러 처리 함수 <-- xy_code

    entire[ENTIRE][input_xy]=1
    entire[turn][input_xy]=1

    #시뮬레이션 함수 <-- input_xy


def ai_play():
    t=analyzer.Dimension3()

uimain=mainUI()
uimain.run()
