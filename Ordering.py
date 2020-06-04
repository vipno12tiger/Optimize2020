from LastOptimize.Customer import Customer
from LastOptimize.Merchan import Merchan


""" Hàm này trả về danh sách khách hàng đặt sản phẩm, dữ liệu được lấy từ 1 file có trước """
def Order(fileName):
    customers = []
    with open(fileName, "r", encoding='utf8') as f:
        data = f.read().split("\n")
    # print(datas)

    i = 0
    while i < len(data)-1:
        name = data[i]
        add = (int)(data[i+1])
        mer = (int)(data[i+2])
        Cus = Customer(name, add, mer)
        customers.append(Cus)
        i += 3

    return customers


"""Hàm này trả về tổng lượng hàng được đặt"""
def getBigBag(customers):
    # Danh sách hàng hoá được đặt
    Mers = []
    for cus in customers:
        mer = cus.merchan
        if mer not in Mers:
            Mers.append(mer)
    # print(Mers)

    # Tổng lượng hàng được đặt, gồm tất cả các thông tin mà đối tượng Merchan có
    BigBag = []
    for mer in Mers:
        count = 0
        for cus in customers:
            flag = (int)(cus.merchan)
            if flag == mer:
                count = count + 1
        merchan = Merchan(mer, count)
        merchan.setMass(merchan.getMass())
        merchan.setSize(merchan.getSize())
        BigBag.append(merchan)

    return BigBag


"""hàm này trả về mặt hàng tương ứng với địa chỉ (0-30)
    Nếu địa chỉ i mà không đặt hàng thì chỗ đó sẽ mặc định là null"""
def getMerchanAddress(customers):
    res = ['null' for i in range(30)]
    for bag in customers:
        flag_address = bag.getAddress()
        mer = ''
        flag_mer = bag.getMerchan()
        if flag_mer == 1:
            mer = "Bánh gấu"
        if flag_mer == 2:
            mer = "Chip Chip"
        if flag_mer == 3:
            mer = "Chuppa Chups"
        res[flag_address] = mer
    return res



# def Test():
#     test = Order("D:\\Giao trinh + Bai tap\\2019-2020\\2019.2\\PythonProject\\LastOptimize\\Ordering.txt")
# #     # for t in test:
# #     #     print(t.toString())
# #
# #     # bags = getBigBag(test)
# #     # for b in bags:
# #     #     print(b.toString())
# #
#     merchanMatrix = getMerchanAddress(test)
#     print(merchanMatrix)
# Test()