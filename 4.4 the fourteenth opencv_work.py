# # Fast和ORB算法

# Fast 算法
# 原理：若一个像素周围有一定数量的像素与该点像素值不同，则认为其为角点。
# API：cv.FastFeatureDetector_create()

# import cv2 as cv
# import numpy as np
#
# # 1. 读取图像
# img = cv.imread(r"D:\opencv_work\opencv_picture\37.jpg")
# if img is None:
#     print("图像读取失败，请检查路径是否正确！")
#     exit()
#
# # 2. Fast 角点检测
# fast = cv.FastFeatureDetector_create(threshold=30)
#
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# kp = fast.detect(gray, None)
#
# # 关键修正：第一个参数用彩色图 img，而不是 gray
# # 第三个参数传 None，让函数返回绘制好的新图像
# img2 = cv.drawKeypoints(
#     img, kp, None,
#     color=(0, 255, 0),
#     flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
# )
#
# # 输出参数
# print("Threshold: {}".format(fast.getThreshold()))
# print("nonmaxSuppression: {}".format(fast.getNonmaxSuppression()))
# print("neighborhood: {}".format(fast.getType()))
# print("Total Keypoints with nonmaxSuppression: {}".format(len(kp)))
#
# # 关闭非极大值抑制
# fast.setNonmaxSuppression(False)
# kp2 = fast.detect(gray, None)
# print("Total Keypoints without nonmaxSuppression: {}".format(len(kp2)))
#
# img3 = cv.drawKeypoints(
#     img, kp2, None,
#     color=(0, 255, 0),
#     flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
# )
#
# # 用 OpenCV 显示，完全避开 matplotlib 的递归错误
# cv.imshow("with NMS", img2)
# cv.imshow("without NMS", img3)
# cv.waitKey(0)
# cv.destroyAllWindows()


# ORB算法
# 原理：是 FAST 算法和 BRIEF 算法的结合，解决了 FAST 没有方向、BRIEF 不具备旋转不变性的问题。
# API：cv.ORB_create()（新版推荐写法）/ cv.xfeatures2d.orb_create()（旧版写法）

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# 1.读取图像
img = cv.imread(r"D:\opencv_work\opencv_picture\37.jpg")

# 2 ORB角点检测
# 2.1 实例化ORB对象

# nfeatures：特征点的最大数量，控制检测到的关键点总数
orb = cv.ORB_create(nfeatures=5000)
# 2.2 关键点检测，并计算特征描述符
kp,des = orb.detectAndCompute(img,None)

print(des.shape)
# 3 将关键点绘制在图像上
img2 = cv.drawKeypoints(img,kp,None,color=(0,255,0),flags=0)
# 4 图显
plt.figure(figsize=(10,8),dpi=100)
plt.imshow(img2[:,:,::-1])
plt.title('ORB角点检测')
plt.xticks([]),plt.yticks([])
plt.show()




