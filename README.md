# NLP-API-APP
# API Application for Sentiment Analysis and Named Entity Recognition

This repository contains an API application that provides sentiment analysis and named entity recognition (NER) services. It's designed to analyze text input and provide insights about the sentiment (positive, neutral, or negative) and identify named entities within the text.

## Getting Started

To use the API, follow the steps below:

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/your-api-application.git
Install the required dependencies. Depending on your environment, you might need Python and other packages installed.

Set up the API configuration and ensure the required services (sentiment analysis and NER) are properly integrated.

Run the API application:

  ```sh
    python app.py

Access the API through a web browser, API client, or your preferred method:

Sentiment Analysis: Send a POST request to /perform_sentiment_analysis with a JSON payload containing the text to be analyzed.
Named Entity Recognition: Send a POST request to /perform_ner with a JSON payload containing the text for NER analysis.
