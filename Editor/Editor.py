class Editor(object):
    def __init__(self):
        super(Editor, self).__init__()

class Mask_Predictor(Editor):
    def __init__(self,MASK_LM):
        self.predict_model=MASK_LM
        self.predict_results=[]
    def predict(self):
        pass