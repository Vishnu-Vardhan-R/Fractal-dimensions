from PIL import Image, ImageOps
import math

SCALE = .5


def main():
    filename = input("Enter the image directory: ")
    image = Image.open(filename)
    # image.show()

    grayscale_copy = image.convert(mode='L')
    grayscale_copy.show()

    # inverted_copy = invert_the_image(grayscale_copy)
    # inverted_copy = ImageOps.invert(grayscale_copy)
    # inverted_copy.show()

    #bw_copy = grayscale_copy.convert(mode='1')
    #bw_copy.show()

    scaled_image = scaling(grayscale_copy)
    scaled_image.show()

    no_of_boxes_1 = count_no_of_boxes(grayscale_copy)
    no_of_boxes_2 = count_no_of_boxes(scaled_image)

    fractal_dimension = math.log(no_of_boxes_2 / no_of_boxes_1) / math.log(SCALE)
    print(f"The Fractal dimension is {float(fractal_dimension)}")


def count_no_of_boxes(image):
    count = 0
    pixel = image.load()
    image = image.convert("RGB")
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))
            # print(r, g, b)
            if (r, g, b) > (0, 0, 0):
                count += 1
    print(f"No. of boxes = {count}")
    return count


def scaling(img):
    image = img.copy()
    scaled_image = image.resize((int(image.width * SCALE), int(image.height * SCALE)), resample=Image.BOX)
    return scaled_image


def invert_the_image(img):
    image = img.copy()
    pixel = img.load()
    image = image.convert("RGB")
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            r, g, b = img.getpixel((x, y))
            pixel[x, y] = (255 - r, 255 - g, 255 - b)
    return image


if __name__ == '__main__':
    main()
