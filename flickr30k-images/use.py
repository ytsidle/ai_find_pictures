import tkinter

import pandas as pd
from rake_nltk import Rake
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from translate import Translator
data=pd.read_csv('data.csv')
nltk_var=Rake(max_length=3)


def xiansi(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    similarity = intersection / union
    return similarity


def imp_list(text):
    """
    :param:本品输入以English字符串，返回其中关键词
    :return: [(..,..),(..,..)]
    """
    global nltk_var
    nltk_var.extract_keywords_from_text(text)
    keyword_extracted = nltk_var.get_ranked_phrases_with_scores()
    return keyword_extracted
class datas:
    def __init__(self,pos,imp,value):
        self.pos=pos
        self.imp=eval(imp)
        self.value=value

l=[]
pol=list(data['pos'])
iml=list(data['imp'])
inp=tkinter.simpledialog.askstring('Asking','寻找内容')
inp=Translator(from_lang="ZH",to_lang="EN-US").translate(inp)
print("trans:{}".format(inp))
inimp=[x[1] for x in imp_list(inp)]
for i in range(len(pol)):
    t=datas(pol[i],iml[i],xiansi(inimp,[x[1] for x in eval(iml[i])]))
    l.append(t)
l=sorted(l, key=lambda x: x.value,reverse=True)
wl=[]
for i in range(5):
    where=r"flickr30k-images/{}".format(l[i].pos)
    print(where)


    img_path = where.split('#')[0]
    wl.append(img_path)
    img = mpimg.imread(img_path)
    plt.figure(figsize=(19,9))
    plt.imshow(img)
    plt.axis('off')
    plt.show()
wl=wl[:2]
print(wl)

