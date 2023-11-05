from huggingface_hub import InferenceClient
from huggingface_hub import login
from PIL import Image
import io
import os
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
# from keras.preprocessing.image import load_img
# from keras.applications.vgg16 import preprocess_input
import numpy as np
import cv2

# Login to HuggingFace Hub
login(token="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")



# Use the Visual Question Anwering Model from HuggingFace Hub
def analyze_image(image_path = "images/Commercial-Ext1.jpeg"):
    image = Image.open(image_path)
    # Convert PIL Image to bytes since parameter needs bytes
    byte_arr = io.BytesIO()
    image.save(byte_arr, format='JPEG')
    image_in_bytes = byte_arr.getvalue()

    question = "What type of building is this?"
    client = InferenceClient()
    results = client.visual_question_answering(image_in_bytes, question, model="dandelin/vilt-b32-finetuned-vqa")
    print(results)
    return results
  
# https://medium.com/@draj0718/deploying-deep-learning-model-using-flask-api-810047f090ac
# def read_image(image_path = "images/Commercial-Ext1.jpeg"):
#     image = load_img(image_path, target_size=(224, 224))
#     x = image.img_to_array(img)
#     x = np.expand_dims(x, axis=0)
#     x = preprocess_input(x)
#     return x  

# Use the Image Classification Model from Justin
def classify_image(image_path = "images/Commercial-Ext1.jpeg"):
    # init Justin's model
    # model_path = os.path.join('models', 'CommercialResidentialF.h5')
    model_path="models/CommercialResidentialF.h5"
    # model = load_model(model_path)
    print(tf.__version__)
    print(keras.__version__)
    image_path="images/Commercial-Ext1.jpeg"
    img = cv2.imread(image_path)
    resize = tf.image.resize(img, (256, 256))
    yhat = model.predict(np.expand_dims(resize/255,0))
    print(yhat)
    return yhat
#   img = read_image(image_path)
#   class_prediction = model.predict(img)
#   classes_x = np.argmax(class_prediction, axis=1)
#   print(classes_x, class_prediction)
#   return {classes_x, class_prediction}
    

