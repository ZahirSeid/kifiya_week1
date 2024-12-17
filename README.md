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

# Task 2: Quantitative Analysis Using TA-Lib
## Overview

This project focuses on applying quantitative analysis to historical stock data using TA-Lib (Technical Analysis Library). We calculate and visualize key technical indicators and financial metrics for various stocks.

The task includes:

    Loading and preparing stock price data.
    Calculating technical indicators like RSI, MACD, SMA, and EMA.
    Visualizing the data for better insights into the stock trends.
    Calculating financial metrics such as expected return, volatility, and cumulative return.
    Reporting the analysis results and key insights.

Steps to Complete
1. Install Dependencies

To run the analysis, first, install the required libraries:

pip install pandas matplotlib TA-Lib pyportfolioopt

2. Load Stock Data

We use pandas to load historical stock price data from CSV files in the yfinance_data directory. Ensure that the data includes columns like Open, High, Low, Close, and Volume.

import pandas as pd

# Example: Load stock data for AAPL
aapl_df = pd.read_csv("Data/AAPL_historical_data.csv")

3. Calculate Technical Indicators

We calculate the following technical indicators using TA-Lib:

    RSI (Relative Strength Index)
    MACD (Moving Average Convergence Divergence)
    SMA (Simple Moving Average)
    EMA (Exponential Moving Average)
    Cumulative Return (percentage change in stock prices over time)

4. Visualize Data

The following visualizations are generated:

    Stock Price Trends: Plots the Close Price, SMA_50, and EMA_12.
    RSI: Plots the RSI with overbought and oversold levels.
    MACD: Plots the MACD line, signal line, and MACD histogram.


5. Calculate Financial Metrics

The financial metrics calculated for each stock include:

    RSI Mean
    MACD Mean
    SMA_50 Mean
    EMA_12 Mean
    Cumulative Return

6. Generate a Report

The results of the financial metrics can be displayed as a summary report for each stock.

### Conclusion

In Task 2, we performed quantitative analysis on stock data using TA-Lib. We calculated key technical indicators (RSI, MACD, SMA, EMA) and visualized stock price trends. The financial metrics provide insights into each stock's performance, aiding in informed decision-making for potential investments.

This analysis lays the foundation for advanced topics such as portfolio optimization and market predictions.

# Task 3: Correlation between News and Stock Movement
## Objective

This task aims to analyze the correlation between news sentiment and stock movements. Specifically, we investigate how daily sentiment from news headlines correlates with daily stock returns for various companies. By doing so, we aim to uncover whether there’s any linear relationship between the sentiment of news articles and stock price fluctuations.
Key Steps

    Data Preparation:
        The stock price data is obtained from CSV files, including columns such as Open, High, Low, Close, Volume, and Daily Returns.
        The news sentiment data is derived from headlines, where the sentiment of each article is quantified on a scale from -1 (negative) to 1 (positive).
        Both datasets are aligned by date to ensure proper comparison.

    Sentiment Analysis:
        News headlines are analyzed for sentiment using an appropriate tool, such as TextBlob or a similar library.
        Sentiment scores are generated and normalized between -1 and 1, indicating the tone of the article (negative, neutral, or positive).

    Correlation Analysis:
        Daily stock returns are calculated as the percentage change in the closing stock price.
        The correlation between daily sentiment scores and daily stock returns is computed using Pearson’s correlation.
        A positive correlation would suggest that positive news correlates with positive stock movements, and a negative correlation would indicate the opposite.

    Results:
        The correlation coefficients for each stock are calculated to assess the relationship between sentiment and stock movement.
        A low or near-zero correlation would suggest that sentiment does not strongly influence daily stock returns.

Dataset

    Stock Data:
        Data is sourced from Yahoo Finance, and includes daily stock prices for companies such as AAPL, AMZN, TSLA, GOOG, META, MSFT, and others.
        Essential columns include Open, High, Low, Close, Volume, and Date.

    News Sentiment Data:
        Sentiment scores are derived from news headlines. Each article is associated with a date, and the sentiment score is computed based on the content of the headline.
        Data includes headline, publisher, date, and sentiment (between -1 and 1).

### Tools and Libraries

    Pandas: For data manipulation and merging datasets.
    NumPy: For numerical operations.
    SciPy: For statistical analysis and Pearson correlation calculation.
    TextBlob: For sentiment analysis.
    Matplotlib/Seaborn: For visualizing results.

### Analysis Approach

    Sentiment Calculation: A sentiment score is calculated for each news article headline, reflecting the positive, neutral, or negative tone of the article.
    Correlation Calculation: The Pearson correlation coefficient is used to quantify the relationship between the sentiment scores and the daily stock returns for each stock.

### Results and Interpretation

    Correlations: The task provides insights into whether sentiment (from news articles) correlates with stock price movements.
    Weak Correlation: The analysis shows that the correlation between sentiment and stock returns is generally weak (values close to 0), suggesting that news sentiment may not have an immediate or strong effect on stock prices.

### Conclusion

The analysis suggests that while sentiment from news headlines provides some information about the tone surrounding a company, it does not exhibit a strong correlation with daily stock price fluctuations. This could be due to various factors, such as:

    Other factors driving stock prices (market conditions, earnings reports, etc.)
    Delayed effects of news sentiment on stock prices
    Limitations in sentiment analysis tools

Further investigations using longer time periods, more advanced sentiment models, or alternative factors like technical indicators may provide deeper insights.
