class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        last_max = arr[-1]
        
        arr[-1] = -1
        
        for i in range(len(arr)-2, -1, -1):
            temp = arr[i]
            arr[i] = last_max
            
            last_max = max(temp, last_max)
        
        return arr