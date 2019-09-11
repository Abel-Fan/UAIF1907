from wordcloud import WordCloud,ImageColorGenerator
# from scipy.misc import imread
from PIL import Image  # pip install pillow
import numpy as np

with open("data.txt",encoding="utf-8") as f:
    data = f.read()

luxunmask = np.array(Image.open("luxun2.png"))
imgcolor = ImageColorGenerator(luxunmask)
wc = WordCloud(font_path="./simhei.ttf",scale=6,mode="RGBA",background_color=None,mask=luxunmask,color_func=imgcolor)


wc.generate(data)
    

wc.to_file("res1.png")

