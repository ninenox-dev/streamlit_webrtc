import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, ClientSettings

st.title("WebRTC Webcam Stream with Streamlit")

webrtc_streamer(
    key="example",
    mode=WebRtcMode.SENDRECV,
    client_settings=ClientSettings(
        media_stream_constraints={
            "video": True,
            "audio": False,
        }
    ),
)
