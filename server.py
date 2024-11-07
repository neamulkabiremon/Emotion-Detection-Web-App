from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Detects the dominant emotion for the provided text.

    Receives JSON data with a 'text' field containing the text to analyze.
    Calls the emotion_detector function to get emotion scores and the
    dominant emotion.

    Returns:
        JSON response containing formatted emotion scores and dominant
        emotion, or an error message if the input is invalid.
    """
    data = request.get_json()
    text_to_analyze = data.get("text", "")

    emotion_result = emotion_detector(text_to_analyze)

    # Check if the dominant emotion is None
    if emotion_result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again."}), 400

    response_text = (f"For the given statement, the system response is 'anger': "
                     f"{emotion_result['anger']}, 'disgust': {emotion_result['disgust']}, "
                     f"'fear': {emotion_result['fear']}, 'joy': {emotion_result['joy']} "
                     f"and 'sadness': {emotion_result['sadness']}. "
                     f"The dominant emotion is {emotion_result['dominant_emotion']}.")

    return jsonify({"message": response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
