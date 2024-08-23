from textblob import TextBlob

def predict_mood(text):
    # Handle None or empty input
    if text is None or text.strip() == '':
        return 'neutral'

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    stressed_keywords = ['overwhelmed', 'anxious', 'stressed', 'worried', 'pressure', 'tense']
    motivated_keywords = ['motivated', 'determined', 'focused', 'driven', 'ready', 'confident']

    lower_text = text.lower()

    if any(word in lower_text for word in stressed_keywords):
        return 'stressed'
   
    if any(word in lower_text for word in motivated_keywords):
        return 'motivated'

    if polarity > 0.1:
        return 'happy'
    elif polarity < -0.1:
        return 'sad'
    else:
        return 'neutral'
