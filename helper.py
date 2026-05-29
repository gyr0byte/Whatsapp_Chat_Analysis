def fetch_stats(selected_user, df):
    if df is None or df.empty:
        return 0
    if selected_user == "Overall":
        return df.shape[0]
    else:
        return df[df["user"] == selected_user].shape[0]