class OperationsWithMatrix:
    def sum(self, A, B):
        C = []
        for i in range(len(A)):
            rows_C = []
            for j in range(len(A[0])):
                rows_C.append(float(A[i][j]) + float(B[i][j]))
            C.append(rows_C)
        return C

    def spacial_calculation(self, C):
        res = 0.0
        for i in range(len(C)):
            if i%2 != 0:
                res += max(C[i])
            else:
                res += min(C[i])
        return res

    def print_results(self, C, res):
        print("C = A + B")
        for row in C:
            print(["{:.1f}".format(val) for val in row])

        print("\nСума найбільших елементів в рядках матриці з непарними номерами та найменших елементів в рядках матриці з парними номерами")
        print(f"{res:.1f}")

    def matrix(self):
        try:
            A = [
                [1.5, 4.5, 5.8],
                [0.4, 5.2, 1.0],
                [4.5, 8.8, 0.1]
            ]
            B = [
                [0.5, 1.8, 2.2],
                [1.9, 2.5, 3.0],
                [2.8, 1.1, 0.9]
            ]

            for matrix_name, current_matrix in [("A", A), ("B", B)]:
                for i in range(len(current_matrix)):
                    for j in range(len(current_matrix[i])):
                        if type(current_matrix[i][j]) is not float:
                            raise TypeError(f"У матриці {matrix_name} елемент [{i}][{j}] не типу float")

            if not A or not B or not A[0] or not B[0]:
                raise ValueError("Матриці не можуть бути порожні")

            rows_A, cols_A = len(A), len(A[0])
            rows_B, cols_B = len(B), len(B[0])

            if rows_A != rows_B or cols_A != cols_B:
                raise ValueError("Для додавання матриці мають бути однакової розмірності")

            C = self.sum(A, B)
            res = self.spacial_calculation(C)
            self.print_results(C, res)

        except ValueError as ve:
            print(f"Помилка значень {ve}")
        except TypeError as te:
            print(f"Помилка типу даних {te}")
        except Exception as e:
            print(f"Непередбачена помилка {e}")

if __name__ == "__main__":
    test = OperationsWithMatrix()
    test.matrix()
