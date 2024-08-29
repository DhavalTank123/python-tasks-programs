'''Create a python class named Algorithms. It should have following sorting algorithms:
 Quick sort
 Bubble sort
 BFS (I/P Graph)
 DFS (I/P Graph)
 Merge Sort
Create a class Sorting which should sort the list provided as input parameter using the algorithm which is also provided
as input parameter. Create a main class which inherits the Sorting class and calls sort method with list and algorithm to
use.
'''
# class algorithm:
#     def quick_sort(self):
#         pass
# if __name__ == '__main__':
#     element = [11,9,29,7,2,15,28]
#     ob=algorithm()
#     ob.quick_sort(element)
#     print(element)


class Algorithms:
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return self.merge(left, right)

    def merge(self, left, right):
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

    def bfs(self, graph, start):
        visited = set()
        queue = [start]
        result = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend(set(graph[vertex]) - visited)

        return result

    def dfs(self, graph, start):
        visited = set()
        stack = [start]
        result = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                stack.extend(set(graph[vertex]) - visited)

        return result


class Sorting:
    def __init__(self):
        self.algorithms = Algorithms()

    def sort(self, arr, algorithm):
        if algorithm == "quick_sort":
            return self.algorithms.quick_sort(arr)
        elif algorithm == "bubble_sort":
            return self.algorithms.bubble_sort(arr)
        elif algorithm == "merge_sort":
            return self.algorithms.merge_sort(arr)
        else:
            raise ValueError("Unsupported sorting algorithm")

    def graph_search(self, graph, start, algorithm):
        if algorithm == "bfs":
            return self.algorithms.bfs(graph, start)
        elif algorithm == "dfs":
            return self.algorithms.dfs(graph, start)
        else:
            raise ValueError("Unsupported graph search algorithm")


class MainClass(Sorting):
    def __init__(self):
        super().__init__()

    def call_sort(self, arr, algorithm):
        return self.sort(arr, algorithm)

    def call_graph_search(self, graph, start, algorithm):
        return self.graph_search(graph, start, algorithm)


# Example usage:
if __name__ == "__main__":
    main = MainClass()

    # Sorting example
    arr = [3, 6, 8, 10, 1, 2, 1]
    algorithm = "quick_sort"
    sorted_arr = main.call_sort(arr, algorithm)
    print(f"Sorted array using {algorithm}: {sorted_arr}")

    algorithm = "bubble_sort"
    sorted_arr = main.call_sort(arr, algorithm)
    print(f"Sorted array using {algorithm}: {sorted_arr}")

    algorithm = "merge_sort"
    sorted_arr = main.call_sort(arr, algorithm)
    print(f"Sorted array using {algorithm}: {sorted_arr}")

    # Graph search example
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    start_node = 'A'

    algorithm = "bfs"
    bfs_result = main.call_graph_search(graph, start_node, algorithm)
    print(f"BFS result starting from {start_node}: {bfs_result}")

    algorithm = "dfs"
    dfs_result = main.call_graph_search(graph, start_node, algorithm)
    print(f"DFS result starting from {start_node}: {dfs_result}")


