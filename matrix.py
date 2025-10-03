class Matrix:
    def __init__(self,n):
        self.size = n
        self.matrix = None

    def build_matrix(self):
        matrix=[]
        for i in range(self.size):
            matrix.append(list(map(int,input().split())))
        self.matrix = matrix
        return matrix

    def convert_minor(self,arr,j,i):
        return [row[:i]+row[i+1:]for row in (arr[:j] + arr[j+1:])]

    def find_det(self,arr):
        if len(arr) ==1:
            print('hi',arr[0][0])
            return arr[0][0]
        if len(arr) == 2:
            return arr[0][0]*arr[1][1] - arr[1][0]*arr[0][1]
        det = 0
        for i in range(len(arr)):
            det += (-1) ** i * arr[0][i] * self.find_det(self.convert_minor(arr,0,i))
        return det

    def transpose_matrix(self,arr):
        ret = []
        for i in range(len(arr)):
            arg = []
            for j in range(len(arr)):
                arg.append(arr[j][i])
            ret.append(arg)
        return ret

    def det_inverse(self,arr):
        det = self.find_det(arr)
        if det ==0:
            print("역행렬이 존재하지 않습니다.")
            return
        if len(arr)==1:
            return [[det**(-1)]]
        ret = []
        for i in range(len(arr)):
            val = []
            for j in range(len(arr)):
                val.append((-1)** (i+j) *self.find_det(self.convert_minor(arr,i,j))/det)
            ret.append(val)
        return self.rounded(self.transpose_matrix(ret))

    def gauss_jordan(self, arr):
        arg = []
        n = len(arr)
        for i in range(n):
            a1 = [0.0] * n
            a1[i] = 1.0
            arg.append([float(x) for x in arr[i]] + a1)
        for k in range(n):
            now_row = k
            max = arg[k][k]
            for i in range(k,n):
                if abs(max) <abs(arg[i][k]):
                    max = arg[i][k]
                    now_row = i
            if now_row != k :
                arg[k], arg[now_row] = arg[now_row], arg[k]
            if abs(max) <1e-9:
                print("역행렬이 존재하지 않습니다.")
                return
            for i in range(n*2):
                arg[k][i] /= max
            for i in range(n):
                if i == k:
                    continue
                t = arg[i][k]
                for j in range(n*2):
                    arg[i][j] -= t*arg[k][j]
        return self.rounded([row[n:] for row in arg])

    def rounded(self,arr):
        return [[round(x,2) for x in row]for row in arr]

    def matrixout(self,arr):
        size = len(arr)
        print("┌" + "       " * size + "┐")
        for i in range(size):
            print("│", end="")
            for j in range(size):
                print("%7.2f" % arr[i][j], end="")
            print("│")
        print("└" + "       " * size + "┘")

    def compare_matrix(self,arr1,arr2):
        if arr1==arr2:
            return "두 결과가 동일합니다."
        else:
            return "두 결과는 다릅니다."
if __name__ == "__main__":
    n = int(input())
    m1 = Matrix(n)
    arr = m1.build_matrix()
    a1 = m1.det_inverse(arr)
    if a1:
        print("행렬식을 이용한 역행렬")
        m1.matrixout(a1)
    a2 = m1.gauss_jordan(arr)
    if a2:
        print("gauss-jordan을 이용한 역행렬")
        m1.matrixout(a2)
    print(m1.compare_matrix(a1,a2))