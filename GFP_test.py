__author__ = 'urvish'
import sys
import scipy
import scipy.ndimage
import numpy
import scipy.misc
from matplotlib import pyplot as plt
def main(gfp_filepath):

    print gfp_filepath
    image = scipy.ndimage.imread(gfp_filepath)
    print image.shape
    green_only =  image[:,:,2]
    print "greenOnly   "  +  str(green_only)

    derivative_of_gradient =  scipy.ndimage.filters.gaussian_gradient_magnitude(green_only, .35 , mode="reflect")
    #imageview = numpy.amax(derivative_of_gradient)*255 / derivative_of_gradient

    #scipy.misc.imshow( imageview)
    numpy.amax((green_only))
    lbl, dim = scipy.ndimage.label(derivative_of_gradient)
    print "dim " + str(dim)
    print "lable " +  str(lbl)

    gaussian_output = scipy.ndimage.filters.gaussian_filter(lbl, 4.4)

    lbl, dim = scipy.ndimage.label(gaussian_output)
    print "dim " + str(dim)
    print "lable " +  str(lbl)

    loc = scipy.ndimage.find_objects(lbl, max_label=1)[0]

    location =  green_only[loc]
    print location
    print location.shape

    fig, ax = plt.subplots()
    ax.imshow(green_only)


    ax.set_title("original")

    fig, ax = plt.subplots()
    ax.imshow(lbl)

    fig, ax = plt.subplots()
    ax.imshow(location)



    plt.show()

if __name__ == "__main__":
    main(sys.argv[1])