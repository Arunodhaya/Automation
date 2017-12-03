import os
import json
import urllib

import h5py
import numpy as np
import pickle as pk
import tensorflow as tf
import label_image
import parts_label_image

# load models
def engine(img_path):
    print(img_path)
    result_dictionary=label_image.prediction(img_path)
    parts_result=parts_label_image.prediction(img_path)
#    img_224 = prepare_img_224(img_path)
#    g1 = car_categories_gate(img_224, first_gate)
    result = {'gate1': 'Car validation check: ', 
   'gate1_result': 0, 
   'gate1_message':result_dictionary, #{0: 'Are you sure this is a picture of your car? Please retry your submission.', 1: 'Hint: Try zooming in/out, using a different angle or different lighting'},
   'gate2':parts_result,
   'gate2_result': None,
   'gate2_message': {0: None, 1: None},
   'location': None,
   'severity':result_dictionary,
   'final': 'Damage assessment unsuccessful!'}
    print(result)
    return result
        
