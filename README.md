# 🧠 Alzheimer's Disease Detection using Deep Learning

[![Python](https://img.shields.io/badge/Python-3.9-blue)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-orange)](https://tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-red)](https://keras.io/)
[![Flask](https://img.shields.io/badge/Flask-black)](https://flask.palletsprojects.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E)](https://scikit-learn.org/)

Deep learning project for **Alzheimer’s disease classification from brain MRI images** using a hybrid **CNN + SVM** approach with a simple **Flask web interface** for prediction.

---

## Overview

Early detection of Alzheimer’s disease can help clinicians identify cognitive decline sooner and support better treatment planning.

This project builds an **image classification pipeline** that analyzes MRI scans and predicts Alzheimer’s disease stages using deep learning and machine learning techniques.

The system performs the following steps:

* MRI image preprocessing
* Feature extraction using a Convolutional Neural Network (CNN)
* Classification using a Support Vector Machine (SVM)
* Prediction through a Flask-based web interface

---

## Key Highlights

* Hybrid **CNN + SVM classification architecture**
* MRI image preprocessing and prediction pipeline
* **Flask web interface** for uploading MRI scans
* Healthcare-focused machine learning application
* Combines **deep learning with classical ML models**

---

## Project Structure

```
Alzheimer_detection/
│
├── AlzhimerDataset/        # MRI dataset
├── Arduino/                # Hardware / sensor related files
├── Model/                  # Model scripts or training files
├── Results/                # Output results and screenshots
├── static/                 # Static files for web interface
├── templates/              # HTML templates
├── upload/                 # Uploaded images for prediction
│
├── Alzhimer_model.h5       # Trained deep learning model
├── autils.py               # Utility functions
├── cnn_svm.py              # CNN + SVM classification logic
├── firebaseTest.py         # Firebase integration test
├── main.py                 # Main Flask application
├── mydatabase.db           # Local SQLite database
├── test.py                 # Testing script
├── test1.jpg               # Sample MRI image
├── test2.png               # Sample MRI image
│
└── README.md
```

---

## Methodology

### 1. Image Preprocessing

MRI images are prepared before inference using standard preprocessing techniques such as resizing and normalization.

### 2. Feature Extraction

A **Convolutional Neural Network (CNN)** extracts high-level visual features from MRI scans.

### 3. Classification

The extracted features are passed to an **SVM classifier**, which improves class separation and final prediction performance.

### 4. Prediction Interface

A **Flask-based web interface** allows users to upload an MRI image and receive a predicted diagnosis.

---

## System Architecture

```
Brain MRI Image
      │
      ▼
Image Preprocessing
      │
      ▼
CNN Feature Extraction
      │
      ▼
SVM Classifier
      │
      ▼
Prediction Output
```

---

## Tech Stack

| Area                  | Tools             |
| --------------------- | ----------------- |
| Programming           | Python            |
| Deep Learning         | TensorFlow, Keras |
| Machine Learning      | Scikit-learn      |
| Web Framework         | Flask             |
| Data Handling         | NumPy, Pandas     |
| Visualization         | Matplotlib        |
| Storage / Integration | SQLite, Firebase  |

---

## Use Case

This project demonstrates a **healthcare-focused machine learning application** for analyzing MRI scans and identifying potential Alzheimer’s disease patterns.

Potential value includes:

* faster screening assistance
* reproducible machine learning predictions
* demonstration of medical image classification workflows

---

## Installation

### Clone the repository

```bash
git clone https://github.com/mrudula1501/alzheimers-detection.git
cd alzheimers-detection
```

### Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

For Windows:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install tensorflow keras flask scikit-learn numpy pandas matplotlib pillow
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Start the Flask application:

```bash
python main.py
```

Open the URL shown in the terminal and upload an MRI image for prediction.

---

## Example Workflow

1. Start the Flask application
2. Upload an MRI brain scan
3. The model processes the image
4. The system predicts the class

---

## Future Improvements

* Add a clean `requirements.txt`
* Improve dataset documentation
* Add training metrics and evaluation plots
* Include prediction screenshots
* Improve project structure

---

## Author

**Mrudula Deshmukh**
ML Engineer | Data Scientist | Healthcare AI

GitHub: https://github.com/mrudula1501
LinkedIn: https://www.linkedin.com/in/dmrudula/
Portfolio: https://mrudula1501.github.io/
