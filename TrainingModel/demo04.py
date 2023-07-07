# 腾讯AI Lab采用自研的Directional Skip-Gram (DSG)算法作为词向量的训练算法。
# DSG算法基于广泛采用的词向量训练算法Skip-Gram (SG)，在文本窗口中词对共现关系的基础上，
# 额外考虑了词对的相对位置，以提高词向量语义表示的准确性。
import gensim

wv_from_text = gensim.models.KeyedVectors.load_word2vec_format('D:/tencent_ailab/tencent-ailab-embedding-zh-d200-v0.2.0/tencent-ailab-embedding-zh-d200-v0.2.0.txt', binary=False)
wv_from_text.init_sims(replace=True)  # 神奇，很省内存，可以运算most_similar
# 该操作是指model已经不再继续训练了，那么就锁定起来，让Model变为只读的，这样可以预载相似度矩阵，对于后面得相似查询非常有利。
import numpy as np


def compute_ngrams(word, min_n, max_n):
    # BOW, EOW = ('<', '>')  # Used by FastText to attach to all words as prefix and suffix
    extended_word = word
    ngrams = []
    for ngram_length in range(min_n, min(len(extended_word), max_n) + 1):
        for i in range(0, len(extended_word) - ngram_length + 1):
            ngrams.append(extended_word[i:i + ngram_length])
    return list(set(ngrams))


def wordVec(word, wv_from_text, min_n=1, max_n=3):
    '''
    wordVec函数是计算未登录词的.
    ngrams_single/ngrams_more,主要是为了当出现oov的情况下,最好先不考虑单字词向量
    '''
    # 确认词向量维度
    word_size = wv_from_text.wv.syn0[0].shape[0]
    # 计算word的ngrams词组
    ngrams = compute_ngrams(word, min_n=min_n, max_n=max_n)
    # 如果在词典之中，直接返回词向量
    if word in wv_from_text.wv.vocab.keys():
        return wv_from_text[word]
    else:
        # 不在词典的情况下
        word_vec = np.zeros(word_size, dtype=np.float32)
        ngrams_found = 0
        ngrams_single = [ng for ng in ngrams if len(ng) == 1]
        ngrams_more = [ng for ng in ngrams if len(ng) > 1]
        # 先只接受2个单词长度以上的词向量
        for ngram in ngrams_more:
            if ngram in wv_from_text.wv.vocab.keys():
                word_vec += wv_from_text[ngram]
                ngrams_found += 1
                # print(ngram)
        # 如果，没有匹配到，那么最后是考虑单个词向量
        if ngrams_found == 0:
            for ngram in ngrams_single:
                word_vec += wv_from_text[ngram]
                ngrams_found += 1
        if word_vec.any():
            return word_vec / max(1, ngrams_found)
        else:
            raise KeyError('all ngrams for word %s absent from model' % word)


vec = wordVec('千奇百怪的词向量', wv_from_text, min_n=1, max_n=3)  # 词向量获取
wv_from_text.most_similar(positive=[vec], topn=10)  # 相似词查找