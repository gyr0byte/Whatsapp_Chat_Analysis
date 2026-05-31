from collections import Counter
import pandas as pd
from urlextract import URLExtract
from wordcloud import WordCloud
extractor = URLExtract()

def fetch_stats(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]

    # fetch number of messages
    num_messages = df.shape[0]
    
    # fetch number of words
    words = []
    for message in df['message']:
        words.extend(message.split())
    num_words = len(words)
    
    # fetch number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>'].shape[0]
    
    #fetch number of links shared
    urls = []
    for message in df['message']:
        urls.extend(extractor.find_urls(message))

    return num_messages, num_words, num_media_messages, len(urls)

def most_busy_users(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={"user":"Name","count":"percent"})
    return x, df

def create_wordcloud(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]

    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df_wc = wc.generate(df['message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user,df):
    if selected_user != "Overall":
        temp = temp[temp['user'] == selected_user]
        
    temp = df[df["message"].str.lower() != "<media omitted>"]
    temp = temp[temp['message'] != 'Media omitted>']
    
    words = []
    for message in temp['message']:
        words.extend(message.split())
    
    return pd.DataFrame(Counter(words).most_common(20))