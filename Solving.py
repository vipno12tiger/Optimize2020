from pulp import *

from LastOptimize.Ordering import *

"""Chia ra các loại xe để chở hàng"""
def divideCar(Bigbag):
    """Danh sách các mặt hàng
    và khối lượng của từng loại hàng"""
    Merchans = []
    Mass = {}
    Size = {}
    Slot = {}
    for b in Bigbag:
        name = b.getName()
        Merchans.append(name)
        mass = b.getMass()
        Mass.__setitem__(name, mass)
        size = b.getSize()
        Size.__setitem__(name, size)
        slot = b.getNumber()
        Slot.__setitem__(name, slot)
        # print(type(b.getId()))

    # print(Merchans)
    # print(Mass)
    # print(Size)
    # print(Slot)

    Cars = []
    while isEmpty(Slot) == False:
        """Giải bài toán với số lượng k1, k2, k3 của từng loại có trong slots"""
        # Tạo bài toán max
        prob = LpProblem("Bài toán cái túi", LpMaximize)
        # Khai báo các biến của bài toán tối ưu
        vars = LpVariable.dicts("Merchans", Merchans,0,9999, LpInteger)
        # Khai báo bài toán cụ thể
        prob += lpSum(vars[i] for i in Merchans), "Tổng số lượng có thể mang"
        # Khai báo các điều kiện của bài toán
        prob += lpSum(Mass[i] * vars[i] for i in Merchans) <= 2.5, "Tổng khối lượng tối đa"
        prob += lpSum(Size[i] * vars[i] for i in Merchans) <= 10.5, "Kích thước tối đa của xe"
        """ Số lượng tối đa của từng mặt hàng """
        for mer in Merchans:
            prob += lpSum(vars[mer]) <= Slot[mer]

        prob.solve()

        # print("status:", LpStatus[prob.status])
        car = {}
        var = prob.variables()
        i = 0
        for sl in Slot:
            val = Slot.__getitem__(sl) - var[i].varValue
            Slot.__setitem__(sl, val)
            car.__setitem__(sl, var[i].varValue)
            i += 1
        Cars.append(car)

    # print(Slot)
    # print(Cars)
    return Cars


""" Kiểm tra xem cái túi to (tổng đơn hàng) có rỗng hay không"""
def isEmpty(slots):
    # slots = {"a": 1, "b": 2, "c":3}
    for slot in slots:
        if slots.__getitem__(slot) != 0:
            return False
    return True




#Test
# print(isEmpty({'Bánh gấu': 0, 'Chip Chip': 0 , 'Chuppa Chups': 0}))

# orders = Order("D:\\Giao trinh + Bai tap\\2019-2020\\2019.2\\PythonProject\\LastOptimize\\Ordering.txt")
# BigBag = getBigBag(orders)
# print(divideCar(BigBag))

# slot = {'Bánh gấu': 7, 'Chip Chip': 9 , 'Chuppa Chups': 13}
# slot.__setitem__('Bánh gấu', 5)
# print(slot)


