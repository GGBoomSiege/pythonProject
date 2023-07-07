from gensim.models import KeyedVectors

# 加载训练完成的单词向量模型
model = KeyedVectors.load_word2vec_format("D:/tencent_ailab/tencent-ailab-embedding-zh-d200-v0.2.0/tencent-ailab-embedding-zh-d200-v0.2.0-s.bin", binary=True)

# 查找与单词最相似的单词
similar_words = model.most_similar('工业互联网')
for word,similar in similar_words:
    print(word, similar)

print(model.similarity('运维工程师', '运维开发'))
print(model.similarity('运维工程师', '互联网'))