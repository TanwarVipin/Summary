import streamlit as st
from datetime import datetime
import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.summary import doc

try:
    import subprocess
    
    @st.cache_resource
    def download_en_core_web_sm():
        subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
except Exception as e:
    raise CustomException(e,sys)

try:

    title_style = '''
    <style>
    h1 {
    color: #FF0000; /* Change to your desired title color */
    font-family: 'Arial', sans-serif; /* Change to your desired font family */
    }
    </style>
    '''

    # Apply the custom title style
    st.markdown(title_style, unsafe_allow_html=True)


    st.title('Text Summarization App',)






    text=st.text_area("Enter Your Text for Summary")

    if st.button('Summary'):

        if text:
            summary=doc(text=text)

            

            logging.info("Summary Created Succesfully")

            st.subheader("Summary of The Article:")

            st.write(summary)

    

except Exception as e:
    raise CustomException(e,sys)







