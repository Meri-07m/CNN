import cv2
from ultralytics import YOLO

model_path = "best.pt"

model = YOLO(model_path)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("YOLOv8 Webcam Inference", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


