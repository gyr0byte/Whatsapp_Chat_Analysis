# WhatsApp Chat Analyzer

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white)

A Streamlit web app that analyzes exported WhatsApp chat data and delivers insights through clean, interactive visualizations.

## 📸 Demo Screenshot

![Demo Screenshot](assets/demo.png?raw=1)

## ✨ Features

- Upload WhatsApp chat `.txt` export file
- Parse and preprocess chat data into a structured DataFrame
- Display key statistics: total messages, total words, media shared, links shared
- Word Cloud visualization of most used words
- Most common words bar chart
- Filter analysis by specific user or overall
- Monthly timeline activity chart
- Daily timeline activity chart
- Activity heatmap (busiest hours and days)
- Most active users analysis
- Emoji analysis

## 🧰 Tech Stack

- Python
- Streamlit
- Pandas
- Matplotlib
- Plotly
- WordCloud
- URLExtract
- Emoji

## 🛠️ Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the app:

```bash
streamlit run app.py
```

## 📤 Export WhatsApp Chat & Use the App

1. Open a chat in WhatsApp.
2. Tap the menu (three dots) and choose **More**.
3. Select **Export chat** and choose **Without media**.
4. Send the exported `.txt` file to your computer.
5. Launch the app and upload the exported file.

## 🗂️ Project Structure

```
app.py
helper.py
preprocessor.py
requirements.txt
```

## 📊 Sample Insights

- Identify the most active users and peak chat times.
- Discover frequently used words and phrases.
- Track daily and monthly activity timelines.
- Spot patterns in monthly activity trends.
- Analyze emoji usage across participants.

## 🤝 Contributing

Contributions are welcome. Feel free to open an issue or submit a pull request for improvements.

## 📄 License

MIT
