import tensorflow as tf
import os

from tensorflow.keras.models import load_model
import cv2
from matplotlib import pyplot as plt
import numpy as np

print(tf.version.VERSION)
print(os.path.join('models', 'CommercialResidentialF.h5'))
new_model = tf.keras.models.load_model('/models/CommercialResidential.h5')