import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* **Hypothesis 1:** Cherry leaves which are infected with powdery mildew have a white coating and spots on its sureface."
        f" Infected leaves can clearly be distinguished from healthy leaves"
        f" **Validation:** Check visualisation page and compare average image and variability of healthy and infected leaves."
        f" Check differences of average healthy and infected leaves."
        f" Average Image, Variability Image and difference of average healthy and infected leaves did not reveal any clear pattern"
        f" to differentiate one from another except some whiteness to the image.\n\n"
        f" **Hypothesis 2:** An Image Montage shows that mildew infected leaves have white coats on their surface."
        f" **Validation:** Check visualisation page and create image montages of 24 healthy and 24 infected leaves and compare the differences."
        f" Comparing 24 healthy and infected leaves from the Montage differences are intuitively visible. \n\n"
        f" **Hypothesis 3:** An ML based model is used in an image visualizer to differentiate between healthy and infected cherry leafs."
        f" The model should have a minimum validity of 97% accuracy."
        f" By the help of this ML based image visualizer the process should become much more effective" 
        f" for the company in terms of time and money saving."
        f" **Validation:** Check mildew detection page and load example leaf images of healthy and infected leaves and check the results."
        f" The model is validated with > 97% accuracy. All tested example images were predicted correctly."
    )
