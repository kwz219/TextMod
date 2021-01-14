import hanlp
def get_tokenized(sentences,model="default"):
    if model=="default":
        pass
    pass
def get_POS(sentence,model="default"):
    pass
def get_NER(sentence,model="fault"):
    pass
def example_tokenized(sentences):
    #用空格对文本分词,仅适用于输入已经分好词的情况
    tokenized_sentences=[]
    for sentence in sentences:
        tokenized_sentences.append(sentence.split())
    return tokenized_sentences
