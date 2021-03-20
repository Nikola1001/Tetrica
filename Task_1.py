# Task 1


def task_1(array):
    try:
        return array.index(0)-1
    except Exception as ex:
        print("Этот элемент не встречается в массиве")

# Сложность О(n)