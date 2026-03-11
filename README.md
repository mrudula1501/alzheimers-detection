# 🧠 Alzheimer's Disease Detection via Deep Learning

[![Python](https://img.shields.io/badge/Python-3.9-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.10-FF6F00?style=flat&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![Keras](https://img.shields.io/badge/Keras-2.10-D00000?style=flat&logo=keras&logoColor=white)](https://keras.io)
[![Flask](https://img.shields.io/badge/Flask-2.0-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-10B981?style=flat)](LICENSE)

Deep learning system for Alzheimer's detection from MRI scans using a CNN + SVM hybrid pipeline.

---

## 📋 Overview

This repository provides an automated pipeline for classifying MRI scans into:

| Label | Description |
|-------|-------------|
| **AD** | Alzheimer's Disease |
| **MCI** | Mild Cognitive Impairment |
| **CN** | Cognitively Normal |

The project combines deep learning feature extraction with traditional machine learning classification, structured as a lightweight inference-ready application.

---

## 📁 Project Structure

```
alzheimers-detection/
├── app.py                      # Flask application entrypoint
├── README.md
├── requirements.txt
├── .gitignore
│
├── assets/                     # Training artifacts & visualizations
│   ├── confusion_matrix.png
│   ├── training_accuracy.png
│   └── training_loss.png
│
├── legacy/                     # Older experimental code (archived)
│
├── models/
│   └── Alzhimer_model.h5       # Trained model weights
│
├── notebooks/                  # Jupyter notebooks
│
├── samples/                    # Sample MRI images for testing
│   ├── test1.jpg
│   └── test2.png
│
├── src/
│   ├── model.py                # AlzheimerDetector inference interface
│   ├── preprocess.py           # MRI image preprocessing & resizing
│   └── utils.py                # Model metadata helper utilities
│
├── static/                     # Flask static assets
├── templates/                  # Flask HTML templates
│
└── tests/
    └── test_model.py           # Model prediction validation tests
```

---

## 🔄 Model Pipeline

```
MRI Image
    ↓
Image Preprocessing
    ↓
CNN Feature Extraction
    ↓
SVM Classification
    ↓
Prediction Output
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mrudula1501/alzheimers-detection.git
cd alzheimers-detection
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

**Activate on macOS/Linux:**
```bash
source venv/bin/activate
```

**Activate on Windows:**
```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000/health
```

**Expected response:**
```json
{"status": "healthy"}
```

---

## 💡 Example Usage

```python
from src.model import AlzheimerDetector
from src.preprocess import preprocess_image

# Load model
detector = AlzheimerDetector("models/Alzhimer_model.h5")

# Preprocess and predict
image = preprocess_image("samples/test1.jpg")
result = detector.predict("samples/test1.jpg")

print(result)
```

**Example output:**
```json
{
    "prediction": "AD",
    "confidence": 0.94,
    "model_path": "models/Alzhimer_model.h5"
}
```

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 📊 Results

Training artifacts are available in the `assets/` directory:

| File | Description |
|------|-------------|
| `training_accuracy.png` | Accuracy curve across epochs |
| `training_loss.png` | Loss curve across epochs |
| `confusion_matrix.png` | Classification quality per class |

## Sample Training Results

### Confusion Matrix
![Confusion Matrix](assets/confusion_matrix.png)

### Training Accuracy
![Training Accuracy](assets/training_accuracy.png)

### Training Loss
![Training Loss](assets/training_loss.png)


---

## 🔮 Future Improvements

- [ ] Replace placeholder inference with the full trained model pipeline
- [ ] Add proper Flask prediction endpoint (`/predict`)
- [ ] Add SHAP / LIME explainability visualizations
- [ ] Add Docker support
- [ ] Add CI/CD via GitHub Actions
- [ ] Move model weights to releases or external storage (e.g., HuggingFace Hub)

---

## 📝 Notes

This repository has been reorganized to separate active project structure from older experimental code, which is stored in `legacy/`.

---

## 📬 Contact

**Mrudula Deshmukh**

[![GitHub](https://img.shields.io/badge/GitHub-mrudula1501-181717?style=flat&logo=github)](https://github.com/mrudula1501)
[![Portfolio](https://img.shields.io/badge/Portfolio-mrudula1501.github.io-10B981?style=flat&logo=githubpages&logoColor=white)](https://mrudula1501.github.io/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-dmrudula-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dmrudula/)
[![Email](https://img.shields.io/badge/Email-mrudulad25@gmail.com-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:mrudulad25@gmail.com)
