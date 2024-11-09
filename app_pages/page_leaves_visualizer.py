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