# Harris和Shi-Tomas算法

# # Harris算法
# 思想：通过图像的局部的小窗口观察图像，角点的特征是窗口沿任意方向都会导致图像灰度的明显变化
# #在 OpenCV 中实现 Harris 检测使用的 API 是：
# # API:dst = cv.cornerHarris(src(数据类型为 float32 的输入图像), blockSize(角点检测中要考虑的邻域大小), ksize, k(角点检测方程中的自由参数，取值通常为 [0.04, 0.06]))
#
# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt
# # 1.读取图像，并转为灰度图
# img = cv.imread(r"D:\opencv_work\opencv_picture\36.jpg")
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# # 2.角点检测
# # 2.1输入图象必须是 float32
# gray = np.float32(gray)
# # 2.2 最后一个参数在 0.04 到 0.05 之间
# dst = cv.cornerHarris(gray,2,3,0.04)
# # 设置阈值，将角点绘制出来，阈值根据图像进行选择
# img[dst>0.1*dst.max()] = [0,255,0]
# #图显
# plt.figure(figsize=(10,8),dpi=100)
# plt.imshow(img[:,:,::-1])
# plt.title('Harris角点检测')
# plt.xticks([]),plt.yticks([])
# plt.show()



# Shi-Tomas算法
# 对Harris算法的改进，能够更好地检测角点
# 在 OpenCV 中实现 Shi-Tomasi 角点检测使用 API:
# API:corners = cv2.goodFeaturesToTrack(image, maxcorners, qualityLevel, minDistance)
# 参数说明：
# image: 输入灰度图像
# maxCorners: 获取角点数的数目
# qualityLevel: 该参数指出最低可接受的角点质量水平，在 0-1 之间
# minDistance: 角点之间最小的欧式距离，避免得到相邻特征点
# 返回值说明：
# corners: 搜索到的角点，处理逻辑为：
# 排除所有低于质量水平的角点
# 把合格的角点按质量排序
# 删除质量较好的角点附近（小于最小欧式距离）的角点
# 最终返回 maxCorners 个角点


import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#1.读取图像
img = cv.imread(r"D:\opencv_work\opencv_picture\37.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 2.角点检测
corners = cv.goodFeaturesToTrack(gray, 1000, 0.005, 10)
# 3.绘制角点
for i in corners:
    x,y = i.ravel()
    cv.circle(img,(int(x),int(y)),2,(0,255,0),-1)
# 4.图显
plt.figure(figsize=(10,8),dpi=100)
plt.imshow(img[:,:,::-1])
plt.title('Shi-Tomas角点检测')
plt.xticks([]),plt.yticks([])
plt.show()






















