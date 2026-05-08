import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# 读取图像
img = cv.imread(r"D:\opencv_work\.venv\3.1.jpg", 0)
# opencv显示图像
# cv.imshow("flower", img)
# cv.waitKey(0)
# cv.destroyAllWindows()
# matplotlib显示图像
plt.imshow(img,cmap=plt.cm.gray)  #RGB通道翻转
plt.show()
# 图像保存
cv.imwrite(r"D:\opencv_work\.venv\picture.jpg",img)


