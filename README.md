# dataset-division-to-train-val-test-python
python script for dividing image data to train test and val

If you have an image dataset in the following structure of directories
- dataset
  - label_1 directory
  - label_2 directory
  - label_3 directory
  - label_n-1 directory
  - label_n directory

then this python script (main.py) will divide the images present in each label directories into train, val and test directories.

## set the following variables according to your requirements in main.py

`PATH_OF_DATA= './dataset/'`<br />
`train_perc = 0.7  #70% `<br />
`val_perc = 0.2    #20% `<br />
`test_perc = 0.1   #10% `<br /> 
