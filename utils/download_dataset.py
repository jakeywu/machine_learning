import os
import sys
from urllib import request
DataPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
if not os.path.isdir(DataPath):
    os.makedirs(DataPath)


class DownloadDataSet(object):
    def __init__(self):
        self.irisPath = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

    @staticmethod
    def _progress(block_num, block_size, total_size):
        """回调函数
        @block_num: 已经下载的数据块
        @block_size: 数据块的大小
        @total_size: 远程文件的大小
        """
        percent = min(block_num * block_size / total_size * 100.0, 100.0)
        sys.stdout.write('\r>> Downloading %.1f%%' % percent)
        sys.stdout.flush()

    def download_iris(self):
        local_path = os.path.join(DataPath, os.path.basename(self.irisPath))
        if os.path.isfile(local_path):
            return local_path
        try:
            request.urlretrieve(self.irisPath, local_path, self._progress)
        except Exception as e:
            raise Exception(e)
        return local_path


if __name__ == "__main__":
    dds = DownloadDataSet()
    dds.download_iris()
