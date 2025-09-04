"""
Flask application for emotion detection using Watson NLP.

This module provides a web interface for analyzing emotions in text
using the Watson NLP emotion detection service.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Route for emotion detection that processes text input and returns formatted response.

    Returns:
        str: Formatted response containing emotion scores and dominant emotion,
             or error message for invalid input.
    """
    # Get the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detector function
    response = emotion_detector(text_to_analyze)

    # Check if dominant_emotion is None (error case)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract the emotions and dominant emotion
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Format the response as requested
    return (f"For the given statement, the system response is 'anger': {anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
            f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}.")


@app.route("/")
def render_index_page():
    """
    Route for the main page that renders the HTML interface.

    Returns:
        str: Rendered HTML template for the main page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
