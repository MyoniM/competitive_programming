#User function Template for python3

class Solution: 
    def select(self, arr, i):
        min_indx = i
        for i in range(i, len(arr) -1):
            if arr[i+1] < arr[min_indx]:
                min_indx = i+1
        return min_indx
        
    def selectionSort(self, arr,n):
        for i in range(len(arr)):
            min_indx = self.select(arr,i)
            if arr[min_indx] < arr[i]:
                temp = arr[i]
                arr[i] = arr[min_indx]
                arr[min_indx] = temp
                