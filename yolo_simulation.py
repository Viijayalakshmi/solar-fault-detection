import cv2

def detect_fault_yolo_simulation(image_path):
    img = cv2.imread(image_path)
    img_resized = cv2.resize(img, (512, 512))
    label = "Faulty"
    confidence = 0.87
    start_point = (100, 100)
    end_point = (300, 300)
    cv2.rectangle(img_resized, start_point, end_point, (0, 0, 255), 2)
    cv2.putText(img_resized, f"{label}: {confidence*100:.1f}%", (100, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
    cv2.imshow("YOLOv11 - Simulated Detection", img_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()