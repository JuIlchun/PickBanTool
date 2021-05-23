class champion:
    def __init__(self,name,top,jg,mid,sup,ad,ban,index) : 
        self.index=index
        self.name=name
        self.top=top
        self.jg=jg
        self.mid=mid
        self.sup=sup
        self.ad=ad
        self.ban=ban

가렌=champion("가렌",True,False,True,False,False,None,1)
print(가렌.index)