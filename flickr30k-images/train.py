import pandas as pd

import jieba
import jieba.analyse

an = pd.read_table('results_20130124.token', sep='\t', header=None,names=['image', 'caption'])
from rake_nltk import Rake
rake_nltk_var = Rake(max_length=7)
import csv
with open('data.csv','w',encoding='utf-8') as f:
    r=len(list(an['caption']))

    re=csv.writer(f)
    re.writerow(['pos','imp'])
    cap=list(an['caption'])
    im=list(an['image'])
    for i in range(r):
        text=cap[i]
        print(text)
        ## Rake

        rake_nltk_var.extract_keywords_from_text(text)
        keyword_extracted = rake_nltk_var.get_ranked_phrases_with_scores()
        re.writerow([im[i],keyword_extracted])

