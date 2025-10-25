import numpy as np
import cv2 as cv
import streamlit as st

uploaded_img = st.file_uploader(
    "Upload image", accept_multiple_files=False, type=["jpg", "png"]
)

if uploaded_img is not None:
    st.image(uploaded_img)