from ultralytics import YOLO

yolo = YOLO("./yolov8n.pt", task="detect") 

#result = yolo(source="./ultralytics/assets/bus.jpg") #对图像检测
#result = yolo(source="screen") #对桌面检测
#result = yolo(source="0") #打开摄像头
result = yolo(source="./ultralytics/assets/AIlabs.jpg",save=True) #对图像检测并保存结果
#result = yolo(source="./ultralytics/assets/bus.jpg",save=True,conf=0.5) #对图像检测并保存结果,精度降低