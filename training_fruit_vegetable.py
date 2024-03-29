# -*- coding: utf-8 -*-
"""Training_fruit_vegetable.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w5mc00QEVZpvnK_CivegXScJKfFTr1Xy

Importing Dataset
"""

from google.colab import drive
drive.mount('/content/drive')

"""Importing Libraries

"""

import numpy as np
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

"""Data preprocessing

Training Image preprocessing
"""

training_set = tf.keras.utils.image_dataset_from_directory(
    '/content/drive/MyDrive/Fruit Recognition System/train',
    labels="inferred",
    label_mode="categorical",
    class_names=None,
    color_mode="rgb",
    batch_size=32,
    image_size=(64, 64),
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    interpolation="bilinear",
    follow_links=False,
    crop_to_aspect_ratio=False

)

"""Validation Image preprocessing

"""

test_set = tf.keras.utils.image_dataset_from_directory(
    '/content/drive/MyDrive/Fruit Recognition System/validation',
    labels="inferred",
    label_mode="categorical",
    class_names=None,
    color_mode="rgb",
    batch_size=32,
    image_size=(64, 64),
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    interpolation="bilinear",
    follow_links=False,
    crop_to_aspect_ratio=False
)

"""Building model

"""

cnn = tf.keras.models.Sequential()

"""Building Convolution layer"""

cnn.add(tf.keras.layers.Conv2D(filters=64,kernel_size=3,activation='relu',input_shape=[64,64,3]))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2))

cnn.add(tf.keras.layers.Conv2D(filters=64,kernel_size=3,activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2))

cnn.add(tf.keras.layers.Dropout(0.5))

cnn.add(tf.keras.layers.Flatten())

cnn.add(tf.keras.layers.Dense(units=128,activation='relu'))

cnn.add(tf.keras.layers.Dense(units=36,activation='softmax'))

"""Compiling and training Phase"""

cnn.compile(optimizer='rmsprop',loss='categorical_crossentropy', metrics=['accuracy'])

training_history = cnn.fit(x=training_set,validation_data=test_set,epochs=30)

"""Saving Model

"""

cnn.save('trained_model.h5')

#Recording History in JSON format
import json
with open('training_hist.json', 'w') as f:
    json.dump(training_history.history, f)

training_history.history

print(training_history.history.keys())

"""Calculating Accuracy of Model Achieved on Test set"""

print('Test set Accuracy: {} %'.format(training_history.history['val_accuracy'][-1]*100))

"""Accuracy Visualization

Training Visualization
"""

epochs=[i for i in range(1,31)]
plt.plot(epochs,training_history.history['accuracy'],color='red')
plt.xlabel('Epochs')
plt.ylabel('Training Accuracy')
plt.title("Visualization of Training Accuracy Result")
plt.show()

"""Validation Visualization"""

plt.plot(epochs,training_history.history['val_accuracy'],color='cyan')
plt.xlabel('Epochs')
plt.ylabel('Validation Accuracy')
plt.title("Visualization of Validation Accuracy Result")
plt.show()