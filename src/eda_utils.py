import pandas as pd
from collections import Counter

def get_headline_stats(df, text_column="headline"):
    """
    Compute statistics for headline lengths.
    """
    df["headline_length"] = df[text_column].apply(len)
    stats = df["headline_length"].describe()
    return stats

def count_publishers(df, publisher_column="publisher"):
    """
    Count articles per publisher.
    """
    return df[publisher_column].value_counts()

def extract_top_keywords(df, text_column="headline", num_keywords=10):
    """
    Extract common keywords from text data.
    """
    all_words = " ".join(df[text_column]).split()
    return Counter(all_words).most_common(num_keywords)

