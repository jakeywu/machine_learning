from utils.cal_distance import Distance


class KNN(object):
    def __init__(self, train_data, test_data):
        self.trainData = train_data
        self.testData = test_data
        self.eachDistance = self.__cal_distance()

    def __cal_distance(self):
        knn_distance = dict()
        for k, v in self.trainData.items():
            dis = Distance([v[0], v[1], v[2]], [self.testData[0], self.testData[1], self.testData[2]])
            knn_distance[k] = round(dis.euclidean_distance(), 3)
        return sorted(knn_distance.items(), key=lambda x: x[1], reverse=False)

    def predict(self, k):
        assert isinstance(k, int)
        res = dict()
        for dis in self.eachDistance[:k]:
            category = self.trainData[dis[0]][3]
            if category in res.keys():
                res[category] += 1
            else:
                res[category] = 1
        return sorted(res.items(), key=lambda x: x[1], reverse=True)[0][0]


if __name__ == "__main__":
    movie_data = {
        "宝贝当家": [45, 2, 9, "喜剧片"],
        "美人鱼": [21, 17, 5, "喜剧片"],
        "澳门风云3": [54, 9, 11, "喜剧片"],
        "功夫熊猫3": [39, 0, 31, "喜剧片"],
        "谍影重重": [5, 2, 57, "动作片"],
        "叶问3": [3, 2, 65, "动作片"],
        "伦敦陷落": [2, 3, 55, "动作片"],
        "我的特工爷爷": [6, 4, 21, "动作片"],
        "奔爱": [7, 46, 4, "爱情片"],
        "夜孔雀": [9, 39, 8, "爱情片"],
        "代理情人": [9, 38, 2, "爱情片"],
        "新步步惊心": [8, 34, 17, "爱情片"]
    }  # 分别代表搞笑镜头/亲吻镜头/打斗镜头
    predict_data = [23, 3, 17, "？片"]  # 唐人街探案
    knn = KNN(movie_data, predict_data)
    print("预测电影[唐人街侦探]主题类型为{}".format(knn.predict(5)))
