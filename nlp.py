import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def extract_resolution_sentences(text, title):
    # Tokenize text into sentences
    sentences = nltk.sent_tokenize(text)
    
    # Initialize sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()
    
    # Iterate over sentences and extract those containing "resolution"
    for sentence in sentences:
        if "resolution" in sentence:
            # Get sentiment of sentence
            sentiment = analyzer.polarity_scores(sentence)["compound"]
            
            # Output sentence, sentiment, and title
            print("Sentence:", sentence)
            print("Sentiment:", sentiment)
            print("Title:", title)
            print()
            
# Example usage
text = "This is a resolution to improve the quality of our products. We will do this by increasing investment in research and development. The resolution passed with a majority vote."
title = "Resolution to Improve Product Quality"
extract_resolution_sentences(text, title)
