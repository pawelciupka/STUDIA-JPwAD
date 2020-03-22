import matplotlib.pyplot as plot


class PlotHelper(object):

    @staticmethod
    def plot(collection, collection_column_name, indexes):

        plot.hist(collection[collection_column_name[indexes[0]]], bins=20,
                  alpha=0.5, label=collection[collection_column_name[indexes[0]]])
        plot.title(collection_column_name[indexes[0]])
        plot.xlabel("CECHA")
        plot.ylabel("OSOBA")
        plot.show()

        plot.hist(collection[collection_column_name[indexes[1]]], bins=20,
                  alpha=0.5, label=collection[collection_column_name[indexes[1]]])
        plot.title(collection_column_name[indexes[1]])
        plot.xlabel("CECHA")
        plot.ylabel("OSOBA")
        plot.show()
