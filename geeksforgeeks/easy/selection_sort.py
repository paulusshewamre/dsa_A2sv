class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)):
            sm_index = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[sm_index]:
                    sm_index = j
            if i != sm_index:
                arr[sm_index], arr[i] = arr[i], arr[sm_index]
        
                    