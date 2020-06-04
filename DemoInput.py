import random
import numpy as np

def main():

    matrix = np.eye(30)
    # print(matrix)

    for i in range(30):
        for j in range(i, 30):
            if(matrix[i][j] == 1):
                matrix[i][j] = 0
            else:
                a = random.randrange(30)
                matrix[i][j] = a
                matrix[j][i] = a


    f = open("graph.txt", "w", encoding="utf8")
    for i in range(30):
        res = str(int(matrix[i][0]))
        for j in range(1,30):
            res = res + ', ' + str(int(matrix[i][j]))
        f.write(res + "\n")
    f.close()

# main()


