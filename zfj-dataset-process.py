import json

def data_process(readf,writesrc,writetgt):
    with open(readf,'r') as rf:
        with open(writesrc,'w') as wfs:
            with open(writetgt,'w') as wft:
                for line in rf.readlines():
                    line=json.loads(line)
                    src=line['code_tokens']
                    tgt=line['docstring_tokens']
                    word=" "
                    for i in src:
                        word+=i+" "
                    word=word.rstrip()
                    word+='\n'
                    wfs.write(word)
                    word=" "
                    for i in tgt:
                        word+=i+" "
                    word=word.rstrip()
                    word+='\n'
                    wft.write(word)
            wft.close()
        wfs.close()
    rf.close()

if __name__ == "__main__":
    data_process('./ZFJ-Python-SO-Dataset/python.both.train.jsonl','./ZFJ-Python-SO-Dataset/src-train.txt','./ZFJ-Python-SO-Dataset/tgt-train.txt')
    data_process('./ZFJ-Python-SO-Dataset/python.both.valid.jsonl','./ZFJ-Python-SO-Dataset/src-valid.txt','./ZFJ-Python-SO-Dataset/tgt-valid.txt')
    data_process('./ZFJ-Python-SO-Dataset/python.both.test.jsonl','./ZFJ-Python-SO-Dataset/src-test.txt','./ZFJ-Python-SO-Dataset/tgt-test.txt')

            

