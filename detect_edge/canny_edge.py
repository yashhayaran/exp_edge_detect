import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from configs.config import CannyParams


class CannyEdgeDetector(object):
    def __int__(self, params):
        self.params: CannyParams = params

    def detect(self, image_path):
        if self.params is None:
            raise Exception("Params are not defined. Please set the params for Canny Edge.")

        image1 = cv.imread(image_path)
        image = cv.imread(image_path)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        use_it = gray
        blurred = cv.GaussianBlur(gray, (3, 3), 0)
        use_it = blurred

        canny = cv.Canny(image=use_it,
                         threshold1=self.params.threshold1,
                         threshold2=self.params.threshold2,
                         apertureSize=self.params.apertureSize,
                         L2gradient=self.params.L2gradient)

        cnts = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        for c in cnts:
            cv.drawContours(image, [c], 0, (36, 255, 12), 2)

        plt.subplot(121), plt.imshow(image1)
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])

        plt.subplot(122), plt.imshow(image)
        plt.title('Edge Image with Aperture + L2gradient'), plt.xticks([]), plt.yticks([])

        plt.show()

        # cv.imshow('canny', canny)
        # cv.imshow('image', image)
        cv.imwrite('canny.png', canny)
        cv.imwrite('image.png', image)
        # cv.waitKey(0)
