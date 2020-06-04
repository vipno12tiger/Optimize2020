"""
Từ đồ thị ban đầu, ta có 1 file ma trận kề
File này dùng để import ma trận đó vào mảng 2 chiều, có sử dụng numpy.
Sau đó sẽ tìm đường đi ngắn nhất giữa 2 điểm bất kỳ trên đồ thị.
"""

import numpy as np


# hàm này dùng để chuyển đổi kiểu dữ liệu string của mảng -> int
def transformData(array):
    res = []
    for a in array:
        r = (int)(a)
        res.append(r)
    return res


"""hàm này dùng để đọc dữ liệu của ma trận kề từ fileName.
Kết quả trả về của hàm này là 1 ma trận đối xứng cỡ (n x n) sau khi dùng numpy"""
def import_core_graph(fileName):
    # mở file chứa dữ liệu của ma trận kề và đọc
    with open(fileName, "r", encoding= 'utf8') as f:
        datas = f.read().split("\n")
    # print(datas)

    # xử lý dữ liệu bên trên để có thể đưa vào mảng numpy 2 chiều
    pre_res = []
    for data in datas:
        r = data.split(", ")
        r = transformData(r)
        pre_res.append(r)
    res = np.array(pre_res)
    return res


"""hàm này trả về kết quả là 1 ma trận với khoảng cách ngắn nhất giữa 2 đỉnh bất kỳ
 sử dụng thuật toán floyd"""
def findMinSpaceMatrix(matrix):
    n=len(matrix)   #chiều dài matrix
    """Ma trận D lưu đường đi
        D[i][j] là đỉnh kề với đỉnh i trên đường đi ngắn nhất từ i đến j"""
    D = np.zeros((n,n))
    # print(D)

    # chuẩn hoá matrix đưa vào, giữa 2 điểm i khác j, nếu không tồn tại đường đi thì gán giá trị là 999999
    for i in range(n):
        for j in range(n):
            if(i!=j and matrix[i][j]==0):
                matrix[i][j] = 999999
            if(matrix[i][j] != 0):
                D[i][j] = j

    # print(matrix)
    # print(D)

    # duyệt qua tất cả các cặp điểm (k,i,j) với k là điểm trung gian :> ez
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] > matrix[i][k] + matrix[j][k]:
                    matrix[i][j] = matrix[i][k] + matrix[j][k]
                    D[i][j] = D[i][k]

    # print(D)
    return [matrix, D]


"""truy vết lưu lại đường đi ngắn nhất giữa 2 đỉnh u,v"""
def findMinRoad(matrix,u ,v):
    flag = int(matrix[u][v])
    flag = int(flag)
    if flag == 0: return 0
    else:
        res = str(u)
        while flag != 0:
            res = res + "_" +str(flag)
            flag = int(matrix[int(flag)][v])
        res = str(res)
        return res

"""Ma trận lưu vết đường đi ngắn nhất giữa các điểm"""
def minRoadMatrix(matrix):
    n = len(matrix)
    pre_res = []

    for i in range(n):
        a = []
        for j in range(n):
            r = findMinRoad(matrix,i,j)
            a.append(r)
        pre_res.append(a)
    res = np.array(pre_res)
    return res

# test
# res = import_core_graph("D:\\Giao trinh + Bai tap\\2019-2020\\2019.2\\PythonProject\\LastOptimize\\graph.txt")
# # print(res)
# test = findMinSpaceMatrix(res)
# # print(test[1])
# minroad = test[1]
# # print(type(findMinRoad(minroad, 6 ,1)))
# a = minRoadMatrix(minroad)
# print(a)
