#!/usr/bin/env python
# coding: utf-8

# In[92]:


import numpy as np
import tensorflow as tf
import os
import cv2
import random
from tensorflow.keras.layers import *
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping
from collections import deque
import datetime
import json
import csv
import shutil
from urllib.request import urlopen
import time


# In[93]:


image_height, image_width = 64, 64
max_images_per_class = 8000
 
dataset_directory = "dataset"

classes_list = ["Fighting","Shooting","RoadAccidents","Robbery","Abuse","Arrest","Arson","Assault","Burglary","Explosion","Normal"]

 
model_output_size = len(classes_list)
print(model_output_size)


# In[94]:


model = tf.keras.models.load_model("C:/Users/rudra/Downloads/VigilAI (2)/VigilAI/model_8000.h5")


# In[95]:


def save_clip(frames):
    height, width, _ = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc('V','P','8','0')  
    frame_rate=15
    output_video = cv2.VideoWriter("C:/Users/rudra/Downloads/output_clip.webm", fourcc, frame_rate, (width, height))

    for frame in frames:
        output_video.write(frame)
    output_video.release()


# In[96]:


def get_location():
    try:
        # Create a geocoder instance
        url='http://ipinfo.io/json'
        response=urlopen(url)
        # Get the current GPS location
        data=json.load(response)
        coordinates=data['loc']
        city=data['city']
        return city,coordinates
    except:
        city,coordinates='NA','NA'
        return city,coordinates


# In[97]:


def get_date_and_time():
    data = datetime.datetime.now()
    data=str(data)
    date,time=data.split(' ')
    date=date.replace('-','_')
    time=time.replace(':','_')
    time=time.replace('.','_')
    return str(date),str(time)


# In[98]:


