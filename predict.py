import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class DogVsCat():
    def __init__(self,fileName):
        self.fileName = fileName
    
    def prediction(self):
        model=load_model('model.h5')

        Input_Image = image.load_img(self.fileName, target_size = (128, 128))
        Input_Image = image.img_to_array(Input_Image)
        Input_Image = np.expand_dims(Input_Image, axis=0)
        result = model.predict(Input_Image)

        if result[0][0] >= 0.5:
            return [{"image":'Dog'}]
        else:
            return [{"image":"Cat"}]

if __name__=='__main__':
    print(DogVsCat('InputImage.jpg').prediction())