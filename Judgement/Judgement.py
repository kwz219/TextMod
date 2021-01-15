from transformers import AutoModelForCausalLM, BertTokenizer
import torch

class Judger(object):
    def __init__(self):
        super(Judger, self).__init__()
        self.judger_model=None
        self.evaluations=[]
    def get_evaluation(self,sentence):
        return self.evalautions

class ALL_PASS_Judger(Judger):
    def __init__(self):
        super(ALL_PASS_Judger, self).__init__()
    def If_pass(self,sentences):
        return True

class PPL_Judger(Judger):
    def __init__(self,model_id):
        self.gptmodel=AutoModelForCausalLM.from_pretrained(model_id,from_tf=True)
        self.tokenizer=BertTokenizer.from_pretrained(model_id)
    def calculate_ppl(self,sentence):
        device="cpu"
        encodings = self.tokenizer(sentence, return_tensors='pt')

        max_length = self.gptmodel.config.n_positions
        stride = 2
        lls = []
        for i in range(0, encodings.input_ids.size(1), stride):
            begin_loc = max(i + stride - max_length, 0)
            end_loc = min(i + stride, encodings.input_ids.size(1))
            trg_len = end_loc - i  # may be different from stride on last loop
            input_ids = encodings.input_ids[:, begin_loc:end_loc].to(device)
            target_ids = input_ids.clone()
            target_ids[:, :-trg_len] = -100
            # print(begin_loc,end_loc)
            with torch.no_grad():
                outputs = self.gptmodel(input_ids, labels=target_ids)
                log_likelihood = outputs[0] * trg_len

            lls.append(log_likelihood)

        ppl = torch.exp(torch.stack(lls).sum() / end_loc)
        return (ppl.item())

if __name__ =="__main__":
    ppl_judger=PPL_Judger("E:\pytorch_pretrained_models\gpt2-medium-chinese/")
    print(ppl_judger.calculate_ppl('他对自己非常有信心'))