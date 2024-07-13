import cv2
from ultralytics import YOLO

# Load the YOLOv8 pose estimation model
model = YOLO('yolov8n-pose.pt')  # Replace with the actual path to your model

results = model(source="movements.mp4", show=True, conf=0.3, save=True)