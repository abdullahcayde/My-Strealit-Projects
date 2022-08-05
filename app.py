import streamlit as st
import datetime
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title ="Forecasting Tool")

tabs = ["Forecasting","Data Visualization","About"]

page = st.sidebar.radio("Tabs",tabs)

if page == "Forecasting":
    st.markdown("<h1 style='text-align: center;'>Forecasting</h1>", unsafe_allow_html=True)
    st.button('Ara')
    st.button('Taramak')

    with text_column:
        st.subheader('Integrate your Lottie Animations Inside Your Streamlit App')
        st.write(
            '''
            Learn how to use Lottie Files in Streamlit !!!!!!
            Animations are fun.
            '''
        )