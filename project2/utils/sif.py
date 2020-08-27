# _*_ coding:utf-8 _*_

import numpy as np 

import skfda
from skfda import FDataGrid
import skfda.preprocessing.smoothing.kernel_smoothers as ks
import skfda.preprocessing.smoothing.validation as val

from utils.config import wordfile, weightfile

import SIF.src.data_io as data_io
import SIF.src.params as params
import SIF.src.SIF_embedding as SIF_embedding

def euclidean_distance(x1, x2):
    '''
    func: 计算两个向量的欧式距离
    '''
    return np.sqrt(np.power(x1-x2,2).sum())

def knn_smooth(data):
    """
    func: 对欧式距离进行knn平滑(使用scikit-fda库进行平滑计算)
    param: data: 欧式距离列表 - list
    return: score: 平滑之后的得分
    """
    smoothing_parameter = int(len(data) / 2)
    fd = FDataGrid(
        sample_points = data, 
        data_matrix = [[i for i in range(1, len(data)+1)]]
    )
    knn = ks.KNeighborsSmoother(smoothing_parameter=smoothing_parameter)
    fd_smoothed = knn.fit_transform(fd)
    
    return [i[0] for i in fd_smoothed.data_matrix.round(2)[0]]

def sif_embedding(sents):
    """
    func: 对列表sents赋值句向量
    param: sents - 切词后的句子列表
    return: 词向量列表
    """
    weightpara = 1e-3 # the parameter in the SIF weighting scheme, usually in the range [3e-5, 3e-3]
    rmpc = 1 # number of principal components to remove in SIF weighting scheme(是否去掉最大主成分项)
    (words, We) = data_io.getWordmap(wordfile)
    # load word weights
    word2weight = data_io.getWordWeight(weightfile, weightpara) # word2weight['str'] is the weight for the word 'str'
    weight4ind = data_io.getWeight(words, word2weight) # weight4ind[i] is the weight for the i-th word
    # load sentences
    x, m = data_io.sentences2idx(sents, words)
    w = data_io.seq2weight(x, m, weight4ind) # get word weights
    param = params.params()
    param.rmpc = rmpc
    embedding = SIF_embedding.SIF_embedding(We, x, w, param) # embedding[i,:] is the embedding for sentence i
    return embedding

def cal_similarity(sents_embedding, title_embedding):
    scores = []
    title_embed = title_embedding[0]
    for s_e in sents_embedding:
        score = euclidean_distance(title_embed, s_e[0])
        scores.append(score)
    # 使用knn平滑
    smooth_scores = [(i, value) for i, value in enumerate(knn_smooth(scores))]
    # 排序
    sorted_scores = sorted(smooth_scores, key = lambda x:x[-1])
    return sorted_scores

def get_summerization(sents, scores, topn):
    idx = [item[0] for item in scores][:topn]
    return ''.join([sents[i].replace(' ', '') for i in idx])