#模板匹配与霍夫检测

# # 模板匹配
# import numpy as np
# import cv2 as cv
# import matplotlib.pyplot as plt
#
# # 原图与模板导入
# img1=cv.imread(r"D:\opencv_work\opencv_picture\32.jpg")
# # 模板导入
# template=cv.imread(r"D:\opencv_work\opencv_picture\33.jpg")
# h,w,l=template.shape
# # 模板匹配
# res=cv.matchTemplate(img1,template,cv.TM_CCOEFF_NORMED)
# # 返回图像中最匹配的位置，确定左上角的坐标，并将匹配位置绘制在图像上
# min_val,max_val,min_loc,max_loc=cv.minMaxLoc(res)
# # 使用平方差时最小值为最佳匹配位置
# # top_left=max_loc
# top_left=max_loc
# bottom_right=(top_left[0]+w,top_left[1]+h)
# cv.rectangle(img1,top_left,bottom_right,(0,255,0),2)
# # 模板匹配图像显示
# plt.imshow(img1[:,:,::-1])
# plt.title('匹配结果'),plt.xticks([]),plt.yticks([])
# plt.show()

# # 霍夫线变换
# import numpy as np
# import cv2 as cv
# import matplotlib.pyplot as plt
# # 加载图片，转为二值图
# img=cv.imread(r"D:\opencv_work\opencv_picture\34.jpg")
#
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# edges=cv.Canny(gray,50,150)
#
# # 霍夫直线变换
# lines=cv.HoughLines(edges,0.8,np.pi/180,150)
# # 将检测的线绘制在图像上（注意是极坐标）
# for line in lines:
#     rho,theta=line[0]
#     a=np.cos(theta)
#     b=np.sin(theta)
#     x0=a*rho
#     y0=b*rho
#     x1 = int(x0 + 1000 * (-b))
#     y1 = int(y0 + 1000 * a)
#     x2 = int(x0 - 1000 * (-b))
#     y2 = int(y0 - 1000 * a)
#     cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)
#
# # 霍夫直线变换图像显示
# plt.figure(figsize=(10,8),dpi=100)
# plt.imshow(img[:,:,::-1]),plt.title('霍夫变换线检测')
# plt.xticks([]),plt.yticks([])
# plt.show()

# 霍夫圆变换
import cv2 as cv
import matplotlib.pyplot as plt
# 读取图片，并转换为灰度图
planets=cv.imread(r"D:\opencv_work\opencv_picture\35.jpg")
gay_img=cv.cvtColor(planets,cv.COLOR_BGR2GRAY)
# 进行中值模糊，去噪点
img=cv.medianBlur(gay_img,7)
# 霍夫圆检测
circles=cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,200,param1=100,param2=50,minRadius=0,maxRadius=100)
# 将检测结果绘制在图像上
for x,y,r in circles[0,:]: # 遍历矩阵每一行的数据
    x,y,r=int(x),int(y),int(r)
    # 绘制圆形
    cv.circle(planets,(x,y),r,(0,255,0),2)
    # 绘制圆心
    cv.circle(planets,(x,y),2,(0,0,255),3)
# 图像显示
plt.figure(figsize=(10,8),dpi=100)
plt.imshow(cv.cvtColor(planets, cv.COLOR_BGR2RGB)),plt.title('霍夫圆变换检测')
plt.xticks([]),plt.yticks([])
plt.show()
































































