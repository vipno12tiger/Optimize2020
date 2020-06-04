"""
File này dùng để chứa đối tượng là khách hàng
"""
class Customer:
    """ Dữ liệu của khách hàng gồm có
    Tên, địa chỉ (tương ứng với điểm trên đồ thị) và loại hàng mà người này đặt"""
    def __init__(self, name, address, merchan):
        self.name = name            # tên khách hàng
        self.address = address      # địa chỉ khách hàng
        self.merchan = merchan      # loại hàng mà khách đặt

    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setMerchan(self, merchan):
        self.merchan = merchan

    def getName(self):
        return self.name

    def getAddress(self):
        return (int)(self.address)

    def getMerchan(self):
        return self.merchan

    def toString(self):
        mer = ''
        flag = self.merchan
        if flag == 1:
            mer = "Bánh gấu"
        if flag == 2:
            mer = "Chip Chip"
        if flag == 3:
            mer = "Chuppa Chups"

        return "[ Name= " + self.name + "; Address= "+ (str)(self.address) + "; Merchan= " + mer + " ]"
