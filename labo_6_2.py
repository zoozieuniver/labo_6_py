n = int(input("Введіть кількість рядків: "))
m = int(input("Введіть кількість стовпців: "))

matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(int(input(f"Елемент [{i}][{j}]: ")))
    matrix.append(row)

history = []
history.append([r[:] for r in matrix]) # Додаємо копію першого покоління

while True:
    # Робимо чернетку для нового покоління
    next_gen = [[0 for _ in range(m)] for _ in range(n)]

    # Проходимо по кожній клітинці поля
    for i in range(n):
        for j in range(m):
            # Рахуємо сусідів
            neighbors = 0
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == 0 and dj == 0: continue
                    
                    ni = (i + di) % n
                    nj = (j + dj) % m
                    if matrix[ni][nj] == 1:
                        neighbors += 1

            # Твоя логіка правил (if-if)
            if matrix[i][j] == 1:
                if 2 <= neighbors <= 3:
                    next_gen[i][j] = 1
                else:
                    next_gen[i][j] = 0
            else:
                if neighbors == 3:
                    next_gen[i][j] = 1
                else:
                    next_gen[i][j] = 0

    # 3. Перевірка історії
    k = -1
    for idx in range(len(history)):
        if history[idx] == next_gen:
            k = idx
            break

    if k != -1:
        # Твій фінальний висновок
        if len(history) - k >= 1:
            print("У вас петля почалася на", k, "кроці з періодичністю", len(history) - k, "поколінь")
        else:
            print("Ваші дані дійшли кінця на", len(history), "кроці")
        break
    else:
        # Оновлюємо все для наступного кроку
        history.append([r[:] for r in next_gen])
        matrix = [r[:] for r in next_gen]