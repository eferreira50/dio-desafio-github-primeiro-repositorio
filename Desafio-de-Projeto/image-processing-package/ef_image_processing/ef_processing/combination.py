#necessary imports
import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity 

#receive image 1 and image 2 as parameter
def find_difference(image1, image2):
    """
    Finds the difference between two images.
    """
    assert image1.shape == image2.shape, "Specify 2 images with de same shape."
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True)
    print("Similarity of the images: {}".format(score))
    normalized_difference_image = (difference_image - np.min(difference_image)) / (np.max(difference_image) - np.min(difference_image))
    return normalized_difference_image

def transfer_histogram(image1, image2):
    """
    Transfers the histogram of image1 to image2.
    """
    matched_image = match_histograms(image1, image2, multichannel=True)
    return matched_image