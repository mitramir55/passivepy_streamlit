import streamlit as st
import pandas as pd
import numpy as np


st.title('PassivePy')


st.write("Our aim with this work is to create a reliable (e.g., passive voice judgments are consistent), valid (e.g., passive voice judgments are accurate), flexible (e.g., texts can be assessed at different units of analysis), replicable (e.g., the approach can be performed by a range of research teams with varying levels of computational expertise), and scalable way (e.g., small and large collections of texts can be analyzed) to capture passive voice from different corpora for social and psychological evaluations of text. To achieve these aims, we introduce PassivePy, a fully transparent and documented Python library.")


link = 'Please visit our [GitHub](https://github.com/mitramir55/PassivePy) if you want to see the code or make any contributions.'
st.markdown(link, unsafe_allow_html=True)

link = 'If you use this package, please cite it as: Sepehri, Amir, David M. Markowitz, and Mitra Mir. 2022. “Passivepy: A Tool to Automatically Identify Passive Voice in Big Text Data.” PsyArXiv. February 3. doi:10.31234/osf.io/bwp3t.'
st.markdown(link, unsafe_allow_html=True)
