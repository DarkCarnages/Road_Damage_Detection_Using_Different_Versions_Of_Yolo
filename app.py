import streamlit as st
import cv2
import numpy as np
import tempfile
from ultralytics import YOLO

st.set_page_config(page_title="Multi YOLO Tester", layout="wide")

st.title("Multi Model YOLO Inference")

@st.cache_resource
def load_models():
    #load n number of models you want 
    return {
        "YOLOv7": YOLO("models/yolov7.pt"),
        "YOLOv8-S": YOLO("models/yolov8s.pt"),
        "YOLOv8-M": YOLO("models/yolov8m.pt"),
        "YOLOV8-L": YOLO("path to yolov8 l best.pt"),
        "YOLOv11-S": YOLO("models/yolov11s.pt"),
        "YOLOv11-M": YOLO("models/yolov11m.pt"),
    }

models = load_models()

file = st.file_uploader(
    "Upload Image or Video",
    type=["jpg", "jpeg", "png", "mp4", "avi", "mov"]
)

def process_image(image):
    best_conf = 0.0
    best_output = None
    best_model = None

    for name, model in models.items():
        results = model(image, conf=0.25, verbose=False)
        r = results[0]

        if r.boxes is None or len(r.boxes) == 0:
            continue

        conf = float(r.boxes.conf.max().cpu().numpy())

        if conf > best_conf:
            best_conf = conf
            best_output = r.plot()
            best_model = name

    return best_model, best_conf, best_output

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    best_conf = 0.0
    best_model = None
    best_frames = None

    for name, model in models.items():
        model_frames = []
        model_best_conf = 0.0

        for frame in frames:
            results = model(frame, conf=0.25, verbose=False)
            r = results[0]

            if r.boxes is not None and len(r.boxes) > 0:
                conf = float(r.boxes.conf.max().cpu().numpy())
                model_best_conf = max(model_best_conf, conf)

            model_frames.append(r.plot())

        if model_best_conf > best_conf:
            best_conf = model_best_conf
            best_model = name
            best_frames = model_frames

    return best_model, best_conf, best_frames

if file is not None:
    file_type = file.type

    if file_type.startswith("image"):
        image = np.frombuffer(file.read(), np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        model_name, conf, output = process_image(image)

        if output is not None:
            st.subheader(f"Best Model: {model_name}")
            st.write(f"Max Confidence: {conf:.4f}")
            st.image(output, channels="BGR")
        else:
            st.warning("No detections found")

    else:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(file.read())
        tfile.close()

        model_name, conf, frames = process_video(tfile.name)

        if frames is not None:
            st.subheader(f"Best Model: {model_name}")
            st.write(f"Max Confidence: {conf:.4f}")
            for frame in frames:
                st.image(frame, channels="BGR")
        else:
            st.warning("No detections found")
