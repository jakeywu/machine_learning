import pandas as pd
from utils.download_dataset import DownloadDataSet

DDS = DownloadDataSet()


class LoadingDataSet(object):
    def __init__(self):
        pass

    @staticmethod
    def loading_iris():
        iris_path = DDS.download_iris()
        df = pd.read_csv(iris_path, header=None, names=["sepalLength", "sepalWidth", "petaLength", "petaWidth", "className"])
        return df


if __name__ == "__main__":
    lds = LoadingDataSet()
    lds.loading_iris()
