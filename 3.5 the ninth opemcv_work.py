# 边缘检测
# Sobel边缘检测(基于搜索的方法获取边界)
# API:Sobel_x_or_y=cv2.Sobel(src,ddepth(图像的深度(cv.CV_16S)),dx,dy,dst,ksize(Sobel算子的大小，即卷积核大小，必为奇数（1、3、5、7），默认为3，如果为-1，则演变为3*3的Scharr算子),scale,delta,borderType(图像的边界模式，默认cv2.BORDER_DEFAULT))
# Scale_abs=cv2.convertScaleAbs(x) #格式转换函数
# result=cv2.addWeighted(src1,alpha,src2,beta) # 图像混合
# Laplacian算子(基于零穿越获取边界)
# API:cv2.laplacian(src,ddepth[,dst[,ksize[,scale[,deltal[,borderType]]]]])
# canny边缘检测
# canny边缘检测流程：
# 噪声去除：高斯滤波
# 计算图像梯度：sobel算子，计算梯度大小和方向
# 非极大值抑制：利用梯度方向像素来判断当前像素是否为边界点
# 滞后阈值：设置两个阈值，确定最终的边界
# API:canny=cv2.Canny(img,threshold1(minval,较小的阈值将间断的边缘连接起来),threshold2(maxval,较大的阈值检测图像中明显的边缘))
# 匹配模板
# API：cv.matchTemplate(img(要进行模板匹配的图像),template(模板),method(实现模板匹配的算法：平方差匹配(CV_TM_SQDIFF,最好的匹配是0，匹配越差值越大)；相关匹配(CV_TM_CCORR，数值越大匹配程度越高，反之越低)；利用线性相关匹配(CV_TM_CCOEFF，1表示最完美匹配，-1为最差匹配)))
# 霍夫变换(提取图片的中圆与直线等几何形状)
# 霍夫线检测
# API:cv.Houghlines(img(要求是二值图像，在使用霍夫变换前先进行二值化，或进行Canny边缘检测),rho(ρ的精确度),theta(θ的精确度),threshold(阈值，只有累加器中的值高于该阈值才会被认为是直线))
# 霍夫圆环检测
# API:cv.HoughCircles(image(输入灰度图),method(使用霍夫变换圆检测的算法，它的参数是CV_HOUGH_GRADIENT),dp(霍夫空间分辨率),minDist(圆心之间的最小距离),param1=100(边缘检测时使用Canny算子的高阈值，低阈值是高阈值的一般),param2=100(检测圆心和确定半径时所共用的阈值),minRadius=0(检测到的圆半径的最大值),maxRadius=0(检测到的圆半径的最大值))


# import numpy as np
# import cv2 as cv
# import matplotlib.pyplot as plt
# img=cv.imread(r"D:\opencv_work\opencv_picture\13.jpg",0)


# # 计算Sobel卷积结果
# x=cv.Sobel(img,cv.CV_16S,1,0)
# y=cv.Sobel(img,cv.CV_16S,0,1)

# # 将数据进型转换
# Scale_absX=cv.convertScaleAbs(x) # convert转换 scale缩放
# Scale_absY=cv.convertScaleAbs(y)
# # 结果合成
# result=cv.addWeighted(Scale_absX,0.5,Scale_absY,0.5,0)
#

# # Scharr算子卷积结果
# x=cv.Sobel(img,cv.CV_16S,1,0,ksize=-1)
# y=cv.Sobel(img,cv.CV_16S,0,1,ksize=-1)


# # Laplacian转换
# result=cv.Laplacian(img,cv.CV_16S)
# Scale_abs=cv.convertScaleAbs(result)


# # Canny边缘检测
# lowThreshold=0
# max_lowThreshold=100
# canny=cv.Canny(img,lowThreshold,max_lowThreshold)


# # Sobel或Scharr滤波结果展示
# plt.figure(figsize=(10,8),dpi=100)
# plt.subplot(121),plt.imshow(img,cmap=plt.cm.gray),plt.title('原图')
# plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(result,cmap=plt.cm.gray),plt.title('Sobel/Scharr滤波后结果')
# plt.xticks([]),plt.yticks([])
# plt.show()

# # Laplacian滤波结果展示
# plt.figure(figsize=(10,8),dpi=100)
# plt.subplot(121),plt.imshow(img,cmap=plt.cm.gray),plt.title('原图')
# plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(Scale_abs,cmap=plt.cm.gray),plt.title('Laplacian滤波后结果')
# plt.xticks([]),plt.yticks([])
# plt.show()
#
# # Canny检测结果展示
# plt.figure(figsize=(10,8),dpi=100)
# plt.subplot(121),plt.imshow(img,cmap=plt.cm.gray),plt.title('原图')
# plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(canny,cmap=plt.cm.gray),plt.title('Laplacian滤波后结果')
# plt.xticks([]),plt.yticks([])
# plt.show()




























