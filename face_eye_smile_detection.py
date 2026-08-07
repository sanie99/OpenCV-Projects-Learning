import cv2

model_path = "face_detection_yunet_2023mar.onnx"

cam = cv2.VideoCapture(0)
if not cam.isOpened():
  print("Error: Could not open webcam.")
  exit()

w = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

detector = cv2.FaceDetectorYN.create(
    model=model_path,
    config="",
    input_size=(w, h),
    score_threshold=0.6,  
    nms_threshold=0.3,
    top_k=5000,
)

while True:
  success, frame = cam.read()
  if not success:
    break

  frame = cv2.flip(frame, 1)

  _, faces = detector.detect(frame)

  if faces is not None:
    for face in faces:
      box = face[:4].astype(int)
      cv2.rectangle(
          frame, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), (0, 255, 0), 2
      )
      features = face[4:14].reshape((5,2)).astype(int)
      cv2.rectangle(frame, (features[0][0] - 50, features[0][1] - 30), (features[1][0] + 50, features[1][1] + 30), (255, 0, 0), 2)
      cv2.putText(frame, "Eyes Detected", (features[0][0] - 50, features[0][1] - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)


  cv2.imshow("Real-Time Face Detection", frame)

  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

cam.release()
cv2.destroyAllWindows()
