import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
# 创建画布
img=np.zeros((512,512,3),np.uint8)
# 绘制图形
# 直线绘制
cv.line(img,(0,0),(511,511),(255,0,0),5)
# 圆形绘制
cv.circle(img,(256,256),60,(0,0,255),5)
# 矩形绘制
cv.rectangle(img,(100,100),(400,400),(0,255,0),5)
# 文字绘制
cv.putText(img,"ambition",(100,150),cv.FONT_HERSHEY_SIMPLEX,5,(255,255,255),3)
# 结果显示
plt.imshow(img[:,:,::-1])
plt.show()
















