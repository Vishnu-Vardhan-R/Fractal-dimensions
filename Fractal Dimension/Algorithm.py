from PIL import Image, ImageOps
import math
"""
Box counting is a method of gathering data for analyzing complex patterns 
by breaking a data-set, object, image, etc. into smaller and smaller pieces, 
typically "box"-shaped, and analyzing the pieces at each smaller scale.

This program aims to analyse the input image using box-counting method to
find the Fractal dimension of the input image. However, the program is not 
intended for all type of images in-general. 
Images have to be converted to a form where the required geometry must be in 
shades of white and the un-necessary background should be in black.
For this, I have provided certain implicit functions like Inverted_copy,
bw_copy as comments, which can be used to achieve the required condition. 
"""


SCALE = .5


def main():
    filename = input("Enter the image directory: ")
    image = Image.open(filename)
    # image.show()

    grayscale_copy = image.convert(mode='L')                # converts input image to grayscale image
    grayscale_copy.show()

    # inverted_copy = ImageOps.invert(grayscale_copy)       # inverts the input image
    # inverted_copy.show()

    # bw_copy = grayscale_copy.convert(mode='1')            # converts input image to black-white format
    # bw_copy.show()

    scaled_image = scaling(grayscale_copy)
    scaled_image.show()

    no_of_boxes_1 = count_no_of_boxes(grayscale_copy)
    no_of_boxes_2 = count_no_of_boxes(scaled_image)
    
    # calculates fractal dimension
    fractal_dimension = math.log(no_of_boxes_2 / no_of_boxes_1) / math.log(SCALE)
    print(f"The Fractal dimension is {float(fractal_dimension)}")


def count_no_of_boxes(image):
    """
    This function analyses the given image for non-black pixels
    and counts them.
    :param image:
    :return: no. of boxes that are non-black
    """
    count = 0
    pixel = image.load()
    image = image.convert("RGB")                # converts to (r,g,b) format (not RGB image) for processing
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))
            if (r, g, b) > (0, 0, 0):           # (r, g, b) > (0, 0, 0) represents non-black colours
                count += 1
    print(f"No. of boxes = {count}")
    return count


def scaling(img):
    """
    This function either scales up/down the input image.
    This scaling process can be done with different methods
    Ex: BILINEAR, BICUBIC, BOX, etc
    I have preferred BOX here for higher precision.
    :param img:
    :return: Re-sized image
    """
    image = img.copy()
    scaled_image = image.resize((int(image.width * SCALE), int(image.height * SCALE)), resample=Image.BOX)
    return scaled_image


if __name__ == '__main__':
    main()
