# _*_ coding:utf-8 _*_
# Created by JiaQi at 08/10/2020

import os 
import pathlib 
from gensim.models import KeyedVectors
from collections import defaultdict

BASE_PATH = str(pathlib.Path(os.path.abspath('__file__')).parent)
model = KeyedVectors.load_word2vec_format(os.path.join(BASE_PATH, 'model', 'zhwiki_embedding_256.model'), binary=False)

def get_related_words(says):
    """
    找出和'说'相关的词
    :param says: 表示说的词 ['说', '表示', '认为', '指出', '提到', ...]
    :return related_says: 和 says 词义相关的词
    """
    object_says = says
    related_says = defaultdict(int)
    max_size = 500
    while object_says and len(related_says) < max_size:
        word = object_says.pop(0)
        related_ = [w for w, value in model.most_similar(word)]
        object_says += related_
        related_says[word] += 1
    return related_says

def save_data():
    related_says = get_related_words(['说', '表示', '认为', '指出', '提到', '宣布'])
    related_says = sorted(related_says.items(), key=lambda x:x[-1], reverse=True)
    related_words = '\n'.join([item[0] for item in related_says])
    with open(os.path.join(BASE_PATH, 'data', 'related_says.txt'), 'w', encoding='utf-8') as f:
        f.write(related_words)
    print('保存文件')

if __name__ == '__main__':
    save_data()