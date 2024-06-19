import json


class CannyParams(object):

    def __init__(self, threshold1, threshold2, apertureSize, L2gradient):
        self.threshold1 = threshold1
        self.threshold2 = threshold2
        self.apertureSize = apertureSize
        self.L2gradient = L2gradient

    @staticmethod
    def getObject(file_path="configs/params.json"):
        file = open(file_path)
        if file:
            data: dict = json.load(file)
            key = 'canny_edge_detection_params'
            if key in data:
                threshold1 = data[key]['threshold1']
                threshold2 = data[key]['threshold2']
                apertureSize = data[key]['apertureSize']
                L2gradient = data[key]['L2gradient']

                return CannyParams(
                    threshold1,
                    threshold2,
                    apertureSize,
                    L2gradient
                )
            else:
                return None
