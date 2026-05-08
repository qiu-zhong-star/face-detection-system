# 直方图
# API：cv2.calcHist(images(原图像),channels（如果输入的是灰度图，它的值就是[0],如果是彩图分别对应B,G,R,[1],[2],[3]）,mask(掩模图像),histSize（BIN的数目）,ranges[,hist[,accumulate]]（像素值范围）)（每个函数都需要用[]传入）
# 掩膜：提取感兴趣区域；屏蔽作用；结构特征提取；特殊图像制作
# 直方图均衡化：扩大图像像素值的分布范围，提高图像的对比度，在过度曝光或不足的图像更好地突出细节
# 自适应均衡化 API：cv.createCLAHE(clipLimit(对比度限制，默认40),tileGridSize(分块大小，默认8*8))

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
# 直接以灰度图方式读入
img=cv.imread(r"D:\opencv_work\opencv_picture\15.jpg",0)

# # 统计灰度图
# histr=cv.calcHist([img],[0],None,[256],[0,256])


# #  创建蒙版
# mask=np.zeros(img.shape[:2],np.uint8)
# mask[400:3000,200:3000]=255
# #  掩膜
# masked_img=cv.bitwise_and(img,img,mask=mask)
# #  统计掩膜后图像的灰度图
# mask_histr=cv.calcHist([img],[0],mask,[256],[1,256])


# # 均衡化处理
# dst=cv.equalizeHist(img)


# 创建一个自适应均衡化对象，并应用于图像
clahe=cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
cl1=clahe.apply(img)

# # 绘制灰度图
# plt.figure(figsize=(10,6),dpi=100)
# plt.plot(histr)
# plt.grid()
# plt.show()

# # 蒙版与掩膜图像显示
# fig,axes=plt.subplots(nrows=2,ncols=2,figsize=(10,8))
# axes[0,0].imshow(img,cmap=plt.cm.gray)
# axes[0,0].set_title("原图")
# axes[0,1].imshow(mask,cmap=plt.cm.gray)
# axes[0,1].set_title("蒙版数据")
# axes[1,0].imshow(masked_img,cmap=plt.cm.gray)
# axes[1,0].set_title("掩膜后数据")
# axes[1,1].plot(mask_histr)
# axes[1,1].grid()
# axes[1,1].set_title("灰度直方图")
# plt.show()

# # 均衡化处理结果
# fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
# axes[0].imshow(img,cmap=plt.cm.gray)
# axes[0].set_title("原图")
# axes[1].imshow(dst,cmap=plt.cm.gray)
# axes[1].set_title("均衡化后结果")
# plt.show()

# 自适应均衡化处理结果
fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
axes[0].imshow(img,cmap=plt.cm.gray)
axes[0].set_title("原图")
axes[1].imshow(cl1,cmap=plt.cm.gray)
axes[1].set_title("自适应均衡化后结果")
plt.show()












































