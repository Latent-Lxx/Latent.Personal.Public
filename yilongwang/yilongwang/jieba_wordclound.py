#!/usr/bin/env python
# -*- coding: utf-8 -*-


from scipy.misc import imread
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import jieba
from jieba import analyse
import pandas as pd
import  csv
import numpy as np;
import matplotlib.pyplot as  plt
import os


# 获取当前路径
path_name = os.path.abspath('..');


# 解析图片
back_photo = imread(f'{path_name}/elong/back.jpeg');
graph = np.array(back_photo);
#词云设置
wc = WordCloud(background_color='white',
               max_words=1000,
               mask=graph,
               max_font_size=100,
               random_state=42,
               font_path=f'{path_name}/elong/msyh.ttf'
               )


file_name = input('请输入酒店名称:');

# 文本导入csv
with open (f'{path_name}/elong/comment_data/{file_name}','r') as f:
    string = f.read();
    jieba_cut = jieba.cut(string,cut_all=False);
    result_str = '/'.join(jieba_cut);
    top = jieba.analyse.extract_tags(result_str,topK=100,withWeight='true',allowPOS='n');

print('==> 文本导入成功!');
# 分词形成
with open(f'{path_name}/elong/fenci_data/{file_name}', 'w') as g:
    csv_head = ["name", "weight"];
    csv.writer(g).writerow(csv_head)
    for i in top:
        csv.writer(g).writerow(i);
print('==> 分词切分成功!');

# 词云形成
fp = pd.read_csv(f'{path_name}/elong/fenci_data/{file_name}');
name = fp.name;
value = fp.weight;

print('==> 词云制作成功!');


#
dic = dict(zip(name,value));
wc.generate_from_frequencies(dic);
image = ImageColorGenerator(graph);
# plt.imshow(wc);
plt.axis('off');
files = str(f'{path_name}/elong/word_cloud/{file_name}.png');
wc.to_file(files);

print('==> 保存完成！');










