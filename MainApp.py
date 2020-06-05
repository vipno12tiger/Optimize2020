from LastOptimize.transformGraph import *
from LastOptimize.Ordering import *
from LastOptimize.Solving import *

"""Kiểm tra xem mặt hàng merchan_name có CÒN ở trong car hay không?"""
def isContain(merchan_name, car):
    flag = True
    if merchan_name == 'null': flag = False
    else:
        if car.get(merchan_name) == 0:
            flag = False
    return flag


"""Tìm điểm đến ngắn nhất tiếp theo 
(điểm này có giá trị khác 0 và 
không có trong min_index_array(chứa danh sách các điểm ngắn nhất không thoả mãn 1 điều kiện nào đó)"""
def findNextIndex(array, min_index_array):
    min_index = -1
    min = 999999
    for i in range(len(array)):
        if min > array[i] and array[i] != 0 and i not in min_index_array:
            min = array[i]
            min_index = i
    return min_index


"""Tìm đường đi cho 1 xe"""
def solutionForACar(MinSpaceMatrix, MinRoadMatrix , merchanAddress, car):
    res = ''        # Lưu vết đường cần đi
    line = 0        # Điểm đến tiếp theo
    total_space = 0 # Tổng quãng đường mà 1 xe phải đi

    while isEmpty(car) == False:
        line_road = MinSpaceMatrix[line]        # Khoảng cách ngắn nhất từ điểm (line) đến các điểm khác
        # print(line_road)
        backtrack_road = MinRoadMatrix[line]    # Đường đi ngắn nhất từ điểm (line) đến các điểm khác
        # print(backtrack_road)
        min_index_array = []                    # Mảng chứa index các phần tử có giá trị bé nhất nhưng không thoả mãn điều kiện
        merchan_name = 'null'                   # Tên của sản phẩm ở địa chỉ. Nếu địa chỉ không đặt hàng thì tên='null'

        # TÌm chỉ số đường đi ngắn nhất thoả mãn điều kiện:
        # Tại điểm đang xét, mặt hàng ở đó phải có ở trong car
        while isContain(merchan_name, car) == False:
            min_index = findNextIndex(line_road, min_index_array)
            merchan_name = merchanAddress[min_index]
            min_index_array.append(min_index)

        total_space += line_road[min_index]
        car.__setitem__(merchan_name, car.get(merchan_name)-1)
        # print(car)
        merchanAddress[min_index] = 'null'      #Sau khi giao hàng xong tại địa điểm phù hợp thì cập nhật lại tên hàng tại địa chỉ đó
        if len(res) == 0:
            res = backtrack_road[min_index]
        else:
            res = res + "; " + backtrack_road[min_index]

        flag_backtrack_road = backtrack_road[min_index].split('_')
        for fbr in flag_backtrack_road:
            flag_merchan = merchanAddress[int(fbr)]
            if isContain(flag_merchan, car) == True:
                car.__setitem__(flag_merchan, car.get(flag_merchan)-1)
                merchanAddress[int(fbr)] = 'null'

        line = min_index
        # print(line)

    # print(res)
    # print(total_space)
    return [res, total_space]


def FinalSolution(MinSpaceMatrix, MinRoadMatrix , merchanAddress, cars):
    for car in cars:
        print(car, end='')
        pre_res = solutionForACar(MinSpaceMatrix, MinRoadMatrix , merchanAddress, car)
        road = pre_res[0]
        total_space = pre_res[1]
        print(': Road =', road, ' &  Total_space =', total_space)


def main():
    Core_graph = import_core_graph("D:\\Giao trinh + Bai tap\\2019-2020\\2019.2\\PythonProject\\LastOptimize\\graph.txt")
    Ordering_Matrix = Order("D:\\Giao trinh + Bai tap\\2019-2020\\2019.2\\PythonProject\\LastOptimize\\Ordering.txt")

    pre_MinSpaceMatrix = findMinSpaceMatrix(Core_graph)
    MinSpaceMatrix = pre_MinSpaceMatrix[1]
    MinRoadMatrix = minRoadMatrix(MinSpaceMatrix)
    merchanAddress = getMerchanAddress(Ordering_Matrix)
    cars = divideCar(getBigBag(Ordering_Matrix))

    FinalSolution(MinSpaceMatrix,MinRoadMatrix,merchanAddress,cars)

main()