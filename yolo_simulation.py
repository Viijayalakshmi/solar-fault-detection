import cv2
import numpy as np
import matplotlib.pyplot as plt

def simulate_yolo_prediction(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("❌ Could not load image:", image_path)
        return

    height, width = img.shape[:2]

    # Simulated bounding box for "fault"
    start_point = (int(width * 0.3), int(height * 0.3))
    end_point = (int(width * 0.6), int(height * 0.6))
    color = (0, 0, 255)  # Red
    thickness = 2

    image_with_box = cv2.rectangle(img.copy(), start_point, end_point, color, thickness)

    # Convert BGR to RGB for displaying with matplotlib
    image_rgb = cv2.cvtColor(image_with_box, cv2.COLOR_BGR2RGB)

    plt.imshow(image_rgb)
    plt.title("YOLOv11 - Simulated Fault Detection")
    plt.axis('off')
    plt.show()

# Example usage
simulate_yolo_prediction("test_images/sample.jpg")
