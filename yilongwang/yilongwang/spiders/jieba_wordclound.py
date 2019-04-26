#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

  @Time    : 19-4-26 下午5:31
  @Author  : Latent
  @Site    : 
  @File    : jieba_wordclound.py
  @Software: PyCharm
  @PS      : 

'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

  @Time    : 19-4-25 上午9:46
  @Author  : Latent
  @Site    :S
  @File    : test_jieba.py
  @Software: PyCharm
  @PS      :

'''

from scipy.misc import imread
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import jieba
from jieba import analyse
import pandas as pd
import  csv
import numpy as np;
import matplotlib.pyplot as  plt

# 解析图片
back_photo = imread('/home/latent-lxx/Desktop/elong/background.jpg');
graph = np.array(back_photo);
#词云设置
wc = WordCloud(background_color='white',
               max_words=1000,
               mask=graph,
               max_font_size=100,
               random_state=42,
               font_path='../simhei.ttf'
               )

#创建csv文件
file = open('/home/latent-lxx/Desktop/jieba_makesi','w');
new_csv = csv.writer(file);
new_csv.writerow(['name','weight']);
file.close();

# 分词导入csv
with open ('/home/latent-lxx/Desktop/makesi','r') as f,open ('/home/latent-lxx/Desktop/jieba_makesi','a+') as g:
    string = f.read();
    jieba_cut = jieba.cut(string,cut_all=False);
    result_str = '/'.join(jieba_cut);
    top = jieba.analyse.extract_tags(result_str,topK=100,withWeight=True,allowPOS='n')

    for i in top:
        csv.writer(g).writerow(i);

# 词云
fp = pd.read_csv('/home/latent-lxx/Desktop/jieba_makesi');
name = fp.name;
value = fp.weight;



dic = dict(zip(name,value));
wc.generate_from_frequencies(dic);
image = ImageColorGenerator(graph);
plt.imshow(wc);
plt.axis('off');
plt.show()











