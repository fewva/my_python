a = [2, 4, 9, 16, 25]
b = [i ** (1/2) for i in a]
def f(x):
    return x ** (1/2)
c = list(map(f,a))
d = []
for i in a:
    d.append(i ** (1/2))

'''Напишите программный код, который будет создавать новый список, содержащий в качестве элементов квадратные корни всех чисел из
 списка [2, 4, 9, 16, 25]:


1) на основе цикла for
2) на основе функции map
3) в виде генератора списка
'''