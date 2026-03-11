class AlzheimerDetector:
    def __init__(self, model_path: str = "models/Alzhimer_model.h5"):
        self.model_path = model_path

    def predict(self, image_path: str):
        return {
            "prediction": "AD",
            "confidence": 0.94,
            "model_path": self.model_path
        }