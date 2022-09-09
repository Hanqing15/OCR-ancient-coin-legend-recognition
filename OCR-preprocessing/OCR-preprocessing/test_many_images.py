#-*- coding: utf-8 -*-
"""
Created on Sat Mar 05 13:55:06 2016
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
img_path = 'Coin_Samples/toulouse_coins_1'
save_path_avers = 'Coin_Samples\\toulouse_coins_1_obverse'
save_path_revers = 'Coin_Samples\\toulouse_coins_1_reverse'
save_path_atelier = 'Coin_Samples\\toulouse_coins_1_mintMark'
img_list = os.listdir(img_path)
# Sor Sort the images to avoid disorder
img_list.sort(key = lambda x:int(x[11:-4]))

for img_name in img_list:
    sample_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), img_path, img_name )

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


    # Save stripes from Toulouse coins
    # for obverse, the second parameter "1" refers to obverse legend
    toto.avers.save_stripe(os.path.join(save_path_avers,img_name[:-4] + '_obverse'+ '.jpg' ), 1)
    # for reverse, the second parameter "1" refers to reverse legend
    toto.revers.save_stripe(os.path.join(save_path_revers, img_name[:-4] + '_reverse' + '.jpg'), 1)
    # for reverse, the second parameter "2" refers to reverse mintMark('atelier' in French)
    toto.revers.save_stripe(os.path.join(save_path_atelier, img_name[:-4] + '_mintMark' + '.jpg'), 2)





