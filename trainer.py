from keras.models import Sequential
from keras.models import Model
from keras.layers import Conv2D,Dense,Flatten,Activation,Dropout,MaxPool2D
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint
from keras.applications import ResNet50
import numpy as np
import os
from sklearn.model_selection import train_test_split
import cv2

def data_preparation():
    path='dataset'
    img_size=100
    data=[]
    target=[]
    classes=os.listdir(path)
    print(classes)
    label_dict={}
    for i,c in enumerate(classes):
        label_dict[c] = i
    print(label_dict)


    for clas in classes:
        data_path=os.path.join(path,clas)
        image_names=os.listdir(data_path)

        for image_name in image_names:
            image_path=os.path.join(data_path,image_name)
            image=cv2.imread(image_path)

            #gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            resized=cv2.resize(image,(img_size,img_size))
            data.append(resized)
            target.append(label_dict[clas])
    data=np.array(data)/255
    data=np.reshape(data,(data.shape[0],img_size,img_size,3))
    target=np.array(target)
    return(data,target)


data,target=data_preparation()
target=np_utils.to_categorical(target)

train_data,test_data,train_target,test_target=train_test_split(data,target,test_size=0.1)

def custom_model():
    model=Sequential()

    model.add(Conv2D(512,(3,3),input_shape=data.shape[1:]))
    model.add(Activation('relu'))
    model.add(MaxPool2D(pool_size=(2,2)))

    model.add(Conv2D(256,(3,3)))
    model.add(Activation('relu'))
    model.add(MaxPool2D(pool_size=(2,2)))

    model.add(Flatten())
    model.add(Dropout(0.5))
    model.add(Dense(50,activation='relu'))
    model.add(Dense(2,activation='softmax'))

    model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
    return model

def resnet_model():
    pretrained_model=ResNet50(include_top=False,input_shape=data.shape[1:])
    pretrained_model.trainable=False

    flat1=Flatten()(pretrained_model.layers[-1].output)
    drop1=Dropout(0.5)(flat1)
    class1=Dense(1024,activation='relu')(drop1)
    output=Dense(2,activation='softmax')(class1)

    model=Model(inputs=pretrained_model.inputs,outputs=output)

    return model




model=resnet_model()
model.summary()

model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
checkpoint=ModelCheckpoint('model-{epoch:03d}.model',monitor='val_loss',verbose=0,save_best_only=True,mode='auto')

history=model.fit(train_data,train_target,epochs=20,verbose=1,callbacks=[checkpoint],validation_split=0.2)

from matplotlib import pyplot as plt

plt.plot(history.history['loss'],'r',label='training loss')
plt.plot(history.history['val_loss'],label='validation loss')
plt.xlabel('# epochs')
plt.ylabel('loss')
plt.legend()
plt.show()

plt.plot(history.history['accuracy'],'r',label='training accuracy')
plt.plot(history.history['val_accuracy'],label='validation accuracy')
plt.xlabel('# epochs')
plt.ylabel('loss')
plt.legend()
plt.show()

#print(model.evaluate(test_data,test_target))

