from Util.FileIO import read_lines
from Util.Datapreprocess import example_tokenized
from Constraint.Constraint import No_Constraint,Abbr_Constraint
from Judgement.Judgement import ALL_PASS_Judger
from Editor.Editor import Rule_Editor
if __name__ =="__main__":
    #利用自定义规则进行替换原文中缩写的例子
    filename="../Resource\Source/Example_input"
    editrule="../Resource\EditRules\Example_Rule"
    inputs=read_lines(filename)
    tokenized_sentences=example_tokenized(inputs)#分词,这里只是示例
    constraint=Abbr_Constraint()#约束器判断是不是缩写
    judger=ALL_PASS_Judger()#该例中不用judge,只要修改就能通过
    rule_editor=Rule_Editor()#基于规则的编辑器
    rule_editor.read_rules_from_file(editrule)#从规则文件中读取规则

    constraint_labels=constraint.Mutable_indexes(tokenized_sentences)#首先获得可变动单词
    transform_results=rule_editor.transform_sentences(tokenized_sentences,constraint_labels)#基于编辑规则进行文本转换
    if judger.If_pass(transform_results):
        print(transform_results)


