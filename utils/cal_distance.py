import numpy as np


class Distance(object):
    # 二维平面上的点的距离算法
    def __init__(self, x1, x2):
        self.X1 = x1
        self.X2 = x2
        if isinstance(self.X1, list):
            self.X1 = np.array(self.X1)
        if isinstance(self.X2, list):
            self.X2 = np.array(self.X2)
        assert isinstance(self.X1, np.ndarray)
        assert isinstance(self.X2, np.ndarray)

    def euclidean_distance(self):
        """欧式距离"""
        # 也可以 np.linalg.norm(dim_x1 - dim_x2)  二范数, 就是欧式距离
        return np.sqrt(np.sum(np.square(self.X1 - self.X2)))

    def manhattan_distance(self):
        """曼哈顿距离"""
        return np.sum(np.abs(self.X1 - self.X2))


if __name__ == "__main__":
    dim_x1 = np.array([27, 3, 17])
    dim_x2 = np.array([2, 3, 55])
    dis = Distance(dim_x1, dim_x2)
    print("欧式距离为{}".format(dis.euclidean_distance()))
