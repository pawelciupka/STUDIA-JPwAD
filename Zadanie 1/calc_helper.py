import statistics
from collections import Counter


class CalcHelper(object):

    @staticmethod
    def calculate_median(collection):
        return statistics.median(collection)

    @staticmethod
    def calculate_minimum(collection):
        return min(collection)

    @staticmethod
    def calculate_maximum(collection):
        return max(collection)

    @staticmethod
    def calculate_dominant(collection):
        return Counter(collection).most_common(1)
