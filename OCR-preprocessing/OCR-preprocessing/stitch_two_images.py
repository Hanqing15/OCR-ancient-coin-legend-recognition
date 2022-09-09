# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 15:36:55 2022

@author: YANG Hanqing
"""
import PIL.Image as Image
import os

# Stitch the obverse and reverse images of a coin together on a single image
img_path = 'C://Users//Ana//Desktop//ancient_monaie//Copie Base_12_2018//1//'  # you could change into your own dataset path
img_save_path = 'C:\\Users\\Ana\Desktop\\ancient_monaie\\Code_YANG\\OCR-preprocessing\\OCR-preprocessing\\Coin_Samples\\toulouse_coins_1'# It's necessary to add the absolu path
img_list = os.listdir(img_path)
img_list.sort(key=lambda x: int(x[:-24]))

def stitch_images(img_path, img_save_path):
    # Important: Get all the images in the current folder and sort them by image number
    img_list = os.listdir(img_path)
    img_list.sort(key=lambda x: int(x[:-24]))
    os.chdir(img_save_path)
    for i in range(0, len(img_list) - 1, 2):
        if img_list[i][:-24] == img_list[i + 1][:-24]:
            img1 = Image.open(img_path + img_list[i])
            img2 = Image.open(img_path + img_list[i + 1])
            new_img = Image.new(mode='RGB', size=((787 * 2), 787),
                                color=(255, 255, 255))  # Remain the original pixel of the two images by setting size
            new_img.paste(img1, box=(0, 0))
            new_img.paste(img2, box=(787, 0))
            new_img.save(os.path.join(img_save_path, "toulouse_1_" + str(int(i / 2 + 1)) + '.jpg'))


# Run
stitch_images(img_path, img_save_path)







