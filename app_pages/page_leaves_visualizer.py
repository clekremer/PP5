import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

def page_leaves_visualizer_body():
    st.write("### Leaves Visualizer")
    st.info(
        f"* The client is interested in having a study that visually "
        f"differentiates a parasitised from an healthy leaves.")

    
    version = 'v1'
    if st.checkbox("Difference between average and variability image"):
      
      avg_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
      avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")

      st.warning(
        f"* We notice the average and variability images did not show "
        f"patterns where we could intuitively differentiate one from another. " 
        f"However, a small difference in the color pigment of the average images are seen for both labels.")

      st.image(avg_mildew, caption='Mildew leaf - Average and Variability')
      st.image(avg_healthy, caption='Healthy leaf - Average and Variability')
      st.write("---")