def create_database(crime_type):
    # Specify the current file path and the new file name
    current_file_path = "C:/Users/rudra/Downloads/VigilAI (2)/VigilAI/healthcare/healthcare/Eyebase/output_clip.webm"
    city,coordinates=get_location()

    date,time=get_date_and_time()

    new_file_name =str(city)+'_'+date+'+'+time+'.webm'
    file_path='Eyebase/'+new_file_name
    new_data = [file_path,crime_type,city,coordinates,date,time]

    csv_file = "C:/Users/rudra/Downloads/VigilAI (2)/VigilAI/healthcare/healthcare/AIbase.csv"

    with open(csv_file, 'a', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        # Append the new data to the CSV file
        writer.writerow(new_data)


    # Extract the directory and the extension from the current file path
    directory = os.path.dirname(current_file_path)
    extension = os.path.splitext(current_file_path)[1]

    # Create the new file path by combining the directory, new file name, and extension
    new_file_path = os.path.join(directory, new_file_name)

    # Rename the file
    os.rename(current_file_path, new_file_path)
    print("done")


# In[99]:


def add_to_database(crime_type):
    # Specify the source file path and the destination folder path
    source_file = "C:/Users/rudra/Downloads/output_clip.webm"
    destination_folder = "C:/Users/rudra/Downloads/VigilAI (2)/VigilAI/healthcare/healthcare/Eyebase"

    # Copy the file to the destination folder
    shutil.copy(source_file, destination_folder)
    create_database(crime_type)


# In[100]:


# def predict_on_live_video(video_file_path, output_file_path, window_size):
#     frame_count=0
#     frames=[]
#     crime_type='NA'
#     counter=0
#     # Initialize a Deque Object with a fixed size which will be used to implement moving/rolling average functionality.
#     predicted_labels_probabilities_deque = deque(maxlen = window_size)
 
#     # Reading the Video File using the VideoCapture Object
# #     video_reader = cv2.VideoCapture(video_file_path)
#     video_reader = cv2.VideoCapture(video_file_path)
 
#     # Getting the width and height of the video 
#     original_video_width = int(video_reader.get(cv2.CAP_PROP_FRAME_WIDTH))
#     original_video_height = int(video_reader.get(cv2.CAP_PROP_FRAME_HEIGHT))
 
#     # Writing the Overlayed Video Files Using the VideoWriter Object
#     # video_writer = cv2.VideoWriter(output_file_path, cv2.VideoWriter_fourcc(*'VP80'), 24, (original_video_width, original_video_height))
 
#     while True: 
 
#         # Reading The Frame
#         status, frame = video_reader.read() 
 
#         if not status:
#             break
 
#         # Resize the Frame to fixed Dimensions
#         resized_frame = cv2.resize(frame, (image_height, image_width))
         
#         # Normalize the resized frame by dividing it with 255 so that each pixel value then lies between 0 and 1
#         normalized_frame = resized_frame / 255
 
#         # Passing the Image Normalized Frame to the model and receiving Predicted Probabilities.
#         predicted_labels_probabilities = model.predict(np.expand_dims(normalized_frame, axis = 0))[0]
 
#         # Appending predicted label probabilities to the deque object
#         predicted_labels_probabilities_deque.append(predicted_labels_probabilities)
 
#         # Assuring that the Deque is completely filled before starting the averaging process
#         if len(predicted_labels_probabilities_deque) == window_size:
 
#             # Converting Predicted Labels Probabilities Deque into Numpy array
#             predicted_labels_probabilities_np = np.array(predicted_labels_probabilities_deque)
 
#             # Calculating Average of Predicted Labels Probabilities Column Wise 
#             predicted_labels_probabilities_averaged = predicted_labels_probabilities_np.mean(axis = 0)
 
#             # Converting the predicted probabilities into labels by returning the index of the maximum value.
#             predicted_max=np.max(predicted_labels_probabilities_averaged)

#             predicted_label = np.argmax(predicted_labels_probabilities_averaged)

#             if predicted_max>0.6 and predicted_label<10:
#                 predicted_label = np.argmax(predicted_labels_probabilities_averaged)
#                 frame_count=frame_count+1
#                 if frame_count<450:
#                     if counter==0:
#                         crime_type=classes_list[predicted_label]
#                         counter=1
#                     frames.append(frame)
#                     save_clip(frames)
#                 else:
#                     if len(frames)>100:    
#                         frame_count=0
#                         frames=[]
#             else:
#                 predicted_label=10 

                
#             # Accessing The Class Name using predicted label.
#             predicted_class_name = classes_list[predicted_label]

           
#         # Writing The Frame
#         # video_writer.write(frame)
 
 
#         cv2.imshow('CCTV FOOTAGE', frame)
 
#         key_pressed = cv2.waitKey(1)
 
#         if key_pressed == ord('q'):
#             break
            
#     add_to_database(crime_type)
#     cv2.destroyAllWindows()
     
#     # Closing the VideoCapture and VideoWriter objects and releasing all resources held by them. 
#     video_reader.release()
#     # video_writer.release()


# In[101]:


# count=0
import threading
# frame_save = []

class test:
    def __init__ (self,video_file_path):
        self.frame_count = 0 
        self.frames = []
        self.status=0
        self.crime_type = "NA"
        self.counter = 0
        self.video_file_path=video_file_path
        self.predicted_labels_probabilities_deque = deque(maxlen = 30)
        self.video_reader = cv2.VideoCapture(self.video_file_path)
        self.processing_thread = None
        self.is_processing = False
        self.window_size=30
        self.ti=None
        self.count=0
        self.lock=threading.Lock()
        self.t3=None
        self.start_time = time.time()
        self.end_time = 0


    def start_processing(self):
        print(self.video_file_path)
        self.is_processing = True
        print("gbg")
        # video_reader = cv2.VideoCapture(self.video_file_path)
        self.processing_thread = threading.Thread(target=self.process_video)
        self.processing_thread.start()
        print(self.video_file_path)
        # print(video_reader)
        # self.status,self.frames = video_reader.read()
        print(self.status)
        # return frames

    def stop_processing(self):
        self.is_processing = False
        if self.processing_thread is not None:
            # self.processing_thread.join()
            pass
    
    def process_video(self):
        
        # original_video_width = int(self.frames(cv2.CAP_PROP_FRAME_WIDTH))
        # original_video_height = int(self.frames(cv2.CAP_PROP_FRAME_HEIGHT))
        
        print("kkk")
        counter=0
        while self.is_processing:
            self.lock.acquire()
            print("lll")
            frames=self.frames
            status, frame = self.video_reader.read()
            if not status:
                print(self.status)
                break
            print("mmm")
            resized_frame = cv2.resize(frame, (image_height, image_width))
            normalized_frame = resized_frame / 255
            # self.processing_thread.join()
            self.lock.release()
            self.ti=threading.Thread(target=test.predict_on_live_video,args= [self,normalized_frame,frame,counter])
            self.ti.start()

            # ti.join()
            # predicted_labels_probabilities = model.predict(np.expand_dims(normalized_frame, axis = 0))[0]
            # self.predicted_labels_probabilities_deque.append(predicted_labels_probabilities)
            # if len(self.predicted_labels_probabilities_deque) == self.window_size:
            #     predicted_labels_probabilities_np = np.array(self.predicted_labels_probabilities_deque)
            #     predicted_labels_probabilities_averaged = predicted_labels_probabilities_np.mean(axis = 0)
            #     predicted_max=np.max(predicted_labels_probabilities_averaged)
            #     predicted_label = np.argmax(predicted_labels_probabilities_averaged)
            #     if predicted_max>0.6 and predicted_label<10:
            #         predicted_label = np.argmax(predicted_labels_probabilities_averaged)
            #         self.frame_count = self.frame_count + 1
            #         if frame_count<450:
            #             if counter == 0:
            #                 crime_type = classes_list[predicted_label]
            #                 counter = 1
            #             frames.append(frame)
            #             save_clip(frames)
            #         else:
            #             if len(frames)>100:
            #                 frame_count = 0
            #                 frames = []
            #     else:
            #         predicted_label= 10
            #     predicted_class_name = classes_list[predicted_label]
            cv2.imshow('CCTV FOOTAGE',frame)
            key_pressed = cv2.waitKey(1)
            if key_pressed == ord('q'):
                break
        cv2.destroyAllWindows()
        self.t3 = threading.Thread(target=save_clip,args=[self.frames])
        self.t3.start()
        self.end_time = time.time()
        print("time==",self.end_time-self.start_time)
        time.sleep(3)
        add_to_database(self.crime_type)
        # self.t3.join()
        print(threading.active_count())
            # video_reader.release()
        # t1 = threading.Thread(target=read_video,args=[])
        # t2 = threading.Thread(target=process_video,args=[])
        # t1.start()
        # t2.start()
        # t1.join()
        # t2.join()
    def predict_on_live_video(self,normalized_frame,frame,counter,window_size=30):
        # t3 = threading.Thread(target=save_clip,args=[self.frames])
        self.lock.acquire()
        # predicted_labels_probabilities_deque = deque(maxlen = window_size
        # print("predict",threading.active_count())
        predicted_labels_probabilities = model.predict(np.expand_dims(normalized_frame, axis = 0))[0]
        self.predicted_labels_probabilities_deque.append(predicted_labels_probabilities)
        if len(self.predicted_labels_probabilities_deque) == self.window_size:
                predicted_labels_probabilities_np = np.array(self.predicted_labels_probabilities_deque)
                predicted_labels_probabilities_averaged = predicted_labels_probabilities_np.mean(axis = 0)
                predicted_max=np.max(predicted_labels_probabilities_averaged)
                predicted_label = np.argmax(predicted_labels_probabilities_averaged)
                if predicted_max>0.6 and predicted_label<10:
                    predicted_label = np.argmax(predicted_labels_probabilities_averaged)
                    self.frame_count = self.frame_count + 1
                    print("counter",self.counter)
                    if self.frame_count<450:
                        print("frame_count",self.frame_count)
                        if self.counter == 0:
                            print("ayaya?")
                            self.crime_type = classes_list[predicted_label]
                            self.counter = 1
                        self.frames.append(frame)
                        # trying to save clip in a new thread
                        # save_clip(self.frames)
                        # frame_save = self.frames
                        # t3.start()
                    else:
                        if len(self.frames)>100:
                            self.frame_count = 0
                            # self.frames = []
                else:
                    self.frame_count = 0
                    # self.frames=[]
                    predicted_label= 10
                predicted_class_name = classes_list[predicted_label]
        else:
            self.frame_count=0
            # pass
        self.lock.release() 
        # self.ti.join()   
        # self.count=1
        # t2 = threading.Thread(target=test.process_video,args=[self])
        # t1 = threading.Thread(target=test.read_video,args=[self])
        # print(self.count)
        # t2.start()
        # t1.start()
        # # t1.join()
        # t2.join()
        



# In[102]:


# import tkinter as tk
# from tkinter.filedialog import askopenfilename
# root = tk.Tk()
# output_file_path = "C:/Users/rudra/OneDrive/Desktop"
# window_size = 30
# video_file_path = 0
# def start():
#     file_path = askopenfilename()
#     output_file_path = "C:/Users/rudra/OneDrive/Desktop"
#     window_size = 30
#     print(file_path)
#     video_file_path = file_path
#     predict_on_live_video(video_file_path, output_file_path, window_size)
# predict_on_live_video(video_file_path, output_file_path, window_size)
# # start()


# In[103]:


# import tkinter as tk
# from tkinter.filedialog import askopenfilename
# def button_click():
#     file_path = askopenfilename()

#     # Display the selected file path
#     # print("Selected file path:", file_path)
#     start(file_path)

# # Create the Tkinter root window
# button = tk.Button(root, text="Click Me!",command = start)
# button.pack()
# root.mainloop()
import tkinter as tk
from tkinter.filedialog import askopenfilename
root = tk.Tk()
root.geometry("600x600")
# output_file_path = "C:/Users/rudra/OneDrive/Desktop"
# window_size = 30
# video_file_path = 0
def start():
    # print("tkinter",threading.active_count())
    file_path = askopenfilename()
    output_file_path = "C:/Users/dwive/Desktop"
    window_size = 30
    print(file_path)
    video_file_path = file_path
    my_object = test(video_file_path)
    # print("start")
    my_object.start_processing()
def start_camera():
    file_path = 0
    output_file_path = "C:/Users/dwive/Desktop"
    window_size = 30
    print(file_path)
    video_file_path = file_path
    my_object = test(video_file_path)
    # print("start")
    my_object.start_processing()

# predict_on_live_video(video_file_path, output_file_path, window_size)
# start()


# In[104]:


# import tkinter as tk
# from tkinter.filedialog import askopenfilename
def button_click():
    file_path = askopenfilename()

    # Display the selected file path
    # print("Selected file path:", file_path)
    start(file_path)

# def cam():
#     cam_start(0)

# Create the Tkinter root window
button = tk.Button(root,font="comicsans 35 bold",bg="yellow",padx=30,pady=20, text="Click Me!",command = start)
button1 = tk.Button(root,font="comicsans 35 bold",bg="yellow",padx=30,pady=20, text="Camera!",command = start_camera)
button.place(x=150,y=50)
button1.place(x=150,y=350)
root.mainloop()

# # tkinter good button
# button = tk.Button(root,font="comicsans 35 bold",bg="yellow",padx=30, text="Click Me!",command = start)
# button.place(x= 100,y=300)
# button.pack(pady= 120)

# button2 = tk.Button(root,font="comicsans 35 bold",bg="yellow",padx=30, text="Live Cam!",command = cam_start)
# button2.place(x=100,y=400)
# button.pack(pady= 120)
# root.mainloop()


# In[ ]:





# In[ ]:




