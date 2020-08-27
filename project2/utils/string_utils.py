# _*_ coding:utf-8 _*_
# Created by JiaQi at 08/10/2020

from pyltp import SentenceSplitter
import jieba 

def split_sentences(sentences):
    sents = SentenceSplitter.split(sentences)
    return [s for s in sents if len(s) > 0]

def cut(sent):
    return ' '.join(jieba.cut(sent))

def cut_string(string):
    sentences = split_sentences(string)
    return [cut(s) for s in sentences]