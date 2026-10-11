
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

# Sample customer reviews
data = {
    "Review": [
        "This product is amazing",
        "I love this product",
        "Very good quality",
        "The product is okay",
        "It is an average product",
        "Nothing special",
        "Very bad product",
        "I hate this product",
        "Poor quality",
        "Excellent service"
    ]
}

df = pd.DataFrame(data)

# Analyze sentiment
def analyze_sentiment(review):
    score = TextBlob(review).sentiment.polarity

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Review"].apply(analyze_sentiment)

# Display results
print("CODEALPHA - SENTIMENT ANALYSIS")
print("=" * 40)
print(df.to_string(index=False))

# Count sentiments
sentiment_counts = df["Sentiment"].value_counts()

print("\nSentiment Summary:")
print(sentiment_counts)

# Create chart
plt.figure(figsize=(8, 5))
sentiment_counts.plot(kind="bar")
plt.title("Customer Review Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sentiment_chart.png")
plt.show()

# Save results
df.to_csv("sentiment_results.csv", index=False)

print("\nOutput: sentiment_results.csv created")
print("Output: sentiment_chart.png created")
