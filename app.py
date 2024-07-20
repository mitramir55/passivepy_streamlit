import streamlit as st
import pandas as pd
import numpy as np
from PassivePySrc import PassivePy


# default params
ALLOWED_EXTENSIONS = {'csv', 'xlsx'}
OUTPUT_FOLDER = 'uploaded_files/'

# create the model
passivepy = PassivePy.PassivePyAnalyzer(spacy_model = "en_core_web_sm")


# for the dataset
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[-1].lower() in ALLOWED_EXTENSIONS

def find_extention(filename: str)-> str:
    """
    uploaded_file_name.csv -> csv
    """
    return filename.rsplit('.', 1)[-1].lower()


def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')



# for analysis 
def analyze_dataset(df, mode, column_name):
    
    # do the analysis
    if mode=='Corpus-level analysis':
        df_output = passivepy.match_corpus_level(df=df, column_name = column_name, n_process = 1, batch_size = 50)
    elif mode=='Sentence-level analysis':
        df_output = passivepy.match_sentence_level(df=df, column_name = column_name, n_process = 1, batch_size = 50)

    return df_output
        


st.title('PassivePy')
st.caption('A Tool to Automatically Identify Passive Voice in Big Text Data')

st.write("Our aim with this work is to create a reliable (e.g., passive voice judgments are consistent), valid (e.g., passive voice judgments are accurate), flexible (e.g., texts can be assessed at different units of analysis), replicable (e.g., the approach can be performed by a range of research teams with varying levels of computational expertise), and scalable way (e.g., small and large collections of texts can be analyzed) to capture passive voice from different corpora for social and psychological evaluations of text. To achieve these aims, we introduce PassivePy, a fully transparent and documented Python library.")


link = 'Please visit our [GitHub](https://github.com/mitramir55/PassivePy) if you want to see the code or make any contributions.'
st.markdown(link, unsafe_allow_html=True)

link = 'If you use this package, please cite it as: [Sepehri, A., Mirshafiee, M. S., & Markowitz, D. M. (2022). PassivePy: A tool to automatically identify passive voice in big text data. Journal of Consumer Psychology.](https://doi.org/10.1002/jcpy.1377)'
st.markdown(link, unsafe_allow_html=True)


st.title("Try our package")
st.caption("Disclaimer: This website is provided solely for the purpose of testing this package. As a result, it can handle a few thousand (up to 10,000) one-line sentences or a few hundred paragraphs in each file.")



# single text
st.subheader("Single sentence analysis")

single_sent = st.text_input("Please enter your sentence in the box below:", "")
button_1 = st.button('analyze', key='butt1')

if single_sent and button_1:
    df_sample_text = passivepy.match_text(single_sent)
    st.write(df_sample_text)


st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

# upload the file for analysis
st.subheader("Dataset analysis")
uploaded_file = st.file_uploader("Choose a file")
col_name = st.text_input("Please enter the column name you wish to analyze", "")


mode = st.selectbox(
    'How would you like to process the dataset?',
    ('Sentence-level analysis', 'Corpus-level analysis'))
button_2 = st.button('analyze', key='butt2')


if uploaded_file is not None and button_2:
    
    uploaded_file_name = uploaded_file.name
    if allowed_file(uploaded_file_name):
        
        # read the file
        format = find_extention(uploaded_file_name)
        if format == 'csv': df = pd.read_csv(uploaded_file)
        if format == 'xlsx': df = pd.read_excel(uploaded_file)

        # adding the column check for duplicates
        columns_in_df = df.columns
        if 'all_passives' in columns_in_df or 'binary' in columns_in_df:
            st.error("""Please make sure your dataset does not have 
                     columns named 'binary' or 'all_passives'. This
                     interferes with the format of the output dataset. """, icon="🚨")
        
        # analyze and show the results
        df_output = analyze_dataset(df, mode, col_name)
        st.write(df_output)

        # create a button for downloading the output
        csv_output = convert_df(df_output)
        st.download_button(
            label="Download data as CSV",
            data=csv_output,
            file_name='output.csv',
            mime='text/csv',
)

    else: 
        st.error("""Please change your Inputs. Possible explanations for your proble:\n
    - file not with an extension different than .csv \n
    - type of analysis not specified. """, icon="🚨")
  
