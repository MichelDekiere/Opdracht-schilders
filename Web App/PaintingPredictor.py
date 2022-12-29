import numpy as np
from keras.models import load_model


class PaintingPredictor:

    def __init__(self, filename):
        self.filename = filename
        self.model = load_model('final_model.keras')

    def predict_painter(self, input: np.array):
        labels = ["Mondriaan", "Picasso", "Rembrandt", "Rubens", "Van Gogh"]

        pred = self.model.predict(input)
        predicted_class = labels[np.argmax(pred)]  # argmax to get the index of class with largest percentage, then use that index to get the concrete
                                                   # digit/letter out of labels list

        return predicted_class  # voorspelde schilder returnen

