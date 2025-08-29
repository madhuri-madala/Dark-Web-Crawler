import streamlit as st
import os 
from bs4 import BeautifulSoup
# from nltk.stem import PorterStemmer
import utils
import pandas as pd
from transformers import AutoTokenizer



def display_classification_results(df):
    st.success('Classification Results')
    st.write(df)
    st.bar_chart(df.set_index('label'))


def main():

    st.title('Dark Web Crawler')

    link = st.text_input('paste web link here')
    btn = st.button('crawl')

    text_file_path = os.path.join('./data', 'data.txt')

    if link and btn:
        op = utils.fetch_text_from_url(link)
        print(op)

        if os.path.exists(text_file_path):
            with open(text_file_path, 'r', encoding='utf-8') as f:
                text = f.read()
                text = text.strip()

        results = utils.classify_text(text)
        df = pd.DataFrame(results[0])
        df = df.sort_values('score', ascending=True) 
        display_classification_results(df)


if __name__=='__main__':
    main()   
    

    
    
        
    

    
