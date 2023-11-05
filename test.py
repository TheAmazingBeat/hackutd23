import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
import os
import cv2
from matplotlib import pyplot as plt
import numpy as np

print(tf.version.VERSION)
print(os.path.join('models', 'CommercialResidentialF.h5'))
new_model = load_model(os.path.join('models', 'CommercialResidentialF.h5'))
image_path = '/images/Commercial-Ext_2.jpeg'
img = cv2.imread(image_path)
resize = tf.image.resize(img, (256,256))
yhatnew = new_model.predict(np.expand_dims(resize/255,0))
print(yhatnew)
if yhatnew > 0.5:
    print(f'Predicted estate is residential')
else:
    print(f'Predicted estate is commercial')
