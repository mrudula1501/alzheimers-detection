from PIL import Image
import numpy as np

def preprocess_image(image_path: str):
    """
    Load and preprocess the MRI image for model inference.
    """
    image = Image.open(image_path).convert("RGB")
    image = image.resize((224, 224))

    image_array = np.array(image) / 255.0
    image_array = image_array.reshape(1, 224, 224, 3)

    return image_array