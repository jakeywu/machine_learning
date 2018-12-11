from collections import Counter
from utils.cal_distance import Distance
from utils.loading_dataset import LoadingDataSet

LDS = LoadingDataSet


class KNN(object):
    def __init__(self, train_data, test_data):
        self.trainData = train_data
        self.testData = test_data
        self.eachDistance = self.__cal_distance()

    def __cal_distance(self):
        knn_distance = dict()
        for index, row in iris_dataset.iterrows():
            x1 = [row["sepalLength"], row["sepalWidth"], row["petaLength"], row["petaWidth"]]
            dis = Distance(x1, self.testData)
            knn_distance[str(index)] = round(dis.euclidean_distance(), 3)
        return sorted(knn_distance.items(), key=lambda x: x[1], reverse=False)

    def predict(self, k):
        assert isinstance(k, int)
        res = list()
        for dis in self.eachDistance[:k]:
            column = self.trainData.loc[int(dis[0])]
            res.append(column["className"])
        return Counter(res).most_common(1)[0][0]


if __name__ == "__main__":
    iris_dataset = LDS.loading_iris()
    predict_data = [2.7, 0.1, 5.3, 4.9]
    knn = KNN(iris_dataset, predict_data)
    print("预测结果为{}".format(knn.predict(10)))
