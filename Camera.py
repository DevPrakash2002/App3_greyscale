import streamlit as st
from PIL import Image

with st.expander('Start Camera'):
    # start the Camera
    camera_image = st.camera_input('Camera')

print(camera_image)
if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_Image = img.convert("L")

    # Render the grayscale imagen the webpage
    st.image(gray_Image)
