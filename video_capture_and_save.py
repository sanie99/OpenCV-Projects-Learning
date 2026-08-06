import cv2
import streamlit as st

st.title("Webcam Streaming Capture")
action = st.selectbox("Select action", ["Stream only", "Stream and save", "Exit"])

def stream_only():
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if not success:
            break
        cv2.imshow("Webcam Streaming", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        camera.release()
        cv2.destroyAllWindows()

def save_stream():
    camera = cv2.VideoCapture(0)
    frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    codec = cv2.VideoWriter_fourcc(*'XVID')
    recorder = cv2.VideoWriter("first_video.mp4", codec, 20, (frame_width, frame_height))
    while True:
        success, frame = camera.read()
        if not success:
            break
        recorder.write(frame)
        cv2.imshow("Webcam Streaming", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()
    recorder.release()
    cv2.destroyAllWindows()

if action == "Stream only":
    stream_only()

if action == "Stream and save":
    save_stream()

if action == "Exit":
    st.stop()
