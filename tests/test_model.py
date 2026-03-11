from src.model import AlzheimerDetector

def test_prediction():
    model = AlzheimerDetector()
    result = model.predict("samples/test1.jpg")

    assert "prediction" in result
    assert "confidence" in result