# 处理数据
import pickle
import jieba


with open("哪吒之魔童降世 短评.txt","rb") as f:
    data0 = pickle.load(f)

data1 = []
def cut_filter(data):
    return [ i for i in jieba.cut(data,cut_all=False) if i not in [',','，','。','.','！','\n','：','」','「','？','…','《','》','［','］','（','）','｜','~',' '] ]

for data in data0:
    data1+=cut_filter(data)


with open('data.txt','w',encoding="utf-8") as f:
    f.write(" ".join(data1))