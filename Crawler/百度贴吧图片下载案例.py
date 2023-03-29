import requests
from lxml import etree

url = 'https://tieba.baidu.com/p/8320714184'

res = requests.get(url).text

# print(res.text)

selector = etree.HTML(res)

images_urls = selector.xpath('//img[@class="BDE_Image"]/@src')

offset = 0

# print(f'{offset}.jpg')

for item in images_urls:
    image_content = requests.get(item).content
    with open(f'{offset}.jpg','wb') as wfile:
        wfile.write(image_content)
    offset += 1