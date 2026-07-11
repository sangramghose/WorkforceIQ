"""
Call Center Sentiment Analysis
- Generates synthetic call transcripts with known sentiments
- Applies VADER sentiment scoring
- Exports scored data for dashboard integration
"""

import pandas as pd
import numpy as np
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon', quiet=True)

# Generate synthetic call data
np.random.seed(42)
n = 10000

negative_texts = [
    "very disappointed with the service",
    "I've been on hold for an hour",
    "product stopped working after a week",
    "worst experience ever",
    "nobody resolved my issue"
]
positive_texts = [
    "agent was very helpful and friendly",
    "problem was solved quickly",
    "great customer service, thank you",
    "I'm very satisfied with the resolution",
    "excellent support team"
]
neutral_texts = [
    "I need to update my address",
    "what are your business hours",
    "please send me the invoice",
    "can I change my plan",
    "general inquiry about pricing"
]

texts = []
sentiments = []
for _ in range(n):
    r = np.random.random()
    if r < 0.3:
        texts.append(np.random.choice(negative_texts))
        sentiments.append('Negative')
    elif r < 0.6:
        texts.append(np.random.choice(positive_texts))
        sentiments.append('Positive')
    else:
        texts.append(np.random.choice(neutral_texts))
        sentiments.append('Neutral')

df = pd.DataFrame({
    'call_id': range(1, n+1),
    'transcript': texts,
    'true_sentiment': sentiments
})

# Sentiment analysis
sia = SentimentIntensityAnalyzer()
df['vader_compound'] = df['transcript'].apply(lambda x: sia.polarity_scores(x)['compound'])
df['vader_sentiment'] = df['vader_compound'].apply(lambda c: 'Positive' if c >= 0.05 else ('Negative' if c <= -0.05 else 'Neutral'))

# Evaluation
accuracy = (df['vader_sentiment'] == df['true_sentiment']).mean()
print(f"Sentiment prediction accuracy: {accuracy:.2%}")

# Export
df[['call_id', 'transcript', 'vader_sentiment', 'vader_compound']].to_csv('callcenter_sentiment.csv', index=False)
print("Sentiment data exported to callcenter_sentiment.csv")
