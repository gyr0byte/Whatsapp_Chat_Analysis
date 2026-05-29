import streamlit as st
import preprocessor
import helper

st.sidebar.title("Whatsapp Chat Analyser")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)
    st.dataframe(df)
    
    #fetch unique users
    user_list = df['user'].unique().tolist()
    if 'group_notification' in user_list:
        user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")
    
    
    selected_user = st.sidebar.selectbox("Show analysis with respect to", user_list)
    
    if st.sidebar.button("Show Analysis"):
        col1, col2, col3, col4 = st.beta_columns(4)
        num_messages = helper.fetch_stats(selected_user, df)
        with col1:
            st.header("Total Messages")
