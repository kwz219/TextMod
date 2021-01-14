class Constraint(object):
    def __init__(self):
        super(Constraint, self).__init__()
        self.constrain_list=[]
    def Mutable(self,word_property):
        if word_property in self.constrain_list:
            return True
        return False