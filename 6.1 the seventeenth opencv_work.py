# 人脸检测
# 使用机器学习的方法完成人脸检测
# 那我们就利用这些文件来识别人脸，眼睛等。检测流程如下：
# 读取图片，并转换成灰度图
# 实例化人脸和眼睛检测的分类器对象
# # 实例化级联分类器
# classifier = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
# # 加载分类器
# classifier.load('haarcascade_frontalface_default.xml')
# rect = classifier.detectMultiScale(gray, scaleFactor, minNeighbors, minSize, maxsize)
# 参数说明：
# gray: 要进行检测的人脸图像（灰度图）
# scaleFactor: 前后两次扫描中，搜索窗口的比例系数
# minNeighbors: 目标至少被检测到minNeighbors次才会被认为是目标
# minSize和maxsize: 目标的最小尺寸和最大尺寸
# 将检测结果绘制出来就可以了。


# # 图片人脸检测
# import cv2 as cv
# import matplotlib.pyplot as plt
# import os
# # 1.以灰度图的形式读取图片
# img = cv.imread(r"D:\opencv_work\opencv_picture\39.jpg")
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#
# # 2.实例化OpenCV人脸和眼睛识别的分类器
# # 获取当前脚本所在目录
# base_dir = os.path.dirname(os.path.abspath(__file__))
#
# # 拼接 XML 文件的绝对路径
# face_cas = cv.CascadeClassifier(
#     cv.data.haarcascades + "haarcascade_frontalface_default.xml"
# )
# eye_cas = cv.CascadeClassifier(
#     cv.data.haarcascades + "haarcascade_eye.xml"
# )
# # 3.调用识别人脸
# faceRects = face_cas.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(32, 32))
# for faceRect in faceRects:
#     x, y, w, h = faceRect
#     # 框出人脸
#     cv.rectangle(img, (x, y), (x + w, y + h), (0,255, 0), 3)
#     # 4.在识别出的人脸进行眼睛的检测
#     roi_color = img[y:y + h, x:x + w]
#     roi_gray = img[y:y + h, x:x + w]
#     eyes = eye_cas.detectMultiScale(roi_gray)
#     for (ex,ey,ew,eh) in eyes:
#         cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
# # 5.检测结果的绘制
# plt.figure(figsize=(8,6),dpi=100)
# plt.imshow(img[:,:,::-1])
# plt.title('图片人脸检测结果')
# plt.xticks([]),plt.yticks([])
# plt.show()


# 视频人脸检测
import cv2 as cv
import matplotlib.pyplot as plt
import os
# 1.读取视频
cap = cv.VideoCapture(r'D:\opencv_work\face.wmv')
# 2.在第一帧数据中进行人脸识别
while cap.isOpened():
    ret,frame = cap.read()
    if ret==True:
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        #3. 实例化OpenCV人脸识别的分类器

        face_cas = cv.CascadeClassifier(
            os.path.join(cv.data.haarcascades, "haarcascade_frontalface_default.xml")
        )
        eye_cas = cv.CascadeClassifier(
            os.path.join(cv.data.haarcascades, "haarcascade_eye.xml")
        )
        #4. 调用人脸识别
        faceRects = face_cas.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(32, 32))
        for faceRect in faceRects:
            x, y, w, h = faceRect
            # 框出人脸
            cv.rectangle(frame, (x, y), (x + w, y + h), (0,255, 0), 3)
        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
# 5.释放资源
cap.release()
cv.destroyAllWindows()










