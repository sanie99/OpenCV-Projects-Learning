import streamlit as st
import cv2
import numpy as np

st.title("Image Grayscale Converter")
image_path = st.text_input("Upload image path")
image = cv2.imread(image_path)

def display_image(convert_display=False):
    if convert_display:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        cv2.imshow("Converted Gray Image", gray_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        st.text("No image to convert.")

def save_converted_image(save_image=False):
    if save_image:
        file_name_input = st.text_input("Enter file name along with format [.jpg , .png]: ")
        file_name = file_name_input+'.jpg'
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        if cv2.imwrite(file_name, gray_image):
            st.success(f'Image saved successfully as {file_name}')
    else:
        st.text("No image to save.")

def display_options():
    st.text("Would you like to?")

    convert_display = st.button("Convert to Grayscale and display it")
    if convert_display:
        display_image(convert_display=True)

    save_image = st.button("Save Grayscale Image")
    if save_image:
        save_converted_image(save_image=True)


if image is not None:
    st.success("Image uploaded successfully!")
    display_options()
else: 
    st.error("Error: image not found.")

