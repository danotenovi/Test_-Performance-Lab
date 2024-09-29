def main():
    # Вводные данные
    num_elements = int(input("Введите количество элементов в массиве: "))
    interval_length = int(input("Введите длину интервала:  "))

    # Создание массива с числами от 1 до num_elements
    arr = range(1, num_elements + 1)

    # Инициализация текущего индекса
    current = 0

    # Вывод пути
    print("Путь:", end = " ")
    while current < num_elements:
        print(arr[current], end = " ")
        current = (current + interval_length - 1) % num_elements
        if current == 0:
            break
    print()

if __name__ == "__main__":
    main()

