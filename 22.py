# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Please enter numbers for list n: "))
m = int(input("Please enter numbers for list m: "))

list_first = set()
list_second = set()

print("Enter the elements of list_first:")
for _ in range(n):
    element = int(input())
    list_first.add(element)

print("Enter the elements of list_second:")
for _ in range(m):
    element = int(input())
    list_second.add(element)

shared_elements = list_first.intersection(list_second)

sorted_shared_elements = sorted(shared_elements)

print("Answer:")
for element in sorted_shared_elements:
    print(element)