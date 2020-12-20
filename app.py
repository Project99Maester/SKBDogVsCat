from utilsPackages import utils
from predict import DogVsCat

from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin

os.putenv('LANG','en_US.UTF-8')
os.putenv('LC_ALL','en_US.UTF-8')

app=Flask(__name__)
CORS(app)

# @cross_origin()
class ClientApp():
    def __init__(self) :
        self.fileName = 'InputImage.jpg'
        self.classifier = DogVsCat(self.fileName)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    client=ClientApp()
    utils.decodeImage(image, client.fileName)
    result = client.classifier.prediction()
    return jsonify(result)

# if __name__=='__main__':
#     app.run(debug=True)