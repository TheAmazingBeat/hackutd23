import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
import os
import cv2
from matplotlib import pyplot as plt
import numpy as np

def classify_image(image_path):
    print(tf.version.VERSION)
    print(os.path.join('models', 'CommercialResidentialF.h5'))
    new_model = load_model(os.path.join('models', 'CommercialResidentialF.h5'))
    #filename
    img = cv2.imread('Residential_test.jpeg')
    resize = tf.image.resize(img, (256,256))
    yhatnew = new_model.predict(np.expand_dims(resize/255,0))
    if yhatnew > 0.5:
        print(f'Predicted estate is residential')
    else:
        print(f'Predicted estate is commercial')