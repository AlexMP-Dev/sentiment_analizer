
from typing import List
import pandas as pd
from googletrans import Translator
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
nltk.download('vader_lexicon')

def analisisSentiment(data: List[List[str]]):
    df = pd.DataFrame(data, columns=["Date", "Time", "contact", "Message"])
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    
    # Initialize translator
    translator = Translator()
    
    # Translate messages to English
    df['Message_English'] = [translator.translate(text, dest='en').text for text in df['Message']]
    
    sentiments = SentimentIntensityAnalyzer()
    # blob = TextBlob()
    # df["positive"] = [sentiments.polarity_scores(i)["pos"] for i in df["Message_English"]]
    # df["negative"] = [sentiments.polarity_scores(i)["neg"] for i in df["Message_English"]]
    # df["neutral"] = [sentiments.polarity_scores(i)["neu"] for i in df["Message_English"]]

    df["sentiment"] = [TextBlob(i).sentiment.polarity for i in df["Message_English"]]
    df["positive"] = [TextBlob(i).sentiment.polarity > 0.25 for i in df["Message_English"]]
    df["negative"] = [TextBlob(i).sentiment.polarity < -0.25 for i in df["Message_English"]]
    df["neutral"] = [TextBlob(i).sentiment.polarity <= 0.25 and TextBlob(i).sentiment.polarity >= -0.25 for i in df["Message_English"]]

    return df.to_dict(orient="records")

def score(a, b, c):
    if (a > b) and (a > c):
        return "Positive"
    if (b > a) and (b > c):
        return "Negative"
    if (c > a) and (c > b):
        return "Neutral"