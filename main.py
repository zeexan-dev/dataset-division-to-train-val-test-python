import numpy as np
import os
import glob
import random
import math
import shutil

PATH_OF_DATA= './dataset/'

# create train, val, test directories
if os.path.exists(PATH_OF_DATA):
  if not os.path.exists(PATH_OF_DATA+'train'):
    os.mkdir(PATH_OF_DATA+'train')
  if not os.path.exists(PATH_OF_DATA+'test'):
    os.mkdir(PATH_OF_DATA+'test')
  if not os.path.exists(PATH_OF_DATA+'val'):
    os.mkdir(PATH_OF_DATA+'val')
  labels_list = os.listdir(PATH_OF_DATA)

  # create lables folder in train, val, test directories
  for label in labels_list:
    if label not in ['train','test','val']:
      if not os.path.exists(PATH_OF_DATA+'train/'+label):
        os.mkdir(PATH_OF_DATA+'train/'+label)
      if not os.path.exists(PATH_OF_DATA+'test/'+label):
        os.mkdir(PATH_OF_DATA+'test/'+label)
      if not os.path.exists(PATH_OF_DATA+'val/'+label):
        os.mkdir(PATH_OF_DATA+'val/'+label)

# set the percentage of data from labels for train, val and test
train_perc = 0.7  #70 %
val_perc = 0.2    #20%
test_perc = 0.1   #10%

for x in labels_list:
  if x not in ['train','test','val']:
    if os.path.exists(PATH_OF_DATA+x):
      
      images_names = os.listdir(PATH_OF_DATA+x)
      total_images = len(images_names)
      # print(str(total_images))

      # find number of items for train,val and test
      num_of_train = math.floor(total_images*train_perc)
      num_of_val = math.floor(total_images*val_perc)
      num_of_test = math.floor(total_images*test_perc)
      # print(str(num_of_train)+' '+str(num_of_val)+' '+str(num_of_test)+' '+'for '+x)

      # create list of items for train,val and test
      train_names = random.sample(images_names,num_of_train)
      for name in train_names:
        images_names.remove(name)
      val_names = random.sample(images_names,num_of_val)
      for name in val_names:
        images_names.remove(name)
      test_names = random.sample(images_names,num_of_test)
      print(x)
      print(str(len(train_names))+' '+str(len(val_names))+' '+str(len(test_names)))

      # move items to relevant directories
      PATH_OF_TRAIN = PATH_OF_DATA+'train/'+x+'/'
      PATH_OF_VAL = PATH_OF_DATA+'val/'+x+'/'
      PATH_OF_TEST = PATH_OF_DATA+'test/'+x+'/'

      for f in train_names:
        shutil.move(PATH_OF_DATA+x+'/'+f, PATH_OF_TRAIN + f)
      for f in val_names:
        shutil.move(PATH_OF_DATA+x+'/'+f, PATH_OF_VAL + f)
      for f in test_names:
        shutil.move(PATH_OF_DATA+x+'/'+f, PATH_OF_TEST + f)

      print('=========================================')