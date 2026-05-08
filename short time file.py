import cv2 as cv
import os

face_cas = cv.CascadeClassifier(
    os.path.join(cv.data.haarcascades, "haarcascade_frontalface_default.xml")
)
eye_cas = cv.CascadeClassifier(
    os.path.join(cv.data.haarcascades, "haarcascade_eye.xml")
)

# 验证加载成功
if face_cas.empty():
    print("人脸分类器加载失败")
    exit()
if eye_cas.empty():
    print("眼睛分类器加载失败")
    exit()

print("加载成功")