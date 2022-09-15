# 2.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = [0, 1]
y = [0, 1]
z = [0, 1]
for i in range(2):
    for j in range(2):
        for k in range(2):
            left = not (x[i] or y[j] or z[k])
            right = not x[i] and not y[j] and not z[k]
            if left == right:
                print(f'При x = {x[i]}, y = {y[j]}, z = {z[k]} утверждение истинно')
            else:
                print(f'При x = {x[i]}, y = {y[j]}, z = {z[k]} утверждение ложно')


