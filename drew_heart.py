import streamlit as st
from matplotlib import pyplot as plt
import numpy as np

def draw_heart():
    fig, ax = plt.subplots()
    t = np.linspace(0, 2 * np.pi, 100)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    ax.plot(x, y, 'r')
    ax.set_aspect(1)
    plt.axis('off')
    plt.title("drew Heart")
    st.pyplot(fig)

draw_heart()