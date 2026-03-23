# 1. Введення розмірів
n = int(input("Введіть кількість рядків (N): "))
m = int(input("Введіть кількість стовпців (M): "))

# 2. Створення та заповнення початкової матриці
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        while True:
            val = int(input(f"Елемент [",i,"][",j,"] (1-жива, 0-мертва): "))
            if val == 0 or val == 1:
                row.append(val)
                break
            print("Помилка! Введіть 0 або 1.")
    matrix.append(row)

# 3. Створення історії та додавання першого стану
history = []
# Робимо глибоку копію, щоб історія не змінювалася разом з матрицею
initial_copy = [r[:] for r in matrix]
history.append(initial_copy)