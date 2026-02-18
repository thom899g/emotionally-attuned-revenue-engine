from textblob import TextBlob
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)

class CustomerSentimentAnalyzer:
    def __init__(self):
        self.model_name = "sentiment_analyzer_1.0"
        logger.info(f"Initialized {self.model_name}")

    def analyze_sentiment(self, text: str) -> Dict[str, Any]:
        """Analyze customer sentiment from input text."""
        try:
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity

            sentiment_score = {
                "polarity": polarity,
                "subjectivity": subjectivity,
                "sentiment": "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
            }
            logger.info(f"Sentiment analysis result: {sentiment_score}")
            return sentiment_score

        except Exception as e:
            logger.error(f"Error analyzing sentiment: {str(e)}")
            raise

    def get_emotional_state(self, sentiment_data: Dict[str, Any]) -> str:
        """Classify emotional state based on sentiment metrics."""
        try:
            if sentiment_data["sentiment"] == "positive":
                return "happy"
            elif sentiment_data["sentiment"] == "negative":
                return "frustrated"
            else:
                return "neutral"

        except KeyError as e:
            logger.error(f"Missing key in sentiment data: {str(e)}")
            raise