class Dict(dict):
    def update_key(self,key,value_obj,p=()):
        if key not in self:
            self[key]=value_obj(*p)

