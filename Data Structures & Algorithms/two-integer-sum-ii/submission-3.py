class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(numbers) - 1

        while i < j:
            l = numbers[i]
            r = numbers[j]
            t = l + r

            if t == target:
                return [i+1, j+1]
            if t > target:
                j -= 1
            else:
                i += 1
        return [-1, -1]