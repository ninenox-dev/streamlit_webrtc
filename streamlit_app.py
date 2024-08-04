import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, ClientSettings

st.title("WebRTC Webcam Stream with Streamlit")

# Configure WebRTC client settings
client_settings = ClientSettings(
    media_stream_constraints={
        "video": True,
        "audio": False,
    }
)

# Stream the webcam
def main():
    
    webrtc_streamer(
        key="example",
        mode=WebRtcMode.SENDRECV,
        client_settings=client_settings,
    )


if __name__ == "__main__":
    main()
