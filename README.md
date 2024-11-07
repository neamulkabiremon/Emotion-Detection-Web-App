# Emotion Detection Web App

An AI-powered web application that uses IBM Watson’s NLP library to detect emotions in text. This application identifies key emotions—anger, disgust, fear, joy, and sadness—and highlights the dominant emotion. Built with Flask, it offers a simple API endpoint for emotion analysis.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [License](#license)

## Overview

The Emotion Detection Web App leverages IBM Watson NLP to analyze input text, returning emotion scores and identifying the dominant emotion. This app can be used for sentiment analysis, customer feedback analysis, or any application needing emotional context from textual data.

## Features

- Detects five primary emotions in text: anger, disgust, fear, joy, and sadness.
- Highlights the dominant emotion based on the highest score.
- Provides a RESTful API endpoint for easy integration.
- Error handling for empty or invalid input.
- Includes unit tests and static code analysis for quality assurance.

## Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone git@github.com:neamulkabiremon/Emotion-Detection-Web-App.git
   cd Emotion-Detection-Web-App

2. Install Required Packages

Ensure Python 3.11 is installed, then install the required packages:

python3.11 -m pip install -r requirements.txt

3. Run the Application Locally

Start the Flask server:

python3.11 server.py

The application will run on http://localhost:5000.

Usage
API Endpoint
Endpoint: /emotionDetector
Method: POST
Body: JSON object with a text field containing the input text.

curl -X POST http://localhost:5000/emotionDetector -H "Content-Type: application/json" -d '{"text": "I love this new technology!"}'
Expected Response
json

{
  "message": "For the given statement, the system response is 'anger': 0.01, 'disgust': 0.002, 'fear': 0.009, 'joy': 0.97 and 'sadness': 0.05. The dominant emotion is joy."
}
Screenshots
Sample API Response

Technologies Used
Python: Programming language
Flask: Web framework
IBM Watson NLP: Emotion detection library
PyLint: For static code analysis
Unit Testing: Ensures code reliability

License
This project is licensed under the MIT License. See the LICENSE file for details.


### Final Steps for Adding to GitHub

1. **Replace `path_to_your_screenshot.png`**: Update this placeholder with the correct image file path or URL.
2. **Save and Commit**:
   - Save this content as `README.md` in your project’s root directory.
   - Commit and push it to GitHub:
     ```bash
     git add README.md
     git commit -m "Added README file with project details"
     git push -u origin main
     ```








