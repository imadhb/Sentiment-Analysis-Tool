from textblob import TextBlob

def sentiment_analysis(text, language='en'):
    try:
       
        blob = TextBlob(text)
        blob = blob.translate(to=language) if language != 'en' else blob
        
       
        sentiment_score = blob.sentiment.polarity

        
        if sentiment_score > 0:
            sentiment = "positive"
        elif sentiment_score == 0:
            sentiment = "neutral"
        else:
            sentiment = "negative"

        return sentiment, sentiment_score

    except Exception as e:
        return "error", str(e)

def main():
    print("Welcome to Sentiment Analysis Tool")
    print("---------------------------------")

    
    text = input("Enter the text you want to analyze: ")

    
    language = input("Enter the language of the text (e.g., 'en' for English, 'ar' for Arabic, default: English): ").lower() or 'en'

    
    sentiment, sentiment_score = sentiment_analysis(text, language)

    
    if sentiment == 'error':
        print("\nError occurred during sentiment analysis:", sentiment_score)
    else:
        print("\nSentiment Analysis Result:")
        print("Sentiment: ", sentiment)
        print("Sentiment Score: ", sentiment_score)

if __name__ == "__main__":
    main()
