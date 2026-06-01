from collections import Counter
import string
from pathlib import Path
import pandas as pd
from urlextract import URLExtract
from wordcloud import WordCloud
import emoji
extractor = URLExtract()


def _is_media_omitted(message_series):
    return message_series.str.strip().str.lower() == "<media omitted>"


def _load_stopwords():
    stopwords_path = Path(__file__).with_name("stop_words.txt")
    if not stopwords_path.exists():
        return set()
    return {
        line.strip().lower()
        for line in stopwords_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }


STOPWORDS = _load_stopwords()


def _normalize_token(token):
    return token.strip(string.punctuation).lower()


def _filtered_tokens(messages):
    tokens = []
    for message in messages:
        for token in message.split():
            cleaned = _normalize_token(token)
            if cleaned and not cleaned.isdigit() and cleaned not in STOPWORDS:
                tokens.append(cleaned)
    return tokens


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
    num_media_messages = df[_is_media_omitted(df["message"])].shape[0]

    # fetch number of links shared
    urls = []
    for message in df['message']:
        urls.extend(extractor.find_urls(message))

    return num_messages, num_words, num_media_messages, len(urls)


def most_busy_users(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts()/df.shape[0])*100,
               2).reset_index().rename(columns={"user": "Name", "count": "percent"})
    return x, df


def create_wordcloud(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
    temp = df[~_is_media_omitted(df["message"])]
    wc = WordCloud(width=500, height=500, min_font_size=10,
                   background_color='white', stopwords=STOPWORDS)
    tokens = _filtered_tokens(temp['message'])
    df_wc = wc.generate(" ".join(tokens))
    return df_wc


def most_common_words(selected_user, df):
    temp = df[~_is_media_omitted(df["message"])]
    if selected_user != "Overall":
        temp = temp[temp['user'] == selected_user]
    tokens = _filtered_tokens(temp['message'])
    return pd.DataFrame(Counter(tokens).most_common(25))

def emoji_helper(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
    emojis = []
    for message in df['message']:
        emojis.extend(emoji.emoji_list(message))
    return pd.DataFrame(Counter([e['emoji'] for e in emojis]).most_common(20))

def monthly_timeline(selected_user,df):
    if selected_user != "Overall": 
        df = df[df['user'] == selected_user]
    timeline = df.groupby(['year','month_num','month']).count()['message'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
    timeline['time'] = time
    return timeline

def daily_timeline(selected_user,df):
    if selected_user != "Overall": 
        df = df[df['user'] == selected_user]
    daily_timeline = df.groupby('only_date').count()['message'].reset_index()
    
    return daily_timeline

def