# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

list1 = [9, 12, 3, 2, 44, 5, 0, 10, 1, 32]
print('list1:', list1)
list2 = list(map(lambda x:x**2, list1))
print('list2:', list2)

# Результат
# list1: [9, 12, 3, 2, 44, 5, 0, 10, 1, 32]
# list2: [81, 144, 9, 4, 1936, 25, 0, 100, 1, 1024]


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit_list1 = ['Ананас', 'Груша', 'Киви', 'Дыня', 'Маракуйя', 'Мандарин', 'Абрикос', 'Гранат']
fruit_list2 = ['Гранат', 'Манго', 'Грейпфрут', 'Ананас', 'Банан', 'Маракуйя', 'Апельсин', 'Дыня']
result_list = [i for i in fruit_list1 if i in fruit_list2]
print(result_list)

# Результат
['Ананас', 'Дыня', 'Маракуйя', 'Гранат']


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

list1 = [8, -9, 3, -8, -22, 14, 23, 46, 6, 14, -3, 99, 44, 71]
list2 = [i for i in list1 if  i >= 0 and i%4 and not i%3]
print(list2)

# Результат
[3, 6, 99]