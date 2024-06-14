import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def canny_edge_1(image_path):
    img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    assert img is not None, "file could not be read, check with os.path.exists()"

    edges1 = cv.Canny(image=img,
                      threshold1=8000,
                      threshold2=8000)

    edges2 = cv.Canny(image=img,
                      threshold1=8000,
                      threshold2=8000,
                      apertureSize=5)

    edges3 = cv.Canny(image=img,
                      threshold1=8000,
                      threshold2=8000,
                      apertureSize=5,
                      L2gradient=False)

    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(122), plt.imshow(edges3, cmap='gray')
    plt.title('Edge Image with Aperture + L2gradient'), plt.xticks([]), plt.yticks([])

    plt.show()


def canny_edge_2(image_path):
    image1 = cv.imread(image_path)
    image = cv.imread(image_path)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    use_it = gray
    blurred = cv.GaussianBlur(gray, (3, 3), 0)
    use_it = blurred
    canny = cv.Canny(image=use_it,
                     threshold1=1500,
                     threshold2=1200,
                     apertureSize=5,
                     L2gradient=True)

    cnts = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    for c in cnts:
        cv.drawContours(image, [c], 0, (36, 255, 12), 2)

    plt.subplot(121), plt.imshow(image1)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(122), plt.imshow(image)
    plt.title('Edge Image with Aperture + L2gradient'), plt.xticks([]), plt.yticks([])

    plt.show()

    #cv.imshow('canny', canny)
    #cv.imshow('image', image)
    cv.imwrite('canny.png', canny)
    cv.imwrite('image.png', image)
    #cv.waitKey(0)
