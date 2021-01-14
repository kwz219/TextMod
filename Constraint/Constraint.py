class Constraint(object):
    """
        约束器-基类
        用于约束哪些类型的词可以用来编辑
    """
    def __init__(self):
        super(Constraint, self).__init__()
        self.constrain_list=[]
    def Mutable(self,word_property):
        if word_property in self.constrain_list:
            return True
        return False

class No_Constraint(object):
    """
        约束器-无约束
    """
    def __init__(self):
        super(No_Constraint, self).__init__()
    def Mutable(self,word_property):
        return True
class Abbr_Constraint(Constraint):
    def __init__(self):
        super(Abbr_Constraint, self).__init__()
    def Mutable(self,word):
        if str(word).isalpha() and str(word).isupper():
            return True
        return False
    def Mutable_indexes(self,sentences):
        sentences_indexes=[]
        for sentence in sentences:
            indexes=[]
            for word in sentence:
                if self.Mutable(word):
                    indexes.append(1)
                else:
                    indexes.append(0)
            sentences_indexes.append(indexes)
        return sentences_indexes
