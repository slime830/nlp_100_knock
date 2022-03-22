import argparse

EOS="EOS"

def print_separater(problem_num):
    print("-" * 10)
    print(f"problem{problem_num}")

def print_dict(dict:dict,head:int=None):
    if head is None:
        head=len(dict.keys())
    for key,value in dict.items()[:head]:
        print(key+" + "+value)

def problem30(mecab_result_filepath,encoding="utf-8"):
    sentences=list()
    sentence=list()
    with open(mecab_result_filepath,"r",encoding=encoding) as f:
        for oneline in f:
            oneline=oneline.replace("\n","")
            if oneline=="":
                continue
            if oneline == EOS:#if oneline is end of sentence
                sentences.append(sentence)
                sentence=list()
            else:
                # surface\tpos,pos1,.....,base,base2,base3
                surface,other_infos=oneline.split("\t")[0],oneline.split("\t")[1]
                other_infos=other_infos.split(",")
                pos=other_infos[0]
                pos1=other_infos[1]
                base=other_infos[-3]

                sentence.append({"surface":surface,"base":base,"pos":pos,"pos1":pos})
                
    return sentences

def problem31(sentences):
    surfaces=list()
    for sentence in sentences:
        for d in sentence:
            surfaces.append(d.get("surface"))
    
    return surfaces

def problem32(sentences):
    bases=list()
    for sentence in sentences:
        for d in sentence:
            bases.append(d.get("base"))
    
    return bases

def problem33(sentences):
    of_spans=list()
    for sentence in sentences:
        for d in sentence:
            if sentence.index(d)==0 or sentence.index(d)==len(sentence)-1:
                continue
            if d.get("surface") == "の":
                before_d=sentence[sentence.index(d)-1]
                after_d=sentence[sentence.index(d)+1]
                if before_d.get("pos") == "名詞" and after_d.get("pos") == "名詞":
                    of_spans.append(before_d.get("surface") + d.get("surface") + after_d.get("surface"))

    return of_spans
            

def main(args):
    print_separater(30)
    sentences=problem30(args.filepath)
    print(sentences[:10])
    print_separater(31)
    print(problem31(sentences))
    print_separater(32)
    print(problem32(sentences))
    print_separater(32)
    print(problem33(sentences))



    

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-fp","--filepath",help="MeCabの結果ファイル",type=str,default="./neko.txt.mecab")
    parser.add_argument("--encoding",help="エンコード",type=str,default="utf-8")
    main(parser.parse_args())

