import cv2
import cv2 as cv
import os
import csv
import time

# ==================== 配置常量 ====================
CSV_PATH = r'D:\opencv_work\checkin_log.csv' # csv文件路径
IMAGE_FOLDER = "checkin_images"  # 相对路径，图片保存在项目文件夹下
WINDOW_NAME = "Face Detection Check-in System" # 显示窗口命名
SCALE_FACTOR = 1.1
MIN_NEIGHBORS = 5


class AttendanceSystem:
    """人脸检测考勤签到系统"""

    def __init__(self):
        """初始化系统：创建文件夹、加载分类器、打开摄像头、读取历史记录"""
        print("[系统] 正在初始化...")

        # 1. 创建照片存储文件夹
        if not os.path.exists(IMAGE_FOLDER):
            os.makedirs(IMAGE_FOLDER)
            print(f"[系统] 已创建照片文件夹: {IMAGE_FOLDER}")

        # 2. 创建 CSV 文件并写入表头（如果不存在）
        if not os.path.exists(CSV_PATH):
            with open(CSV_PATH, 'w', encoding='utf-8-sig', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['时间', '人脸数量', '照片文件'])
            print("[系统] 已创建签到记录文件")

        # 3. 读取历史签到总数
        self.total_checkins = 0
        with open(CSV_PATH, 'r', encoding='utf-8-sig') as f:
            self.total_checkins = max(0, sum(1 for _ in f) - 1)  # 减去表头行
        print(f"[系统] 历史签到总数: {self.total_checkins}")

        # 4. 加载人脸检测分类器
        cascade_path = os.path.join(cv.data.haarcascades, "haarcascade_frontalface_default.xml")
        self.face_cas = cv.CascadeClassifier(cascade_path)
        if self.face_cas.empty():
            print("[错误] 人脸检测分类器加载失败，请检查 OpenCV 安装")
            exit(1)

        # 5. 打开摄像头
        self.cap = cv.VideoCapture(0)
        if not self.cap.isOpened():
            print("[错误] 无法打开摄像头，请检查摄像头是否被占用")
            exit(1)

        # 6. 本次运行期间的签到计数
        self.session_counter = 0

        print("[系统] 初始化完成，按 ESC 退出\n")

    def run(self):
        """主循环：实时检测、处理键盘输入"""
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                print("[错误] 无法读取摄像头画面")
                break

            # 1. 转灰度图（提高检测效率）
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            # 2. 人脸检测
            faceRects = self.face_cas.detectMultiScale(
                gray, scaleFactor=SCALE_FACTOR,
                minNeighbors=MIN_NEIGHBORS, minSize=(32, 32)
            )

            # 3. 当前帧的人脸数量
            current_face_count = len(faceRects)

            # 4. 在画面上绘制人脸框
            for (x, y, w, h) in faceRects:
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

            # 5. 画面信息显示（带黑色描边，任何背景下都清晰）
            # 显示的总数 = 历史总数 + 本次签到数
            display_total = self.total_checkins + self.session_counter

            # 第1行：当前人脸数
            cv.putText(frame, f"Faces: {current_face_count}", (10, 30),
                       cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 4)  # 黑色描边
            cv.putText(frame, f"Faces: {current_face_count}", (10, 30),
                       cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)  # 白色文字

            # 第2行：总签到数
            cv.putText(frame, f"Total: {display_total}", (10, 55),
                       cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 4)
            cv.putText(frame, f"Total: {display_total}", (10, 55),
                       cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            # 6. 无人脸提示
            if current_face_count == 0:
                cv.putText(frame, "NO FACE DETECTED", (250, 100),
                           cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 4)
                cv.putText(frame, "NO FACE DETECTED", (250, 100),
                           cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            # 7. 显示画面
            cv.imshow(WINDOW_NAME, frame)

            # 8. 键盘事件处理
            key = cv2.waitKey(1) & 0xFF

            if key == 27:  # ESC 退出
                print(f"\n[系统] 程序退出，本次签到次数: {self.session_counter}")
                break

            elif key == 32:  # 空格签到
                if current_face_count > 0:
                    self._checkin(frame, current_face_count)
                else:
                    print("[签到失败] 未检测到人脸，请面对摄像头")

            elif key == 108 or key == 76:  # L / l 查看历史
                self._show_history()

            elif key == 99 or key == 67:  # C / c 清空记录
                self._clear_records()

        # 释放资源
        self.cap.release()
        cv.destroyAllWindows()

    def _checkin(self, frame, face_count):
        """执行签到：保存图片、记录 CSV、更新计数"""
        # 生成时间戳
        timestamp_img = time.strftime("%Y%m%d_%H%M%S")
        timestamp_log = time.strftime("%Y-%m-%d %H:%M:%S")

        # 保存图片
        filename = f"{IMAGE_FOLDER}/checkin_{timestamp_img}.jpg"
        cv2.imwrite(filename, frame)

        # 追加 CSV 记录
        with open(CSV_PATH, 'a', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp_log, face_count, filename])

        # 更新计数
        self.session_counter += 1

        print(f"[签到成功] 时间：{timestamp_log}，检测到人脸数：{face_count}，总签到次数：{self.total_checkins + self.session_counter}")

    def _show_history(self):
        """显示所有历史签到记录"""
        if not os.path.exists(CSV_PATH):
            print("[提示] 暂无签到记录")
            return

        with open(CSV_PATH, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            rows = list(reader)

        if len(rows) <= 1:
            print("[提示] 暂无签到记录")
            return

        print("\n" + "=" * 50)
        print("签到历史记录")
        print("=" * 50)
        for i, row in enumerate(rows):
            if i == 0:
                print(f"【表头】 {' | '.join(row)}")
                print("-" * 50)
            else:
                print(f"  {' | '.join(row)}")
        print("=" * 50 + "\n")

    def _clear_records(self):
        """清空所有签到记录（CSV 文件 + 照片文件夹）"""
        confirm = input("[确认] 清空所有签到记录？(y/n): ")
        if confirm.lower() != 'y':
            print("[取消] 未执行清空操作")
            return

        # 清空 CSV，保留表头
        with open(CSV_PATH, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['时间', '人脸数量', '照片文件'])

        # 清空照片文件夹
        if os.path.exists(IMAGE_FOLDER):
            for filename in os.listdir(IMAGE_FOLDER):
                if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                    file_path = os.path.join(IMAGE_FOLDER, filename)
                    os.remove(file_path)

        # 重置计数器
        self.total_checkins = 0
        self.session_counter = 0

        print("[系统] 所有签到记录已清空（CSV + 照片）")


# ==================== 程序入口 ====================
if __name__ == '__main__':
    system = AttendanceSystem()
    system.run()