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
        shannon_entropy += -prob*log(prob, 2)
    return shannon_entropy


def choose_best_feature(data_set, label):
    """
    通过信息增益选择最优特征
    """
    features_num = data_set.shape[1] - 1
    base_shannon_entropy = calculate_shannon_entropy(data_set)
    print("数据集整体经验熵为%.3f\n" % base_shannon_entropy)
    for i in range(features_num):
        values = list(set(data_set[:, i]))
        entropy = 0.
        for j in values:
            sub_set = data_set[data_set[:, i] == j]  # 获取子集
            sub_shannon = calculate_shannon_entropy(sub_set)  # 子集条件熵
            prob = sub_set.shape[0] / data_set.shape[0]
            entropy += prob * sub_shannon
        print("[%s]信息增益为%.3f" % (label[i], base_shannon_entropy - entropy))


def create_decision_tree():
    """
    构造决策树
    """
    pass


if __name__ == '__main__':
    x, y = example_data_set()
    choose_best_feature(x, y)
