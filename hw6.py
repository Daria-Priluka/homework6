m = int(input("Введите размер первого массива: "))
n = int(input("Введите размер второго массива: "))

array1 = []
print("Введите через пробел значения элементов первого массива:")
for i in range(0,m):
    a = float(input())
    array1.append(a)
array2 = []
print("Введите через пробел значения элементов второго массива:")
for j in range(0,n):
    b = float(input())
    array2.append(b)
def check_massiv(array1,array2):
    for i in range (0,m):
        for j in range(0,n):
            if (array1[i] == array2[j]):
                c = " "
                c = array1[i]
                print("Общие элементы для первого и второго массивов: ", c) 

check_massiv(array1,array2)
