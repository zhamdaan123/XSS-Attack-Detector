from tflite_runtime.interpreter import Interpreter

from src.commons import convert_to_ascii

#model = tf.keras.models.load_model('model.h5')
interpreter = Interpreter(model_path='model.tflite')
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


class XSSDetector:
    """XSS Detector"""

    def predict(self, data: str, score: float = 0.5):
        """Predict a data"""
        ascii_input = convert_to_ascii(data)
        ascii_input = ascii_input.reshape(1, 20, 20, 1)
        #prediction = model.predict(ascii_input)[0][0]
        interpreter.set_tensor(input_details[0]['index'], ascii_input)
        interpreter.invoke()
        prediction = interpreter.get_tensor(output_details[0]['index'])[0]
        is_malicious = True if prediction > score else False
        return is_malicious, float(prediction)
