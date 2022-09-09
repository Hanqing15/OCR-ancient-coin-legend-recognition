# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 15:36:55 2022

@author: YANG Hanqing
"""

import cv2
import os
from PIL import Image
from Algorithm import Piece
from skimage import io

import numpy as np
import pytesseract
from pytesseract import Output
import cv2

try:
    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont
except ImportError:
    import Image

# Warning: It should stitch the obverse and reverse images together on a single image before run test file.
# File path
sample_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Coin_Samples', 'toulouse_coins_1/toulouse_1_21.jpg')

# Show Image
Image.open(sample_path).show()
# Import Coin (Piece in French)
toto = Piece.Piece(sample_path)
# Generate Obverse (Avers in French) and Reverse (Revers in French)
toto.generate_aversrever()
# Show circles coins
toto.show_coin_with_circles()


# Uncoil the coin and generate a stripe for both obverse and reverse
toto.avers.coin2stripe()
toto.revers.coin2stripe()

# Show stripes for obverse and reverse
toto.avers.show_stripe()
toto.revers.show_stripe()

# Extract words
toto.avers.extract_words() #It's not necessary for save stripe, but to see the effect of binarization
toto.revers.extract_words()

# Save stripes
# for obverse, the second parameter "1" refers to obverse legend
toto.avers.save_stripe("Coin_Samples\\Toulouse_obverse_strip_save.jpg", 1)
# for reverse, the second parameter "1" refers to reverse legend
toto.revers.save_stripe("Coin_Samples\\Toulouse_reverse_strip_save.jpg", 1)
# for reverse, the second parameter "2" refers to reverse mintMark('atelier' in French)
toto.revers.save_stripe("Coin_Samples\\Toulouse_mintMark_strip_save.jpg", 2)






