import tensorflow as tf

from src.commons import convert_to_ascii

model = tf.keras.models.load_model('model.h5')


class XSSDetector:
    """XSS Detector"""

    def predict(self, data: str, score: float = 0.5):
        """Predict a data"""
        ascii_input = convert_to_ascii(data)
        ascii_input = ascii_input.reshape(1, 20, 20, 1)
        prediction = model.predict(ascii_input)[0][0]
        is_malicious = True if prediction > score else False
        return is_malicious, float(prediction)
