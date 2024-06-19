# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from configs.config import CannyParams
from detect_edge import canny_edge

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    params = CannyParams.getObject()
    if params is not None:
        detector = canny_edge.CannyEdgeDetector(
            params
        )

        images = [
            "assets/photo1717552254.jpeg",
            "assets/TC1-CAM11662615487.305533.jpg"
        ]

        detector.detect(
            images[1]
        )

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
