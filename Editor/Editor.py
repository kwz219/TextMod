from transformers import BertTokenizer, BertForMaskedLM
import torch

class Editor(object):
    """
        编辑器-基类
        对文本进行编辑操作的类
    """
    def __init__(self):
        super(Editor, self).__init__()

class Mask_Predictor(Editor):
    """
    利用Masked Language Model 来预测别mask位置的词
    """
    def __init__(self,MASK_LM):

        self.tokenizer=BertTokenizer.from_pretrained(MASK_LM)
        self.mlmodel=BertForMaskedLM.from_pretrained(MASK_LM)
        self.predict_results=[]
    def predict_all(self,sentences,replace_ids,arg_K):
        for sent,id in zip(sentences,replace_ids):
            self.predict_one(sent,id,arg_K)
    def predict_one(self,sentence,replace_id,arg_k):
        maskid = replace_id
        # sentences.append(sentence)
        input_ids = torch.tensor(self.tokenizer.encode(sentence, add_special_tokens=True)).unsqueeze(0)
        input_ids = input_ids.to('cpu')
        self.mlmodel.eval()
        predict_sentences=[]
        with torch.no_grad():
            outputs = self.mlmodel(input_ids)
            predictions = outputs[0]
            indexes = self.argKth(predictions[0, maskid + 1], arg_k+1)
            predicted_token = self.tokenizer.convert_ids_to_tokens(indexes)
            for tokid in range(1, len(predicted_token)):
                sentence[maskid] = predicted_token[tokid]
                print(sentence)
                predict_sentences.append(sentence)
        self.predict_results.append(predict_sentences)
    def argKth(self,tensor, k):
        indexes = []
        while len(indexes) < k:
            cmaxi = torch.argmax(tensor)
            indexes.append(cmaxi)
            tensor[cmaxi] = -100
        return indexes

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

if __name__ =="__main__":
    MLM_BertChinese=Mask_Predictor("bert-base-chinese")
    MLM_BertChinese.predict_one(['生','活','的','真','谛','是','美'],6,5)

