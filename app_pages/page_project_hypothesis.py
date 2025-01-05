import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect powdery mildew leaves have clear marks/signs, "
        f"typically white dots all around the leaf, that can differentiate them from a healthy leaf \n\n"
        f"* An Image Montage shows that typically a powdery mildew-containing leaf has white marks across it. "
        f"Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another except some whiteness to the image."
    )