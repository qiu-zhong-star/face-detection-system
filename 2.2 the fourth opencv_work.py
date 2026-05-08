# 图像的算数操作
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img1=cv.imread(r"D:\opencv_work\opencv_picture\01.jpg")
img2=cv.imread(r"D:\opencv_work\opencv_picture\02.jpg")
target_width = 640
target_height = 480

# 调整两张图片到相同尺寸
img1_resized = cv.resize(img1, (target_width, target_height))
img2_resized = cv.resize(img2, (target_width, target_height))
# 加减乘除cv.add() cv.subtract() cv.multiply() cv.divide()
# 加法操作
# img3=cv.add(img1_resized,img2_resized ) # cv中的加法
# img4=img1_resized+img2_resized          # 直接相加
# 算数操作图像显示
# fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
# axes[0].imshow(img3[:,:,::-1])
# axes[0].set_title("cv中的加法")
# axes[1].imshow(img4[:,:,::-1])
# axes[1].set_title("直接相加")
# plt.show()

# 图像混合
# img3=cv.addWeighted(img1_resized,0.3,img2_resized,0.7,0) #占比权重
# 图像混合显示
# plt.figure(figsize=(8,8))
# plt.imshow(img3[:,:,::-1])
# plt.show()

# 图像的缩放(调用cv.resize())
# 绝对尺寸
rows,cols=img1.shape[:2]
res=cv.resize(img1,(2*cols,2*rows),interpolation=cv.INTER_CUBIC)
# 相对尺寸
res1=cv.resize(img1,None,fx=0.5,fy=0.5)
# matplotlib显示图像
fig,axes=plt.subplots(nrows=1,ncols=3,figsize=(10,8),dpi=100)
axes[0].imshow(res[:,:,::-1])
axes[0].set_title("绝对尺寸（放大）")
axes[1].imshow(img1[:,:,::-1])
axes[1].set_title("原图")
axes[2].imshow(res1[:,:,::-1])
axes[2].set_title("相对尺寸（缩小）")
plt.show()












