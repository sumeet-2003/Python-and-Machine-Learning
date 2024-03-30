import os
from flask import Flask, render_template, request
from keras.models import load_model
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load the model
model_path = 'D://RiceCrop_DS/samplepredict.h5'  # Replace 'D://project/your_model.h5' with the path to your model
model = load_model(model_path)

# Define your classes
classes = ['Brown Spot','Healthy', 'Hispa', 'Leaf Blast']

@app.route('/', methods=['GET'])
def fun():
    return render_template('index.html')

@app.route('/info',methods=['GET','POST'])
def info():
    return render_template('info_page.html')

@app.route('/', methods=['POST'])
def predict():
    # Save the uploaded image
    imagefile = request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)

    # Preprocess the image
    image = Image.open(image_path)
    image = image.resize((256, 256))  # Resize the image to match your model's input size
    image = np.array(image) / 255.0  # Normalize the pixel values (assuming your model was trained with normalized data)

    # Make prediction
    prediction = model.predict(np.expand_dims(image, axis=0))

    # Get the predicted class
    predicted_class_index = np.argmax(prediction)
    predicted_class = classes[predicted_class_index]

    # Return the prediction result
    return render_template('index.html', prediction=predicted_class)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
