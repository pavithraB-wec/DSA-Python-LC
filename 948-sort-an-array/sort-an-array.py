class Solution(object):
    def sortArray(self, nums):
        n = len(nums)
        
        # Iterative heapify ensures strict O(1) space with no stack overflow
        def heapify(heap_size, root_idx):
            while True:
                largest = root_idx
                left = 2 * root_idx + 1
                right = 2 * root_idx + 2
                
                if left < heap_size and nums[left] > nums[largest]:
                    largest = left
                    
                if right < heap_size and nums[right] > nums[largest]:
                    largest = right
                    
                if largest != root_idx:
                    nums[root_idx], nums[largest] = nums[largest], nums[root_idx]
                    root_idx = largest  
                else:
                    break

        # Step 1: Build a max-heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)
            
        # Step 2: Extract elements from the heap one by one
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]  # Correct element-wise swap
            heapify(i, 0)  
            
        return nums
