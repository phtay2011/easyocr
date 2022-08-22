from json import decoder
import os

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

# config
## 'ta','ch_sim','en','ms' -> 'tamil','simplified chinese',' english',
lang = ['ch_sim','en'] 
file_types = ('png','jpg','jpeg')

# General Params
#https://www.jaided.ai/easyocr/documentation/
decoder_ = 'beamsearch' #greedy', 'beamsearch', 'wordbeamsearch'.
paragraph_ = True # If line by line bounding box is preferred, change it `False`

# Text Detection Params
mag_ratio_ = 2.0 #Magnify text 

# Bounding Box Merging Params (Not in use)
slope_ths_ = 0.1
ycenter_ths_ = 0.5
height_ths_ = 0.5
width_ths_ = 0.5
add_margin_ = 0.1
x_ths_ = 1.0
y_ths_ = 0.5

#Generate bounding box and extract text
def ocr(decoder,paragraph,mag_ratio):
    reader = easyocr.Reader(lang)
    #image_name = '1.png'
    image = cv2.imread(image_name)
    result = reader.readtext(
        image, 
        decoder= decoder ,
        paragraph = paragraph, 
        mag_ratio = mag_ratio
        )
    for res in result:
        top_left = (int(res[0][0][0]), int(res[0][0][1])) # convert float to int
        bottom_right = (int(res[0][2][0]), int(res[0][2][1])) # convert float to int
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 3)
        #cv2.putText(image, res[1], (top_left[0], top_left[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
        #cv2.putText(image, res[1], (top_left[0]+200, top_left[1]), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
    cv2.imwrite('{}/easyOCR/final_image_{}'.format(folder_dir, image_name), image)    
    save_to_txt_file(result, image_name, folder_dir = '.')   
    return image, result
    


#Save result to text file
def save_to_txt_file(result, filename, folder_dir = '.'):
        txt_file = str("\n".join(str(el) for el in result))
        #open text file
        text_file = open("{}/easyOCR/final_text_{}.txt".format(folder_dir,filename), "w")
        #write string to file
        text_file.write(txt_file)
        
        #close file
        text_file.close()

#Add spaces in between words

#Loop through images in a folder

folder_dir = '/Users/taypaulhong/Desktop/Test Images' 
os.chdir(folder_dir)
for image_name in os.listdir(folder_dir):
    if image_name.split('.')[-1] in file_types:
        print(image_name)
        #RUN function
        image, result = ocr(decoder_, paragraph_, mag_ratio_)
        print (result)
