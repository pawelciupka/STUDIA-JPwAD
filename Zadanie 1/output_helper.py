from calc_helper import CalcHelper


class OutputHelper(object):

    @staticmethod
    def get_median_output(collection):
        result = "Mediana dla cech ilościowych wynosi = " + \
            str(CalcHelper.calculate_median(collection))
        return result

    @staticmethod
    def get_minimum_output(collection):
        result = "Minimalna wartość dla cech ilościowych wynosi = " + \
            str(CalcHelper.calculate_minimum(collection))
        return result

    @staticmethod
    def get_maximum_output(collection):
        result = "Maksymalna wartość dla cech ilościowych wynosi = " + \
            str(CalcHelper.calculate_maximum(collection))
        return result

    @staticmethod
    def get_dominant_output(collection):
        result = "Dominanta dla cech jakościowych wynosi = " + \
            str(CalcHelper.calculate_dominant(collection))
        return result

    @staticmethod
    def get_correlation_output(feature1, feature2, correlation_coefficient):
        result = "Skorelowane cechy: \n1. " + str(feature1) + "\n2. " + str(
            feature2) + "\n\nWspółczynnik korelacji: \n" + str(correlation_coefficient)
        return result
