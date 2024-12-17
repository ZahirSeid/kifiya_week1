# Task-1: Exploratory Data Analysis (EDA)

## Overview
This task involves performing an exploratory data analysis (EDA) on financial news headlines. The dataset contains over 1.4 million rows and covers information about news headlines, publishers, publication dates, stock tickers, and associated metadata.

The objective is to analyze the dataset, extract insights, and visualize key patterns through graphs and statistical summaries.

---

## Key Objectives
1. **Descriptive Statistics**:
   - Calculate and visualize the distribution of headline lengths.
   - Identify the top publishers by article count and analyze publisher domains.
2. **Text Analysis**:
   - Extract the top keywords from the dataset.
   - Perform sentiment analysis to classify headlines into `positive`, `neutral`, or `negative`.
3. **Time Series Analysis**:
   - Analyze daily and monthly publication trends to identify patterns over time.

---

## Steps and Methodology

### 1. Data Cleaning and Preparation
- **Headline Lengths**:
  - Calculated the number of characters in each headline.
  - Visualized the distribution using a histogram.

- **Publisher Contributions**:
  - Counted the number of articles per publisher and visualized the top 10 publishers using a bar chart.
  - Analyzed publisher domains to identify missing or incomplete metadata.

- **Date Parsing**:
  - Converted timezone-aware publication dates to a standardized format (UTC) for consistency.

### 2. Sentiment Analysis
- Used **VADER Sentiment Analysis** to classify headlines into `positive`, `neutral`, or `negative` categories based on the tone of the text.
- Applied parallel processing to speed up the sentiment analysis for large datasets.
- Visualized the sentiment distribution with a bar chart.

### 3. Text Analysis
- Extracted the top keywords from headlines using word frequency analysis.
- Cleaned the text data (e.g., removed non-alphabetic characters) and tokenized it into individual words.
- Visualized the top 10 keywords with a bar chart.

### 4. Time Series Analysis
- Analyzed publication trends over time:
  - **Daily Trends**: Visualized the number of articles published per day.
  - **Monthly Trends**: Aggregated and visualized article counts by month to detect long-term patterns.

---

## Visualizations
1. **Distribution of Headline Lengths**: Histogram of headline lengths.
2. **Top Publishers**: Bar chart of the top 10 publishers by article count.
3. **Daily and Monthly Publication Trends**: Line plots showing article counts over time.
4. **Sentiment Distribution**: Bar chart of sentiment counts (`positive`, `neutral`, `negative`).
5. **Top Keywords**: Horizontal bar chart of the top 10 keywords and their frequencies.

---

## Insights and Recommendations
### Key Insights:
1. Most headlines are concise, with lengths between 40 and 90 characters.
2. A small number of publishers dominate the dataset, with many articles lacking proper domain metadata.
3. Publication trends show spikes during significant financial events or market cycles.
4. Sentiment analysis reveals a predominance of negative or neutral tones in financial news.
5. Extracted keywords align with financial themes, such as "stocks," "market," and "earnings."

### Recommendations:
1. Enrich metadata to resolve unknown domains and improve publisher tracking.
2. Investigate spikes in publication activity to correlate them with financial events.
3. Use sentiment analysis and topic modeling insights to build predictive models for stock market trends.

---

## How to Run the Analysis
1. **Requirements**:
   - Python 3.x
   - Required libraries: `pandas`, `matplotlib`, `seaborn`, `nltk`, `joblib`, `tqdm`
   - Install dependencies:
     ```bash
     pip install pandas matplotlib seaborn nltk joblib tqdm
     ```

2. **Steps**:
   - Ensure the dataset is placed in the `Data/modularization-demo/data/` directory.
   - Run the notebook or script containing the EDA code.
   - Visualizations and insights will be generated as part of the output.

---

## File Structure
```
kifiya_week1/
├── Data/
│   └── modularization-demo/
│       └── data/
│           └── raw_analyst_ratings.csv  # Dataset
├── notebooks/
│   └── task1_eda.ipynb                  # Notebook for EDA
├── scripts/
│   └── eda_utils.py                     # Utility functions for EDA
├── README.md                            # This README file
```

---

## Acknowledgments
- **VADER Sentiment Analysis** for its effective sentiment scoring.
- The dataset for providing a rich source of financial headlines for analysis.
