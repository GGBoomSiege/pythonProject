from gensim.models import Word2Vec

# 加载预训练的中文词向量模型
model = Word2Vec.load(word2vec.model)

# 计算两个词语之间的相似度
word1 = "苹果"
word2 = "梨子"
similarity = model.wv.similarity(word1, word2)
print(f"相似度：{similarity}")

# 寻找与给定词语最相似的词语
word = "香蕉"
most_similar_words = model.wv.most_similar(word)
print(f"{word} 最相似的词语：")
for similar_word, similarity in most_similar_words:
    print(similar_word, similarity)
