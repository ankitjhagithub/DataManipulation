#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:14:41 2019

@author: uesr
"""

#converting the image into the numpy format
import numpy as np
import pandas as pd
import os
import torch
from PIL import Image


ip_path = "/home/uesr/Desktop/Cityscapes/" 
op_path = "/home/uesr/Desktop/Cityscapes/results/"


#creating a folder to store the numpy array of images
if not os.path.exists(op_path):
    os.makedirs(op_path)

if not os.path.exists(os.path.join(op_path,'train')):
    os.makedirs(os.path.join(op_path,'train'))    
if not os.path.exists(os.path.join(os.path.join(op_path,'train'),'image')):
    os.makedirs(os.path.join(os.path.join(op_path,'train'),'image'))
if not os.path.exists(os.path.join(os.path.join(op_path,'train'),'mask')):
    os.makedirs(os.path.join(os.path.join(op_path,'train'),'mask'))


if not os.path.exists(os.path.join(op_path,'val')):
    os.makedirs(os.path.join(op_path,'val'))
if not os.path.exists(os.path.join(os.path.join(op_path,'val'),'image')):
    os.makedirs(os.path.join(os.path.join(op_path,'val'),'image'))
if not os.path.exists(os.path.join(os.path.join(op_path,'val'),'mask')):
    os.makedirs(os.path.join(os.path.join(op_path,'val'),'mask'))
    
if not os.path.exists(os.path.join(op_path,'test')):
    os.makedirs(os.path.join(op_path,'test'))
if not os.path.exists(os.path.join(os.path.join(op_path,'test'),'image')):
    os.makedirs(os.path.join(os.path.join(op_path,'test'),'image'))
if not os.path.exists(os.path.join(os.path.join(op_path,'test'),'mask')):
    os.makedirs(os.path.join(os.path.join(op_path,'test'),'mask'))
  

image_dir = os.path.join(os.path.join(ip_path,'leftImg8bit'),'test')
target_dir = os.path.join(os.path.join(ip_path,'gtFine'),'test')    

images = []
targets = []
#target_name = ''
for city in os.listdir(image_dir):
    img_dir = os.path.join(image_dir,city)
    tar_dir = os.path.join(target_dir,city)
    for file_name in os.listdir(img_dir):
        images.append(os.path.join(img_dir,file_name))
        target_name = '{}_{}'.format(file_name.split('_leftImg8bit')[0],'{}_labelIds.png'.format('gtFine'))
        targets.append(os.path.join(tar_dir,target_name))
        
    
for i in range(len(images)):
    img = Image.open(images[i])
    img = np.asarray(img,dtype='uint8')
    tar = Image.open(targets[i])
    tar =np.asarray(tar,dtype='uint8')
    f_i = os.path.join(op_path,'test/image',str(i))
    f_t = os.path.join(op_path,'test/mask',str(i))
    np.save(f_i,img)
    np.save(f_t,tar)
    
    
    