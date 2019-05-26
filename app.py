from flask import Flask, jsonify, request, render_template
from PIL import Image
import base64
from keras.models import load_model
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, img_to_array
import io
import tensorflow as tf
from keras import backend as K
import os

app = Flask(__name__)
global graph

def get_model():
    global model
    model = load_model('cifar10_classifier.h5')
    print("Model Loaded")


def preprocessing_image(image, target_size):
    if image.mode != 'RGB':
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    return image


print("Loading the keras model")
get_model()
graph = tf.get_default_graph()


@app.route("/predict", methods=['POST'])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocessing_image(image, target_size=(32,32))
    with graph.as_default():
        prediction = model.predict_classes(processed_image)
        response = {
            'yclass': int(prediction[0])
    }

    return jsonify(response)


'''
@app.route('/')
def index():
    return render_template("page.html")


@app.route('/hello', methods=['POST'])
def hello():
    message = request.get_json(force=True)
    name = message['name']
    response = {
        'greeting': 'Hello,' + name + '!'
    }
    return jsonify(response)



@app.route('/')
def page():
    return "Good Morning Mumbai"
'''

if __name__ == '__main__':
    #port = int(os.environ.get('PORT', 5000))
    app.run(debug=True)


'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        # self.gotmarks = self.name + ' obtained ' + self.marks + ' marks'

    @property
    def gotmarks(self):
        return self.name + ' obtained ' + self.marks + ' marks'

    @gotmarks.setter
    def gotmarks(self, sentence):
        name, rand, marks = sentence.split(' ')
        self.name = name
        self.marks = marks


st = Student("Jaki", "25")
print(st.name)
print(st.marks)
print(st.gotmarks)
print("##################")
st.name = "Anusha"
print(st.name)
print(st.gotmarks)
print("##################")
st.gotmarks = 'Golam obtained 36'
print(st.gotmarks)
print(st.name)
print(st.marks)
'''