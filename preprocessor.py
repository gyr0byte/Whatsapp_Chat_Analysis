import re
import pandas as pd


def preprocess(data):
    date_pattern = r"\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}(?:\s(?:am|pm|AM|PM))?"
    entry_pattern = (
        r"(?s)^" +
        r"(" + date_pattern + r")" +
        r"\s-\s([^:]+):\s(.*?)" +
        r"(?=\n" + date_pattern + r"\s-\s[^:]+:\s|\Z)"
    )
    entries = re.findall(entry_pattern, data, flags=re.M)
    messages = [f"{name}: {msg}" for _, name, msg in entries]
    dates = [
        re.sub(r"\s(?:am|pm|AM|PM)$", "", d.replace("\u202f", " ")) + " - "
        for d, _, _ in entries
    ]
    df = pd.DataFrame({"user_message": messages, "message_date": dates})
    # convert message_date type
    clean_dates = df["message_date"].str.replace(r"\s-\s$", "", regex=True)
    df["message_date"] = pd.to_datetime(
        clean_dates, format="mixed", dayfirst=True)
    df.rename(columns={"message_date": "date"}, inplace=True)
    # separate users and messages
    users = []
    message_texts = []
    for text in df["user_message"]:
        entry = text.split(": ", 1)
        if len(entry) == 2:
            users.append(entry[0])
            message_texts.append(entry[1])
        else:
            users.append("Unknown")
            message_texts.append(entry[0])
    df["user"] = users
    df["message"] = [m.replace("\n", " ").strip() for m in message_texts]
    
    # drop empty/media-omitted messages
    df = df[df["message"] != ""]
    df = df[df["message"].str.lower() != "<media omitted>"]
    
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df.drop(columns=['user_message'], inplace=True)

    return df
