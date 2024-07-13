import cv2
from ultralytics import YOLO

# Load the YOLOv8 pose estimation model
model = YOLO('yolov8n-pose.pt')  # Replace with the actual path to your model

# Open the video file
video_path = "movements.mp4"
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error opening video file")

# Loop through the frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Use YOLO model to detect poses in the frame
    results = model(frame, show=False, conf=0.3)
    
    # Get the number of people detected in the frame
    num_people = len(results.xyxy[0])
    
    if num_people == 0:
        print("No people detected in the frame")
    elif num_people > 1:
        print(f"More than one person detected ({num_people} people)")
    else:
        print("One person detected")
        
        # Use the second model to check for motion (this is a placeholder, replace with actual implementation)
        motion_detected = True  # Replace with actual motion detection code
        
        if motion_detected:
            # Use the third model to classify the type of motion (this is a placeholder, replace with actual implementation)
            motion_type = "unknown"  # Replace with actual motion classification code
            print(f"Motion detected: {motion_type}")
        else:
            print("No significant motion detected")
    
    # Display the frame (optional)
    cv2.imshow('Frame', frame)
    
    # Press Q to quit the video
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close display windows
cap.release()
cv2.destroyAllWindows()
