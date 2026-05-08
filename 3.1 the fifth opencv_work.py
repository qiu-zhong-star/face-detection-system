#几何变换

# 图像的平移(cv.warpAffine())
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread(r"D:\opencv_work\opencv_picture\03.jpg")
# 平移
# rows,cols=img.shape[:2]
# M=np.float32([[1,0,100],[0,1,50]])# 平移二维矩阵，x方向移100，y方向移50
# dst=cv.warpAffine(img,M,(cols,rows))

# # 图像旋转
# 调用cv.getRotationMatrix2D()获取旋转矩阵,然后调用cv.warpAffine()进行旋转
# rows,cols=img.shape[:2]
# # 生成旋转矩阵
# M=cv.getRotationMatrix2D((cols/2,rows/2),90,1)# 中心，角度，缩放比例
# # 进行旋转变换
# dst=cv.warpAffine(img,M,(cols,rows))

# # 图像仿射变换
# 调用cv2.getAffineTransform()将创建变换矩阵,最后该矩阵将传输给cv2.warpAffine()进行变换
# rows,cols=img.shape[:2]
# # 创建变换矩阵
# pts1=np.float32([[50,50],[200,50],[50,200]])# 原始图像的三个点
# pts2=np.float32([[100,100],[200,50],[100,250]])# 仿射的三个点
# M=cv2.getAffineTransform(pts1,pts2)
# # 完成放射变换
# dst=cv2.warpAffine(img,M,(cols,rows))

# # 图像透射变换
# 通过函数cv.getPerspectiveTransform()找到变换矩阵,将cv.warpPerspective()进行投射变换
# rows,cols=img.shape[:2]
# # 创建变换矩阵
# pts1=np.float32([[56,65],[368,52],[28,387],[389,390]]) # 原图像指定四个点
# pts2=np.float32([[100,145],[300,100],[80,190],[310,300]]) # 目标转换的四个点
#
# T=cv.getPerspectiveTransform(pts1,pts2)
# # 进行变换
# dst=cv.warpPerspective(img,T,(cols,rows))

# # 图像金字塔，进行图像采样
# up_img=cv.pyrUp(img) # 上采样操作
# img_1=cv.pyrDown(img) # 下采样操作


# 平移图像显示
# fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
# axes[0].imshow(img[:,:,::-1])
# axes[0].set_title("原图")
# axes[1].imshow(dst[:,:,::-1])
# axes[1].set_title("平移后的结果")
# plt.show()

# 旋转图像显示
# fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
# axes[0].imshow(img[:,:,::-1])
# axes[0].set_title("原图")
# axes[1].imshow(dst[:,:,::-1])
# axes[1].set_title("旋转后的结果")
# plt.show()

# # 仿射图像显示
# fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
# axes[0].imshow(img[:,:,::-1])
# axes[0].set_title("原图")
# axes[1].imshow(dst[:,:,::-1])
# axes[1].set_title("仿射后的结果")
# plt.show()

# # 透射图像显示
# fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
# axes[0].imshow(img[:,:,::-1])
# axes[0].set_title("原图")
# axes[1].imshow(dst[:,:,::-1])
# axes[1].set_title("透射后的结果")
# plt.show()

# # 图像采样显示
# cv.imshow('enlarge', up_img)
# cv.imshow('original', img)
# cv.imshow('shrink', img_1)
# cv.waitKey(0)
# cv.destroyAllWindows()

plt.imshow(img[:,:,::-1])
#plt.imshow(img)
plt.show()
































