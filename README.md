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
