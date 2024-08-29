import cv2
from ultralytics import YOLO
import numpy as np

# 加载你自己训练的YOLOv8模型
model_path = r"D:\ultralytics-8.1.0\runs\train\exp5\weights\best.pt"
model = YOLO(model_path)

# 打开视频文件
video_path = "D:/ultralytics-8.1.0/vision_work/armor.avi"
cap = cv2.VideoCapture(video_path)

# 获取视频尺寸
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 视频中心点
center_point = (width / 2, height / 2)

# 相机焦距和主点位置
focal_length = 1000  # 假设焦距为1000像素
principal_point = (width / 2, height / 2)  # 假设主点位置在图像中心

# 物体的3D点
object_points = np.array([[0, 0, 0],
                          [1, 0, 0],
                          [0, 1, 0],
                          [0, 0, 1]], dtype=np.float32)

# 用于存储前一帧的中心点位置
prev_centers = {}

# 循环遍历视频帧
while cap.isOpened():
    # 从视频读取一帧
    success, frame = cap.read()

    if success:
        # 在帧上运行YOLOv8追踪，持续追踪帧间的物体
        results = model.track(frame, persist=True)
        boxes = results[0].boxes.xyxy  # 获取边界框

        # 处理每个检测到的物体
        for i, box in enumerate(boxes):
            x1, y1, x2, y2 = box
            x_center = (x1 + x2) / 2
            y_center = (y1 + y2) / 2

            # 计算中心点
            center = (x_center, y_center)

            # 如果物体在前一帧中也被检测到，计算中心点的位置变化
            if i in prev_centers:
                prev_center = prev_centers[i]
                delta_x = x_center - prev_center[0]
                delta_y = y_center - prev_center[1]
                displacement = np.sqrt(delta_x**2 + delta_y**2)
            else:
                delta_x, delta_y, displacement = 0, 0, 0

            # 更新当前物体的中心点位置
            prev_centers[i] = center

            # 使用近似方法计算物体的位置
            z = focal_length / np.sqrt((x_center - principal_point[0])**2 + (y_center - principal_point[1])**2)
            position = np.dot(object_points, np.array([[z, 0, 0],
                                                       [0, z, 0],
                                                       [0, 0, z]]).T).T

            # 计算物体相对于视频中心点的位置变化
            delta_center_x = x_center - center_point[0]
            delta_center_y = y_center - center_point[1]
            displacement_center = np.sqrt(delta_center_x**2 + delta_center_y**2)

            # 绘制边界框和中心点位置变化
            label = f"({position[0][0]:.2f}, {position[0][1]:.2f}, {position[0][2]:.2f}) ({displacement_center:.2f} pixels)"
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
            cv2.circle(frame, (int(x_center), int(y_center)), 5, (0, 255, 0), -1)
            cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # 展示带注释的帧
        cv2.imshow("YOLOv8 Tracking", frame)

        # 如果按下'q'则退出循环
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # 如果视频结束则退出循环
        break

# 释放视频捕获对象并关闭显示窗口
cap.release()
cv2.destroyAllWindows()
