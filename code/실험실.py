class C:
    def __init__(self,*p):
        if len(p)==4:
            self.set_scan_value(*p)

        elif len(p)==3:
            self.set_option_value(*p)
    
    def set_scan_value(self,a,b,c,d):
        self.update_parameter(locals())

    def set_option_value(self,e,f,g):
        self.update_parameter(locals())

    def update_parameter(self,local_dict):
        self.__dict__.update(local_dict)




a,b,\
c=1,2,3
print(a,b,c)


