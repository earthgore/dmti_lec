from random import randint
import math
def gen(p, b):
    #p - вероятность
    #b - размер выборки
    if randint(0, b) < p*b:
        return 0
    else:
        return 1

game = [[2, -3], [-1, 2]]
#1
arr_vec1 = []

for i in range(100):
    arr_vec1.append((gen(0.5, 100), gen(0.5, 100)))
sum1 = 0
sd1 = 0 #СКО среднего
for i in arr_vec1:
    sum1 += game[i[0]][i[1]]
aver1 = sum1/100 #Среднее значение выгрыша/проигрыша игрока А
for i in arr_vec1:
    sd1 += (game[i[0]][i[1]] - aver1)**2
sd1 = math.sqrt(sd1/100)

#2
arr_vec2 = []

for i in range(100):
    arr_vec2.append((gen(0.5, 100), gen(0.25, 100)))
sum2 = 0
sd2 = 0 #СКО среднего
for i in arr_vec2:
    sum2 += game[i[0]][i[1]]
aver2 = sum2/100 #Среднее значение выгрыша/проигрыша игрока А
for i in arr_vec2:
    sd2 += (game[i[0]][i[1]] - aver2)**2
sd2 = math.sqrt(sd2/100)
#3
p = 0.5
q = 0.5
b = 100
arr_vec3 = []

for i in range(100):
    x = gen(p, b)
    y = gen(q, 100)
    if x == y:
        if x == 0:
            p += 10.0/b
        else:
            p -= 10.0/b
        b += 10
    if p < 0:
        p = 0
    elif p > 1:
        p = 1
for i in range(100):
    arr_vec3.append((gen(p, 100), gen(q, 100)))
sum3 = 0
sd3 = 0 #СКО среднего
for i in arr_vec3:
    sum3 += game[i[0]][i[1]]
aver3 = sum3/100 #Среднее значение выгрыша/проигрыша игрока А
for i in arr_vec3:
    sd3 += (game[i[0]][i[1]] - aver3)**2
sd3 = math.sqrt(sd3/100)
#4
p1 = 0.5
q = 0.5
b = 1000
arr_vec4 = []

for i in range(100):
    x = gen(p1, b)
    y = gen(q, 100)
    if x != y:
        if x == 0:
            p1 -= (game[x][y])*5.0/b
        else:
            p1 += (game[x][y])*5.0/b
        if b != 5:
            b -= 5
    if p1 < 0:
        p1 = 0
    elif p1 > 1:
        p1 = 1
for i in range(100):
    arr_vec4.append((gen(p1, 100), gen(q, 100)))
sum4 = 0
sd4 = 0 #СКО среднего
for i in arr_vec4:
    sum4 += game[i[0]][i[1]]
aver4 = sum4/100 #Среднее значение выгрыша/проигрыша игрока А
for i in arr_vec4:
    sd4 += (game[i[0]][i[1]] - aver4)**2
sd4 = math.sqrt(sd4/100)
#5
p2 = 0.5
q1 = 0.5
b = 100
arr_vec5 = []

for i in range(100):
    x = gen(p2, b)
    y = gen(q1, b)
    if x == y:
        if x == 0:
            p2 += (game[x][y])*5.0/b
        else:
            p2 -= (game[x][y])*5.0/b
        b += (game[x][y])*5
    else:
        if y == 0:
            q1 -= (game[x][y])*5.0/b
        else:
            q1 += (game[x][y])*5.0/b
        b += (-game[x][y])*5
    if p2 < 0:
        p2 = 0
    elif p2 > 1:
        p2 = 1
    if q1 < 0:
        q1 = 0
    elif q1 > 1:
        q1 = 1
for i in range(100):
    arr_vec5.append((gen(p2, 100), gen(q1, 100)))
sum5 = 0
sd5 = 0 #СКО среднего
for i in arr_vec5:
    sum5 += game[i[0]][i[1]]
aver5 = sum5/100 #Среднее значение выгрыша/проигрыша игрока А
for i in arr_vec5:
    sd5 += (game[i[0]][i[1]] - aver4)**2
sd5 = math.sqrt(sd5/100)
print("С вероятностями 0.5 и 0.5")
print("Исход 100 игр:", sum1)
print("Среднее значение выгрыша/проигрыша игрока А:", aver1)
print("СКО:", sd1)
print("С вероятностями 0.5 и 0.25")
print("Исход 100 игр:", sum2)
print("Среднее значение выгрыша/проигрыша игрока А:", aver2)
print("СКО:", sd2)
print("С подкреплением")
print("Вероятность А1:", p)
print("Исход 100 игр:", sum3)
print("Среднее значение выгрыша/проигрыша игрока А:", aver3)
print("СКО:", sd3)
print("С наказанием")
print("Вероятность А1:", p1)
print("Исход 100 игр:", sum4)
print("Среднее значение выгрыша/проигрыша игрока А:", aver4)
print("СКО:", sd4)
print("С подкреплением для двоих")
print("Вероятность А1:", p2)
print("Вероятность В1:", q1)
print("Исход 100 игр:", sum5)
print("Среднее значение выгрыша/проигрыша игрока А:", aver5)
print("СКО:", sd5)