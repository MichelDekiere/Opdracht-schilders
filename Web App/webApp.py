from flask import Flask, render_template, request, jsonify
from PIL import Image
import numpy as np
import io
# from pyngrok import ngrok

from PaintingPredictor import PaintingPredictor

app = Flask(__name__)


# ngrok.set_auth_token("29QwS5TmszqKVoH3XllMtQ0pckI_5ypz8nzud9wJaZu6x5GEu")
# public_url = ngrok.connect(5000).public_url
# print(public_url)

@app.route('/')
@app.route('/PaintingPredictor')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST', "GET"])
def predict_chocolate():
    pp = PaintingPredictor('final_model.keras')

    f = request.files['file-selector'].read()

    # convert bytes to image
    stream = io.BytesIO(f)
    image = Image.open(stream).convert("RGB")
    stream.close()

    image = image.resize((180, 180))
    img_np = np.array([np.array(image)])  # Image object omzetten naar numpy array (2 keer voor juiste shape)

    prediction = pp.predict_painter(img_np)  # voorspelling maken met de PaintingPredictor

    return render_template("index.html", output=prediction)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
