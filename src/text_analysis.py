from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download("vader_lexicon")

def analyze_sentiment(text):
    """
    Analyze sentiment of a given text.
    Returns: sentiment (positive, neutral, negative).
    """
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)
    if sentiment_score['compound'] > 0.05:
        return "positive"
    elif sentiment_score['compound'] < -0.05:
        return "negative"
    else:
        return "neutral"

