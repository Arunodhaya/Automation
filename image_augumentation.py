# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 12:10:17 2017

@author: win10
"""

import Augmentor
p = Augmentor.Pipeline(r"C:\Users\win10\Saved Games\Desktop\car-damage-detective-master\ML model\imagedataset\parts damage\bumber")
p.rotate(probability=0.9, max_left_rotation=10, max_right_rotation=10)
p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)
#p.random_distortion(probability=0.8,grid_height=20,grid_width=20,magnitude=0.5)
p.skew_tilt(probability=0.7,magnitude=1)
p.histogram_equalisation(probability=0.8)
p.sample(20)
