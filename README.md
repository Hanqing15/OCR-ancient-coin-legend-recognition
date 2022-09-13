# OCR-ancient-coin-legend-recognition
`OCR` `Reading coin legend` `OCR evaluation metrics` 
## 1. What is it for？
The aim here is to recognize the legends on coins from the ancient Roman Imperial period which includes the obverse and reverse legends as well as the mint mark on the bottom of reverse. Also, a metric to evaluate the recognition results has been given.

## 2. How to make it work?
 Code here consists of three main steps:

### Step-1 Stitch the obverse and reverse coin pictures on one picture as the input.
* Run `stitch_two_images.py` file in `OCR_preprocessing` folder. Then, you could get the image, for example, below:

![toulouse_1_1](OCR-preprocessing/OCR-preprocessing/Coin_Samples/toulouse_coins_1/toulouse_1_1.jpg "The obeverse and reverse coin images after being stitched")
 
### Step-2 Preprocess the images and save them for OCR.
* Run `test_one_image.py` file or `test_many_images` file in `OCR_preprocessing` folder.
* After this step, you could get all processed images (Strip images) and save them in the corresponding folders separately in `Coin_Samples`. They will be used in next step of OCR.
 * Example of processed image (Strip image): 
 
 ![Strip image of toulouse_1_1](OCR-preprocessing/OCR-preprocessing/Coin_Samples/toulouse_coins_1_obverse//toulouse_1_1_obverse.jpg "The preprocessed image of toulouse_1_1 obverse coin ")
 
 ### Step-3 Do OCR and the error evaluation metrics.
 * Highly recommended to open `OCR_Metrics_CER_WER_Colab` in `Jupyter Notebook`.
 
 
 
