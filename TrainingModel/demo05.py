from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('D:/tencent_ailab/tencent-ailab-embedding-zh-d200-v0.2.0/tencent-ailab-embedding-zh-d200-v0.2.0-s.txt', binary=False)
model.save_word2vec_format('D:/tencent_ailab/tencent-ailab-embedding-zh-d200-v0.2.0/tencent-ailab-embedding-zh-d200-v0.2.0-s.bin', binary=True)
