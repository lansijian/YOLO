from ultralytics import YOLO
import cv2

# Load a YOLOv8 model
model = YOLO('yolov8n.pt')

# Load an image
img = cv2.imread('image.jpg')

# Perform object detection
results = model(img)

# Print the detected objects
print(results)