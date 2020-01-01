class KthLargest: #TLE

    def __init__(self, k: int, nums: List[int]):
        # arr = self.build_max_heap(nums)
        # print(arr)
        # self.arr = arr
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        arr = self.build_max_heap(self.nums)
        sorted_arr = self.heap_sort_desc(arr)
        # print(sorted_arr[self.k-1])
        return sorted_arr[self.k-1]

    def max_heapify(self, arr: List[int], i: int):
        # print(arr)
        left = 2*i+1
        right = 2*i+2
        largest = i
        l = len(arr)-1
        if left <= l and arr[left] > arr[i]:
            largest = left
        if right <= l and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.max_heapify(arr, largest)

    def build_max_heap(self, arr: List[int]) -> List[int]:
        half = (len(arr)//2)
        for i in reversed(range(half)):
            # print(i)
            self.max_heapify(arr, i)
        return arr

    def heap_sort_desc(self,arr):
        arr = arr.copy()
        self.build_max_heap(arr)
        sorted_arr = []
        for _ in range(len(arr)):
            arr[0], arr[-1] = arr[-1], arr[0]
            sorted_arr.append(arr.pop())
            self.max_heapify(arr, 0)

        return sorted_arr


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
