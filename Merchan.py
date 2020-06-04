"""
File này chứa đối tượng là mặt hàng
"""

class Merchan:
    """ Hàm dựng đối tượng"""
    def __init__(self, id, number, size=0 , mass=0):
        self.id = id            # Mã sản phẩm
        self.size = size        # Kích thước sản phẩm
        self.mass = mass        # Khối lượng sản phẩm
        self.number = number    # Số lượng được đặt

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    """ Trả về tên của sản phẩm """
    def getName(self):
        mer = ''
        flag = self.id
        if flag == 1:
            mer = "Bánh gấu"
        if flag == 2:
            mer = "Chip Chip"
        if flag == 3:
            mer = "Chuppa Chups"
        return mer

    """ Trả về khối lượng của sản phẩm"""
    def getMass(self):
        flag = self.id
        if flag == 1:
            w = 0.5
        if flag == 2:
            w = 0.25
        if flag == 3:
            w = 0.15
        return w

    def setMass(self,mass):
        self.mass = mass

    """ Trả về kích thước của sản phẩm """
    def getSize(self):
        flag = self.id
        if flag == 1:
            s = 1.0
        if flag == 2:
            s = 1.5
        if flag == 3:
            s = 1.8
        return s

    def setSize(self, size):
        self.size = size


    def getNumber(self):
        return self.number

    def setNumber(self, number):
        self.number = number

    def toString(self):
        mer = ''
        flag = self.id
        if flag == 1:
            mer = "Bánh gấu"
        if flag == 2:
            mer = "Chip Chip"
        if flag == 3:
            mer = "Chuppa Chups"

        return "[ Name= " + mer + "; Mass= " + (str)(self.mass) + "; Size= " + str(self.size) +"; Number= " + (str)(self.number) + " ]"