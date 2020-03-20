import numpy


class FileHelper(object):

    @staticmethod
    def load_data(filepath, delimiter=','):
        collection = numpy.genfromtxt(
            filepath, dtype=None, delimiter=delimiter, names=True)
        return collection
