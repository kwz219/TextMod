class Editor(object):
    """
        编辑器-基类
        对文本进行编辑操作的类
    """
    def __init__(self):
        super(Editor, self).__init__()

class Mask_Predictor(Editor):
    def __init__(self,MASK_LM):
        self.predict_model=MASK_LM
        self.predict_results=[]
    def predict(self):
        pass

class Rule_Editor(Editor):
    """
        基于规则的编辑器
    """
    def __init__(self):
        super(Rule_Editor, self).__init__()
        self.rulesdict=dict()
    def read_rules_from_file(self,rule_file):
        with open(rule_file,'r',encoding='utf8')as rf:
            for line in rf:
                src,tgt=line.split()
                self.rulesdict[src]=tgt
            rf.close()
    def transform_word(self,word):
        return self.rulesdict[word]
    def transform_sentences(self,tokenized_sentences,mutable_labels):
        transform_results=[]
        for sent,labels in zip(tokenized_sentences,mutable_labels):
            for index in range(len(sent)):
                if labels[index]==1:
                    sent[index]=self.transform_word(sent[index])
            transform_results.append(sent)
        return transform_results

