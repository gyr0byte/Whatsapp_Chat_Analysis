def fetch_stats(selected_user, df):
    if df is None or df.empty:
        return 0
    if selected_user == "Overall":
        # 1. Fetch number of messages
        num_messages = df.shape[0]
        #2. number of words
        words = 0
        for message in df['message']:
            message_words = message.split()
            words += len(message_words)
        return num_messages, words
    else:
        num_messages = df[df["user"] == selected_user].shape[0]
        words = 0
        for message in df[df["user"] == selected_user]["message"]:
            message_words = message.split()
            words += len(message_words)
        return num_messages, words