import hanlp
def get_tokenized(sentences,model="default"):
    if model=="default":
        tokenizer=hanlp.load(hanlp.pretrained.tok.LARGE_ALBERT_BASE)
    results=tokenizer(sentences)
    return results
def get_POS(sentences,model="default"):
    if model=="default":
        POS_model=hanlp.load(hanlp.pretrained.pos.CTB9_POS_ALBERT_BASE)
    results = POS_model(sentences)
    return results
def get_NER(sentence,model="fault"):
    pass
def example_tokenized(sentences):
    #用空格对文本分词,仅适用于输入已经分好词的情况
    tokenized_sentences=[]
    for sentence in sentences:
        tokenized_sentences.append(sentence.split())
    return tokenized_sentences
if __name__ =="__main__":
    tokenized_result=get_tokenized(["你吃饭了没？","昨日气温骤降。"])
    print(tokenized_result)
    print(get_POS(tokenized_result))#得到词性之前需要先分词
