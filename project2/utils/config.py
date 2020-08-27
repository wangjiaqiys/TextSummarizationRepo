# _*_ coding:utf-8 _*_
# Created by JiaQi at 08/10/2020

import os 
import pathlib 
from gensim.models import KeyedVectors
from pyltp import Parser, NamedEntityRecognizer, Postagger
# 项目的根目录
root = str(pathlib.Path(os.path.abspath('__file__')).parent)

# 词向量路径
wv_model_path = os.path.join(root, 'model', 'news_zhwiki_embedding_256.model')

# ltp模型路径
ner_model_path = os.path.join(root, 'model/ltp', 'ner.model')
parse_model_path = os.path.join(root, 'model/ltp', 'parser.model')
postag_model_path = os.path.join(root, 'model/ltp', 'pos.model')
# ner = NamedEntityRecognizer()
# ner.load(ner_model_path)

# parser = Parser()
# parser.load(parse_model_path)

# postagger = Postagger()
# postagger.load(postag_model_path)

# 说 相关词语
related_says_path = os.path.join(root, 'data', 'related_says.txt')

# 句向量相关
wordfile = os.path.join(root, 'model/zhwiki_embedding_256.bin')
weightfile = os.path.join(root, 'SIF/auxiliary_data/cnwiki_vocab.txt') # each line is a word and its frequency