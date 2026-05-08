# 形态学操作
# 腐蚀与膨胀
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread(r"D:\opencv_work\opencv_picture\07.jpg")
img1=cv.imread(r"D:\opencv_work\opencv_picture\11.jpg")
img2=cv.imread(r"D:\opencv_work\opencv_picture\12.jpg")
# # 创建核结构
# kernel=np.ones((5,5),np.uint8)
# # 图像腐蚀和膨胀
# erosion=cv.erode(img,kernel) # 腐蚀
# dilate=cv.dilate(img,kernel) # 膨胀

# 开运算与闭运算
# 创建核结构
kernel1=np.ones((10,10),np.uint8)
# 开运算：先腐蚀后膨胀，作用：分离物体，消除小区域。特点：去除小的干扰快，而不影响原来的图像
# 闭运算：先膨胀后腐蚀，作用：消除/闭合物体里的孔洞。特点：可以填充闭合区域
cvOpen=cv.morphologyEx(img1,cv.MORPH_OPEN,kernel1)
cvClose=cv.morphologyEx(img2,cv.MORPH_CLOSE,kernel1)

# 礼帽运算与黑帽运算
# 礼帽运算：礼帽运算 = 原图 - 开运算(原图)，突出了比原图轮廓周围更明亮的区域，与选择的核的大小有关
# 黑帽运算：黑帽运算 = 闭运算(原图) - 原图，突出了比原图轮廓周围更暗的区域，与选择的核的大小有关
kernel1=np.ones((10,10),np.uint8)
top=cv.morphologyEx(img1,cv.MORPH_TOPHAT,kernel1)
black=cv.morphologyEx(img2,cv.MORPH_BLACKHAT,kernel1)

# 腐蚀与膨胀图像展示
# fig,axes=plt.subplots(nrows=1,ncols=3,figsize=(10,8),dpi=100)
# axes[0].imshow(erosion[:,:,::-1])
# axes[0].set_title("腐蚀后结果")
# axes[1].imshow(img[:,:,::-1])
# axes[1].set_title("原图")
# axes[2].imshow(dilate[:,:,::-1])
# axes[2].set_title("膨胀后结果")
# plt.show()

# # 开闭运算图像显示
# fig,axes=plt.subplots(nrows=2,ncols=2,figsize=(10,8))
# axes[0,0].imshow(img1[:,:,::-1])
# axes[0,0].set_title("原图")
# axes[0,1].imshow(cvOpen[:,:,::-1])
# axes[0,1].set_title("开运算的结果")
# axes[1,0].imshow(img2[:,:,::-1])
# axes[1,0].set_title("原图")
# axes[1,1].imshow(cvClose[:,:,::-1])
# axes[1,1].set_title("闭运算的结果")
# plt.show()

# 礼帽与黑帽运算图像显示
fig,axes=plt.subplots(nrows=2,ncols=2,figsize=(10,8))
axes[0,0].imshow(img1[:,:,::-1])
axes[0,0].set_title("原图")
axes[0,1].imshow(top[:,:,::-1])
axes[0,1].set_title("礼帽运算的结果")
axes[1,0].imshow(img2[:,:,::-1])
axes[1,0].set_title("原图")
axes[1,1].imshow(black[:,:,::-1])
axes[1,1].set_title("黑帽运算的结果")
plt.show()