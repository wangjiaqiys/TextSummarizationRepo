# _*_ coding:utf-8 _*_
# Created by JiaQi at 08/10/2020
# from utils.config import related_says_path, ner, parser, postagger

from utils.load_file import load
from utils.string_utils import cut_string, cut
from utils.sif import sif_embedding, cal_similarity, get_summerization

def process(content, title):
    # 1. 分句, 分词
    ## 1.1 文章需要切分成句子
    ## 1.2 标题应该是一段，对这一段进行分词即可
    sents = cut_string(content)
    titles = [cut(title)]
    # TODO: 将项目1改成句向量提取的方式
    # 2. 句向量计算
    sents_embeddings = sif_embedding(sents)
    title_embeddings = sif_embedding(titles)
    # 3. 计算文章中每个句子与标题的欧式距离 - 该得分是经过knn平滑和排序之后的得分
    scores = cal_similarity(sents_embeddings, title_embeddings)
    # 4. 获取文章摘要 - 取文章三分之一的句子作为文章的摘要
    summerization = get_summerization(sents, scores, len(sents)//3)
    return {'summerization': summerization}
    

if __name__ == '__main__':
    string = """
    此外，自本周（6月12日）起，除小米手机6等15款机型外，其余机型已暂停更新发布（含开发版/体验版内测，稳定版暂不受影响），以确保工程师可以集中全部精力进行系统优化工作。有人猜测这也是将精力主要用到MIUI 9的研发之中。
    MIUI 8去年5月发布，距今已有一年有余，也是时候更新换代了。
    当然，关于MIUI 9的确切信息，我们还是等待官方消息。
    """
    title = '小米MIUI9首批机型曝光：共计15款'

    summarization = process(string, title)
    print('ok')