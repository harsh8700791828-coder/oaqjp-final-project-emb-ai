import requests, json
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    text = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers = Headers, json = text)
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    dominant_emotion = max(emotions, key=emotions.get)
    return {
        'anger': anger_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'dominant_emotion': dominant_emotion
    }