import math


def read_circle_file(file_path):
    with open(file_path, 'r') as file:
        x, y = map(float, file.readline().split())
        r = float(file.readline().strip())
    return x, y, r


def read_points_file(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.split())
            points.append((x, y))
    return points


def calculate_position(x, y, r, point):
    px, py = point
    distance = math.sqrt((px - x) ** 2 + (py - y) ** 2)
    if distance > r:
        return 2
    elif distance == r:
        return 0
    else:
        return 1


def main():
    try:
        circle_x, circle_y, circle_r = read_circle_file('file1.txt')
        points = read_points_file('file2.txt')

        for point in points:
            position = calculate_position(circle_x, circle_y, circle_r, point)
            print(position)

    except FileNotFoundError:
        print("Ошибка: Файлы 'file1.txt' или 'file2.txt' не найдены.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()



