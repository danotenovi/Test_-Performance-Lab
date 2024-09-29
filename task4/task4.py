class QuickSelect:
    def __init__(self, nums):
        self.nums = nums

    def solve(self, start, end, k):
        pivot_position = self.pivot_position_solver(start, end)
        if pivot_position < k - 1:
            return self.solve(pivot_position + 1, end, k)
        elif pivot_position == k - 1:
            return self.nums[pivot_position]
        else:
            return self.solve(start, pivot_position - 1, k)

    def pivot_position_solver(self, left, right):
        pivot = self.nums[right]
        pivot_position = left

        for i in range(left, right + 1):
            if self.nums[i] < pivot:
                self.nums[i], self.nums[pivot_position] = self.nums[pivot_position], self.nums[i]
                pivot_position += 1

        self.nums[right], self.nums[pivot_position] = self.nums[pivot_position], self.nums[right]
        return pivot_position


def ans(nums, median):
    return sum(abs(num - median) for num in nums)


def main():
    try:
        with open('numbers.txt', 'r') as file:
            nums = [int(line.strip()) for line in file.readlines()]

        quick_select = QuickSelect(nums)
        median = quick_select.solve(0, len(nums) - 1, (len(nums) + 1) // 2)
        result = ans(nums, median)
        print(result)

    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


if __name__ == "__main__":
    main()
