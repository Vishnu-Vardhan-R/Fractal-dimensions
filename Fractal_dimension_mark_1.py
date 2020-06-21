import numpy as np
import pylab as pl

"""
The simplest method is box counting: the idea is to fully cover the object with many boxes of a given size, 
count how many boxes are needed to cover the object and repeat the process for many box sizes. 
The scaling of the number of boxes covering the object with the size of the boxes gives an estimate 
for the fractal dimension of the object.
The idea is to simply bin the object in a histogram of variable bin sizes. 
This can be easily generalised to any dimensions, thanks to Numpy’s histrogramdd  function.

Reference : https://francescoturci.net/2016/03/31/box-counting-in-numpy/
"""


def rgb2gray(rgb_image):
    """
    This function converts the input image to grayscale image
    :return: grayscale image
    """
    r, g, b = rgb_image[:, :, 0], rgb_image[:, :, 1], rgb_image[:, :, 2]
    grayscale_image = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return grayscale_image


def find_non_zero_pixels(image):
    """"
    This function finds and lists pixels that are non-black
    :return: list of pixel values
    """
    lists = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i, j] > 0:
                lists.append((i, j))
    return lists


def graph_plot(scales, Ns):
    """
    This function plots a linear logarithmic graph between scale vs _____
    Then we do a linear regression to this graph
    :return: coefficients of the linear curve-fitting polynomial (slope & y-intercept)
    """
    # linear fit, polynomial of degree 1
    coefficients = np.polyfit(np.log(scales), np.log(Ns), 1)

    pl.plot(np.log(scales), np.log(Ns), 'o', mfc='none')
    pl.plot(np.log(scales), np.polyval(coefficients, np.log(scales)))
    pl.xlabel('log $\epsilon$')
    pl.ylabel('log N')
    # pl.savefig('Fractal_graph.pdf')
    pl.show()
    return coefficients


def main():
    filename = input("Enter image filename/directory:")     # input image filename/directory is given
    input_rgb_img = pl.imread(filename)
    image_width = input_rgb_img.shape[1]
    image_height = input_rgb_img.shape[0]

    print(f"The dimensions of the image: {image_width} x {image_height} pixels")
    grayscale_image = rgb2gray(input_rgb_img)

    pixels = find_non_zero_pixels(grayscale_image)      # finding all the non-zero pixels

    pixels = pl.array(pixels)       # converts lists to arrays
    print(pixels.shape)             # prints the dimension of array (no. of lists) & elements in each dimension

    # computing the fractal dimension
    # considering only scales in a logarithmic list
    scales = np.logspace(0.01, 1, num=10, endpoint=False, base=2)
    Ns = []

    # looping over several scales
    for scale in scales:
        print("======= Scale :", scale)
        # computing the histogram
        H, edges = np.histogramdd(pixels, bins=(np.arange(0, image_width, scale), np.arange(0, image_height, scale)))
        Ns.append(np.sum(H > 0))

    coeffs = graph_plot(scales, Ns)
    print(f"The slope of the curve is {coeffs[0]}")

    # the fractal dimension is the OPPOSITE of the fitting coefficient
    print(f"The Hausdorff dimension is {-coeffs[0]}")

    np.savetxt(f"{filename[:-3]}.txt", list(zip(np.log(scales), np.log(Ns))))


if __name__ == '__main__':
    main()