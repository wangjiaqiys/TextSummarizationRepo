# 1. 运行步骤

1. 使用`project2_script.ipynb`脚本对新闻数据做了数据预处理，并将新闻数据与wiki数据做了合并，保存到 `dtaset/content_cut.txt`
2. 使用`word2vec.ipynb`脚本对`content_cut.txt`文件做了词向量训练
3. 使用`cnwiki_vocab_script.ipynb`脚本获得`cnwiki_vocab.txt`文件，并保存在 `SIF/auxiliary_data/cnwiki_vocab.txt` 路径下
4. 对`https://github.com/PrincetonML/SIF`实现sif句向量做了修改
    * 词向量加载改成加载中文词向量的方式
    * 脚本中存在一些文件加载，字典遍历的小bug，相应的做了修改
    * 调用SIF的脚本在utils/sif.py
5. knn平滑使用的是scikit-fda库，实现在utils/sif.py脚本中
6. woker.py脚本中写了脚本的逻辑
4. 使用`deploy.py`脚本可以部署成接口的形式，在网页中进行操作

# 2. 样例
参考图片。

# 3. TOOD

1. 预处理的脚本没有合并，jupyter脚本是在代码实现过程的一些测试。