from wordcloud import WordCloud,ImageColorGenerator
from scipy.misc import imread

with open("data.txt",encoding="utf-8") as f:
    data = f.read()

luxunmask = imread("timg.jpg")
imgcolor = ImageColorGenerator(luxunmask)
wc = WordCloud(font_path="./simhei.ttf",scale=6,mode="RGBA",background_color=None,mask=luxunmask,color_func=imgcolor)


wc.generate(data)
    

wc.to_file("res1.png")

