# coding: utf-8

# In[1]:
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
from glob import glob

# 載入檔案位址
training_dir = "./trainingtest/train"
validation_dir = "./trainingtest/val"
image_files = glob(training_dir + '/*/*.*')
valid_image_files = glob(validation_dir + '/*/*.*')


# In[2]:
# 取得類別數量
folders = glob(training_dir + '/*')
num_classes = len(folders)
print ('Total Classes = ' + str(num_classes))


# In[3]:
#AlexNet網路模型建立

# importing the libraries for model training
from keras.models import Model
from keras.layers import Flatten, Dense
from keras.applications import VGG16

'''
IMAGE_SIZE = [227, 227]


# loading the weights of VGG16 without the top layer. These weights are trained on Imagenet dataset.
# input_shape = (64,64,3) as


vgg = VGG16(input_shape = IMAGE_SIZE + [3], weights = 'imagenet', include_top = False)

# this will exclude the initial layers from training phase as there are already been trained.
for layer in vgg.layers:
    layer.trainable = False

x = Flatten()(vgg.output)
x = Dense(128, activation = 'relu')(x)
x = Dense(num_classes, activation = 'softmax')(x)  # adding the output layer with softmax function as this is a multi label classification problem.

model = Model(inputs = vgg.input, outputs = x)
'''


from keras.models import Sequential
from keras.layers import Dense,Flatten,Dropout
from keras.layers.convolutional import Conv2D,MaxPooling2D

IMAGE_SIZE = [227, 227]

model = Sequential()
model.add(Conv2D(96,(11,11),strides=(4,4),input_shape=(227,227,3),padding='valid',activation='relu',kernel_initializer='uniform'))
model.add(MaxPooling2D(pool_size=(3,3),strides=(2,2)))
model.add(Conv2D(256,(5,5),strides=(1,1),padding='same',activation='relu',kernel_initializer='uniform'))
model.add(MaxPooling2D(pool_size=(3,3),strides=(2,2)))
model.add(Conv2D(384,(3,3),strides=(1,1),padding='same',activation='relu',kernel_initializer='uniform'))
model.add(Conv2D(384,(3,3),strides=(1,1),padding='same',activation='relu',kernel_initializer='uniform'))
model.add(Conv2D(256,(3,3),strides=(1,1),padding='same',activation='relu',kernel_initializer='uniform'))
model.add(MaxPooling2D(pool_size=(3,3),strides=(2,2)))
model.add(Flatten())
model.add(Dense(4096,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(4096,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes,activation='softmax'))
model.compile(loss='categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])
model.summary()


# In[4]:



# importing the libraries image Augmentation
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.vgg16 import preprocess_input

training_datagen = ImageDataGenerator(
                                    rescale=1./255,
                                    shear_range=0.2, 
                                    zoom_range=0.2,
                                    horizontal_flip=True,
                                    preprocessing_function=preprocess_input)

validation_datagen = ImageDataGenerator(rescale = 1./255, preprocessing_function=preprocess_input)

training_generator = training_datagen.flow_from_directory(training_dir, target_size = IMAGE_SIZE, batch_size = 32, class_mode = 'categorical')
validation_generator = validation_datagen.flow_from_directory(validation_dir, target_size = IMAGE_SIZE, batch_size = 32, class_mode = 'categorical')


# The labels are stored in class_indices in dictionary form. 
# checking the labels
training_generator.class_indices

# In[5]:
#參數設定

#training_images = 10500
#validation_images = 3000

training_images = len(image_files)
validation_images = len(valid_image_files)
epochs = 100
batch_size = 32
steps_per_epoch = np.int(training_images/batch_size)
validation_steps = np.int(validation_images/batch_size)


history = model.fit_generator(training_generator,
                   steps_per_epoch = steps_per_epoch,
                   epochs = epochs,
                   validation_data = validation_generator,
                   validation_steps = validation_steps)

model.save('my_model.h5')  # creates a HDF5 file 'my_model.h5'




# In[6]:
#acc與loss 的圖表輸出

# Plot the train and validation loss
plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='val loss')
plt.legend()
plt.show()

# Plot the train and validation accuracies
plt.plot(history.history['accuracy'], label='train acc')
plt.plot(history.history['val_accuracy'], label='val acc')
plt.legend()
plt.show()

#輸出第1、50、100次數值
print ('Training Accuracy = ' + str(history.history['accuracy'][0]))
print ('Training Loss = ' + str(history.history['loss'][0]))
print ('Validation Accuracy = ' + str(history.history['val_accuracy'][0]))
print ('Validation Loss = ' + str(history.history['val_loss'][0]))

print ('Training Accuracy = ' + str(history.history['accuracy'][49]))
print ('Training Loss = ' + str(history.history['loss'][49]))
print ('Validation Accuracy = ' + str(history.history['val_accuracy'][49]))
print ('Validation Loss = ' + str(history.history['val_loss'][49]))

print ('Training Accuracy = ' + str(history.history['accuracy'][99]))
print ('Training Loss = ' + str(history.history['loss'][99]))
print ('Validation Accuracy = ' + str(history.history['val_accuracy'][99]))
print ('Validation Loss = ' + str(history.history['val_loss'][99]))
