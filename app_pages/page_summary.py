import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.header("General Information")

    st.info(
        f" Powdery mildew is a fungal disease on cherry trees."
        f" Infected plants display white powdery coat on the leaves and stems."
        f" The disease occurs mostly in high humid and moderate temperatures."
        f" It can have severe and negative impact on growth, by slowing down the growth of the plant"
        f" and can infect the fruits as well."
    )

    st.warning(
        f"**Project Dataset**\n\n"
        f"\n The dataset was dowloaded from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).\n"
        f"It contains 2104 healthy leaves and 2104 affected leaves. "
    )

    st.success(
        f"The project has two business requirements:\n\n"
        f"1 - The client is interested in conducting a study to visually differentiate"
        f" a healthy cherry leaf from one with powdery mildew.\n\n"
        f"2 - The client is interested in predicting if a cherry leaf is healthy"
        f" or contains powdery mildew."
    )

    st.write(
        f"For more information, please visit my GitHub Repo **read** the "
        f"[README file](https://github.com/clekremer/PP5/blob/main/README.md).")
