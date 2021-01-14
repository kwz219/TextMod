class Judger(object):
    def __init__(self):
        super(Judger, self).__init__()
        self.judger_model=None
    def get_PPL(self,sentence):
        ppl=0
        return ppl

class ALL_PASS_Judger(Judger):
    def __init__(self):
        super(ALL_PASS_Judger, self).__init__()
    def If_pass(self,sentences):
        return True