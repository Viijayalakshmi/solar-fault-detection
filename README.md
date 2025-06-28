Solar Cell Fault Detection using CNN & Simulated YOLOv11

This project detects solar panel faults (like cracks, dirt, and hotspots) using deep learning.

How to Run:

1. Open Command Prompt
2. Go to this folder using cd command
3. Install required packages:
   pip install -r requirements.txt
4. Run this command to predict image:
   python main.py
5. To show bounding box like YOLO:
   python yolo_simulation.py

Project Files:

- main.py → Detects Fault or Normal
- yolo_simulation.py → Draws red box (simulated YOLO)
- models/ → Has the trained model file (.h5)
- test_images/ → Sample test images to try

Project by:
Vijaya Lakshmi S and Team  
SRM TRP Engineering College
