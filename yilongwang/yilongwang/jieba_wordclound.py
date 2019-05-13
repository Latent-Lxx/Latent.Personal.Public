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

# 解析图片
back_photo = imread('/home/latent-lxx/Desktop/elong/back.jpeg');
graph = np.array(back_photo);
#词云设置
wc = WordCloud(background_color='white',
               max_words=1000,
               mask=graph,
               max_font_size=100,
               random_state=42,
               font_path='/home/latent-lxx/fonts/msyh.ttf'
               )


file_name = input('请输入酒店名称:');

#创建csv文件
file = open('/home/latent-lxx/Desktop/jieba_makesi','w');
new_csv = csv.writer(file);
new_csv.writerow(['name','weight']);
file.close();


# 文本导入csv
with open ('/home/latent-lxx/Desktop/elong/comment_data/{name}'.format(name=file_name),'r') as f:
    string = f.read();
    jieba_cut = jieba.cut(string,cut_all=False);
    result_str = '/'.join(jieba_cut);
    top = jieba.analyse.extract_tags(result_str,topK=100,withWeight='true',allowPOS='n');

print('==> 文本导入成功!');
# 分词形成
with open('/home/latent-lxx/Desktop/elong/fenci_data/{name}'.format(name=file_name), 'w') as g:
    csv_head = ["name", "weight"];
    csv.writer(g).writerow(csv_head)
    for i in top:
        csv.writer(g).writerow(i);
print('==> 分词切分成功!');

# 词云形成
fp = pd.read_csv('/home/latent-lxx/Desktop/elong/fenci_data/{name}'.format(name=file_name));
name = fp.name;
value = fp.weight;

print('==> 词云制作成功!');


#
dic = dict(zip(name,value));
wc.generate_from_frequencies(dic);
image = ImageColorGenerator(graph);
# plt.imshow(wc);
plt.axis('off');
files = str('/home/latent-lxx/Desktop/elong/word_cloud/{isname}.png'.format(isname=file_name));
wc.to_file(files);

print('==> 保存完成！');










