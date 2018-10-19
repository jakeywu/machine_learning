# coding:utf8

import numpy as np
from collections import Counter
from math import log


def example_data_set():
    """
    年龄： 0代表青年 1代表中年 2代表老年
    是否有工作： 0代表否 1代表是
    信贷情况： 0代表一般 1代表好 2代表非常好
    类别(是否给贷款): no代表否　yes代表是
    """
    input_x = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 1, 1, 1, 1],
        [1, 0, 1, 2, 1],
        [1, 0, 1, 2, 1],
        [2, 0, 1, 2, 1],
        [2, 0, 1, 1, 1],
        [2, 1, 0, 1, 1],
        [2, 1, 0, 2, 1],
        [2, 0, 0, 0, 0]
    ]
    title = ['年龄', '有工作', '有自己的房子', '信贷情况']
    return np.array(input_x), title


def calculate_shannon_entropy(data_set):
    """
    计算信息熵
    """
    total_count = data_set.shape[0]
    shannon_entropy = 0.
    for key, v in Counter(data_set[:, -1]).items():
        prob = v/total_count
        print("类别{}的信息量为{}".format(key, -log(prob, 2)))
        shannon_entropy += -prob*log(prob, 2)
    return shannon_entropy


if __name__ == '__main__':
    x, y = example_data_set()
    print(calculate_shannon_entropy(x))
