from .header import *

class Parents:
    def __init__(self,posT,lineT):
        self.posT=posT
        self.lineT=lineT

    def compare(self,parents):
        union=self.posT+parents.posT
        return len(union)==len(set(union))

    @property
    def sibling_key(self):
        return self.posT,self.lineT

