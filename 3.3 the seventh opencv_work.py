# 图像平滑
# 椒盐噪声：图像中随机出现白点或黑点，高斯噪声：噪声的概率密度分布是正太分布
# 均值滤波：优点是算法简单，计算速度块，缺点是在去噪的同时也去除了很多细节，将图像变得模糊
# API:cv.blur(src,ksize,anchor,borderType),(输入图像；卷积核大小；表示核中心，默认（-1，-1）；边界类型)
# 高斯滤波：去除高斯噪声
# API:cv.GaussianBlur(src,ksize(卷积核的高度和宽度都应该为奇数),sigmax（水平方向的标准差）,sigmay（垂直方向的标准差）,borderType),
# 中值滤波：去除椒盐噪声
# API:cv.medianBlur（src,ksize）
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'PingFang SC']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

img=cv.imread(r"D:\opencv_work\opencv_picture\30.jpg")
img1=cv.imread(r"D:\opencv_work\opencv_picture\29.jpg")
# # 均值滤波
# blur=cv.blur(img,(5,5))

# 高斯滤波
# GaussianBlur=cv.GaussianBlur(img1,(3,3),1)

# 中值滤波
median_blur=cv.medianBlur(img,5)

# # 均值滤波图像显示
# plt.figure(figsize=(10,8),dpi=100)
# plt.subplot(121),plt.imshow(img[:,:,::-1]),plt.title('原图')
# plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(blur[:,:,::-1]),plt.title('均值滤波后结果')
# plt.xticks([]),plt.yticks([])
# plt.show()

# # 高斯滤波图像显示
# plt.figure(figsize=(10,8),dpi=100)
# plt.subplot(121),plt.imshow(img1[:,:,::-1]),plt.title('原图')
# plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(GaussianBlur[:,:,::-1]),plt.title('高斯滤波后结果')
# plt.xticks([]),plt.yticks([])
# plt.show()

# 高斯滤波图像显示
plt.figure(figsize=(10,8),dpi=100)
plt.subplot(121),plt.imshow(img[:,:,::-1]),plt.title('原图')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(median_blur[:,:,::-1]),plt.title('中值滤波后结果')
plt.xticks([]),plt.yticks([])
plt.show()
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False




































