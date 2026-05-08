import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread(r".venv/3.1.jpg")
# 获取某个像素点的值
px=img[100,100]
# 仅获取蓝色通道的强度值
blue=img[100,100,0]
# 修改某个点的像素值
img[100,100]=[255,255,255]
# 获取图像属性
sp=img.shape
# 获取数据类型
dy=img.dtype
# 像素数
se=img.size
# 通道拆分
b,g,r=cv.split(img)
# 通道合并
img2=cv.merge((b,g,r))
# 色彩空间的转换
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# 转HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)

print(px)
print(blue)
print(img[100,100])
print(sp)
print(dy)
print(se)
print(b)
# plt.imshow(img[:,:,::-1])  #RGB通道翻转
# plt.imshow(b,cmap=plt.cm.gray)  #b通道
# plt.imshow(img2[:,:,::-1])
# plt.imshow(gray,cmap=plt.cm.gray)
plt.imshow(hsv)
plt.show()