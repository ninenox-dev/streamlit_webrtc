import av
# import cv2
# import numpy as np
import streamlit as st
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer
# from ultralytics import YOLO

# โหลดโมเดล YOLOv8
# model = YOLO('yolov8n.pt')

class VideoTransformer(VideoTransformerBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # การตรวจจับวัตถุ
        # results = model(img)

        # # วาดกรอบรอบวัตถุ
        # for result in results:
        #     for box in result.boxes:
        #         x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
        #         conf = box.conf[0]
        #         cls = box.cls[0]
        #         label = f"{model.names[int(cls)]}: {conf:.2f}"
        #         cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        #         cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return av.VideoFrame.from_ndarray(img, format="bgr24")

# สร้างหน้าหลักใน Streamlit
st.title("Webcam Stream with YOLOv8 Object Detection")

# เรียกใช้ webrtc_streamer เพื่อเปิดกล้อง
webrtc_streamer(key="example", video_processor_factory=VideoTransformer)
