import numpy as np
import skimage as sk
import skimage.io as skio

# image functions
def display_image(im):
    skio.imshow(im)
    skio.show()

# file util functions
def get_file(fname): 
    # read in the image
    impath = f"../images/{fname}"
    imname = fname.split(".")[0]
    im = skio.imread(impath)

    # convert to double
    im = sk.img_as_float(im)

    return imname, im

def save_file(imname, im_out):
    fname = f"../images/{imname}"
    print(f"Saving output as {fname}...")
    skio.imsave(fname, im_out)
