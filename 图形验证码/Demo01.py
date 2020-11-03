import tesserocr
from PIL import Image

image = Image.open('./images/CheckCode.png')
# 转为灰度图像
image = image.convert('L')

threshold = 127
table = []

# 二值化
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
# mode='1'默认的阀值为127
image = image.point(table, '1')
# image.show()
result = tesserocr.image_to_text(image)
print(result)
