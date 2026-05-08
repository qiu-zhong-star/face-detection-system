# 视频读写

# 视频读取与显示
# OpenCV 视频读取核心 API
# 创建视频读取对象
# cap = cv.VideoCapture(filepath)
# filepath：视频文件路径，也可以传入设备索引（如0表示电脑默认摄像头）

# 获取视频属性

# retval = cap.get(propId)
# propId：属性索引（0~18），常用的有：
# 属性索引	含义
# cv.CAP_PROP_FRAME_WIDTH(3)	视频宽度
# cv.CAP_PROP_FRAME_HEIGHT(4)	视频高度
# cv.CAP_PROP_FPS(5)	        视频帧率
# cv.CAP_PROP_FRAME_COUNT(7)	视频总帧数

# 显示帧：cv.imshow("window_name", frame)
# 控制播放速度：cv.waitKey(25)（单位毫秒，25ms 对应约 40fps 的播放速度）
# 释放资源：cap.release()
# 关闭窗口：cv.destroyAllWindows()

# import cv2 as cv
# import numpy as np
# # 1.获取视频对象
# cap = cv.VideoCapture('D:\opencv_work\cat.wmv')
# # 2.判断是否读取成功
# while cap.isOpened():
#     # 3.获取每一帧图像
#     ret,frame = cap.read()
#     # 4.获取成功显示图像
#     if ret == True:
#         cv.imshow('frame',frame)
#     # 5.每一帧间隔为25ms
#     if cv.waitKey(25) & 0xFF == ord('q'):
#         break
#
#
# # 6.释放视频对象
# cap.release()
# cv.destoryAllwindows()


# 视频文件的保存
# 在 OpenCV 中，保存视频使用的是 cv2.VideoWriter 对象，关键 API 如下：
# 1. 创建视频写入对象
# out = cv2.VideoWriter(filename, fourcc, fps, frameSize)
# 参数说明：
# filename：视频文件的保存路径（如 output.avi）
# fourcc：视频编解码器的 4 字节代码
# fps：输出视频的帧率
# frameSize：视频帧的尺寸（宽，高）

# 2. 设置视频编解码器
# retval = cv2.VideoWriter_fourcc(c1, c2, c3, c4)
# 参数说明：
# c1,c2,c3,c4：编解码器的 4 字节代码，可在 fourcc.org 查看完整列表，不同平台支持的编解码器不同。
# 常见配置：
# Windows：DIVX（对应 .avi 格式）
# macOS/Linux：MJPG（对应 .mp4）、DIVX（对应 .avi）、X264（对应 .mkv）

import cv2 as cv
import numpy as np
# 1.读取视频
cap = cv.VideoCapture('D:\opencv_work\cat.wmv')
# 2.获取图像的属性（宽和高），并将转换为整数
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# 3.创建保存视频的对象，设置编码格式，帧率，图像的宽高等
out = cv.VideoWriter('outpy.avi',cv.VideoWriter_fourcc('D','I','V','X'),10,(frame_width,frame_height))
while True:
    # 4.获取视频中的每一帧图像
    ret,frame = cap.read()
    if ret == True:
        # 5.将每一帧图像写入到输出文件中
        out.write(frame)
    else :
        break

# 6.释放资源
# cap.release()
out.release()
# cv.destoryAllwindows()




















