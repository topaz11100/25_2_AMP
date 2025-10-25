import numpy as np
import cv2 as cv
import streamlit as st

def read_as_cv2_image(file) -> np.ndarray:
    """Streamlit UploadedFile -> OpenCV 이미지(np.ndarray, BGR/RGBA)."""
    data = file.getvalue()                 # 바이트 얻기 (read() 대신 getvalue() 쓰면 포인터 신경 X)
    arr  = np.frombuffer(data, np.uint8)   # uint8 1D 배열
    img  = cv.imdecode(arr, cv.IMREAD_UNCHANGED)  # GRAY/BGR/RGBA 그대로
    if img is None:
        raise ValueError("이미지 디코딩 실패")
    return img

def to_streamlit_color(img: np.ndarray) -> np.ndarray:
    """OpenCV(BGR/RGBA/GRAY) -> Streamlit용 RGB/RGBA/GRAY."""
    if img.ndim == 2:
        return img  # GRAY
    if img.shape[2] == 3:
        return cv.cvtColor(img, cv.COLOR_BGR2RGB)  # BGR -> RGB
    if img.shape[2] == 4:
        # BGRA -> RGBA
        b, g, r, a = cv.split(img)
        return cv.merge([r, g, b, a])
    raise ValueError(f"예상치 못한 채널 수: {img.shape}")

src_col, rst_col = st.columns(2)

uploaded_img = st.file_uploader(
    "Upload image", accept_multiple_files=False, type=["jpg", "png"]
)

if uploaded_img is not None:
    with src_col:
        st.image(uploaded_img)

    rst = read_as_cv2_image(uploaded_img)
    rst = cv.bitwise_not(rst)
    rst = to_streamlit_color(rst)

    with rst_col:
        st.image(rst)
