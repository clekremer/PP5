import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* Cherry leaves which are infected with powdery mildew have a white coating and spots on its sureface."
        f"* Infected leaves can clearly be distinguished from healthy leaves"
        f"and validation can be done by comparing healthy and infected leaves based on images. \n\n"
        f"* Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another except some whiteness to the image."
        f"* An Image Montage shows that mildew infected leaves have white coats on their surface. \n\n"
        f"* An ML based model is used in an image visualizer to differentiate between healthy and infected cherry leafs."
        f"* The model should have a minimum validity of 97% accuracy"
        f"* By the help of this ML based image visualizer the process should become much more effective" 
        f"for the company in terms of time and money saving"
    )