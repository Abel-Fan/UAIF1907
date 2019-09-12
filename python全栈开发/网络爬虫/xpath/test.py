# import lxml.etree as etree
#
# with open("index.html") as f:
#     htmlobj = etree.HTML(f.read())
#     # arr = htmlobj.xpath("//div[@class='box']/ancestor::body")
#     # arr = htmlobj.xpath("//div[@class='box']/child::*")
#     arr = htmlobj.xpath("//div[contains(@class,'box')]")
#     print(arr)
