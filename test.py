import os
import random
from typing import List
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

model = tf.keras.models.load_model("/home/ahmad/hidayatahmad/Univ/Bangkit-Project-Laook/laook-backend/path/model.h5")

#  Preprocess the image and perform ingredient recognition using the machine learning model
    # img_tensor = tf.keras.preprocessing.image.load_img("temp_image.jpg", target_size=(320, 320))
    # img_array = tf.keras.preprocessing.image.img_to_array(img_tensor)
    # preprocessed_img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    # preprocessed_img_tensor = tf.expand_dims(img_array, axis=0)
    # images = np.vstack([preprocessed_img_tensor])

    # Perform prediction on the preprocessed image tensor
    # predicted_labels = model.predict(images, batch_size = 10)

    # Convert the predicted labels to ingredient names
    # recognized_ingredients = [label.decode('utf-8') for label in predicted_labels]  # Modify this conversion based on your model's output format

    # Return the list of recognized ingredients
    # return {"ingredients": predicted_labels}

# data = pd.read_csv('/content/_classes.csv')

img = image.load_img('/home/ahmad/hidayatahmad/Univ/Bangkit-Project-Laook/laook-backend/temp_image.jpg', target_size=(320, 320, 3))
# plt.imshow(img)
img = image.img_to_array(img)
img = img/255.0

img = img.reshape(1, 320, 320, 3)

# classes = data.columns[2:]
# print(classes)
y_prob = model.predict(img)
top3 = np.argsort(y_prob[0])[:-4:-1]

for i in range(3):
    print(classes[top3[i]])