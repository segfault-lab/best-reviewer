from abc import ABC, abstractmethod
import random

class Sort(ABC):
    @abstractmethod
    def sort(self, data: list[int]) -> list[int]:
        pass

class BubbleSort(Sort):
    def sort(self, data: list[int]) -> list[int]:
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

class SelectionSort(Sort):
    def sort(self, data: list[int]) -> list[int]:
        n = len(data)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if data[j] < data[min_idx]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
        return data

class QuickSort(Sort):
    def sort(self, data: list[int]) -> list[int]:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)

class MergeSort(Sort):
    def sort(self, data: list[int]) -> list[int]:
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])
        return self._merge(left, right)

    def _merge(self, left: list[int], right: list[int]) -> list[int]:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

class SortPrinter:
    def __init__(self):
        self._algorithm: Sort = None
        self._data = []
        self._is_sorted = False

    def insert(self, value: int):
        self._data.append(value)
        self._is_sorted = False

    def selection(self, algorithm: Sort):
        self._algorithm = algorithm

    def run(self):
        if not self._algorithm:
            raise ValueError("No sorting algorithm selected")
        self._data = self._algorithm.sort(self._data)
        self._is_sorted = True

    def show(self):
        if self._algorithm:
            print(self._algorithm.__class__.__name__)
        if not self._is_sorted:
            print(f"Before: {self._data}")
        else:
            print(f"After : {self._data}")

    def empty(self):
        self._data.clear()
        self._algorithm = None
        self._is_sorted = False

if __name__ == "__main__":
    random.seed(1)
    arr = [random.randint(1, 100) for _ in range(10)]
    sort_printer = SortPrinter()
    for algo in [BubbleSort, SelectionSort, QuickSort, MergeSort]:
        sort_printer.empty()
        for value in arr:
            sort_printer.insert(value)
        sort_printer.selection(algo())
        sort_printer.show()
        sort_printer.run()
        sort_printer.show()