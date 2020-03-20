import numpy

from file_helper import FileHelper
from output_helper import OutputHelper
from plot_helper import PlotHelper


class Main(object):

    @staticmethod
    def first_step():

        collection = FileHelper.load_data('fertility_Diagnosis.data')
        collection_column_name = collection.dtype.names

        for column_name in collection_column_name:
            print(column_name)
            if isinstance(collection[column_name][0], numpy.float64) or isinstance(collection[column_name][0], numpy.int64) or isinstance(collection[column_name][0], numpy.int32):
                print(OutputHelper.get_minimum_output(collection[column_name]))
                print(OutputHelper.get_maximum_output(collection[column_name]))
                print(OutputHelper.get_median_output(collection[column_name]))
                print("\n")
            elif isinstance(collection[column_name][0], numpy.bytes_):
                print(OutputHelper.get_dominant_output(
                    collection[column_name]))
                print("\n")

    @staticmethod
    def second_step():
        collection = FileHelper.load_data('fertility_Diagnosis_quantity.data')
        collection_column_name = collection.dtype.names

        collection_list = numpy.array(collection.tolist())

        # Utworzenie macierzy z listy (utworzenie dwuwymiarowej tablicy)
        matrix = numpy.transpose(collection_list)

        # Utworzenie macierzy korelacji
        correlation_matrix = numpy.corrcoef(matrix)

        # Utworzenie macierzy trójkątnej
        triangular_matrix = numpy.triu(correlation_matrix, k=1)

        # Indeksy najbardziej skorelowanych cech
        indexes = numpy.unravel_index(
            triangular_matrix.argmax(), triangular_matrix.shape)

        print(OutputHelper.get_correlation_output(
            collection_column_name[indexes[0]], collection_column_name[indexes[1]], triangular_matrix[indexes[0]][indexes[1]]))

        PlotHelper.plot(collection=collection,
                        collection_column_name=collection_column_name, indexes=indexes)


Main.first_step()
print("\n\n")
Main.second_step()
