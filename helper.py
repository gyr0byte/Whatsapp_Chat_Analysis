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

    return num_messages, num_words, num_media_messages