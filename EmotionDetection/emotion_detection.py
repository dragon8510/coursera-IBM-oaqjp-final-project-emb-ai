import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyzes the emotion of the given text using Watson NLP.
    
    Args:
        text_to_analyze (str): The text to analyze for emotions
        
    Returns:
        dict: Dictionary containing emotion scores and dominant emotion
    """
    # Watson NLP Emotion Predict API endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Required headers for the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input JSON format required by the API
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Make the POST request to Watson NLP service
    response = requests.post(url, json=input_json, headers=headers)
    
    # Check for status code 400 (blank entries)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Convert the response text to dictionary
    response_dict = json.loads(response.text)
    
    # Extract emotions from the response
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    # Extract the required emotions with their scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Find the dominant emotion (emotion with highest score)
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    # Get the dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Return the formatted output
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }