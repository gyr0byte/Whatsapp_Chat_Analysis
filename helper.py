from urlextract import URLExtract
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