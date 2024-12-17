from collections import Counter

def get_word_frequency(text_list, top_n=10):
    """
    Get the top N most common words from a list of text strings.
    """
    all_words = " ".join(text_list).split()
    return Counter(all_words).most_common(top_n)

