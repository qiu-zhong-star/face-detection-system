markdown
# 人脸检测签到模拟系统

基于 OpenCV 的人脸检测签到系统，支持实时检测、签到拍照、记录管理。

## 功能特点

- **实时人脸检测**：使用 Haar Cascade 分类器，绿色矩形框标注人脸位置
- **签到功能**：按空格键签到，自动保存照片到本地
- **记录管理**：CSV 格式存储签到记录，支持查看历史（L 键）和清空记录（C 键）
- **画面信息显示**：实时显示当前人脸数和总签到数
- **无人脸提示**：检测不到人脸时，画面中央显示红色提示文字

## 技术栈

- Python 3.x
- OpenCV（人脸检测）
- CSV（数据存储）

## 使用方法

1. 安装依赖：
   ```bash
   pip install opencv-python
运行程序：

bash
python face_detection_system.py
按空格键签到，L 键查看记录，C 键清空，ESC 退出

键盘操作
按键	功能
空格	签到（需检测到人脸）
L	查看历史签到记录
C	清空所有记录（需确认）
ESC	退出程序
项目结构
text
face-detection-system/
├── face_detection_system.py   # 主程序
├── checkin_log.csv            # 签到记录（自动生成）
├── checkin_images/            # 签到照片（自动生成）
└── README.md                  # 项目说明
运行效果
摄像头打开后，实时检测人脸并用绿色矩形框标注

左上角显示当前人脸数和总签到数

按空格键签到，控制台输出签到成功信息

按 L 键查看所有历史签到记录

按 C 键清空所有记录和照片

作者
GitHub：qiu-zhong-star
