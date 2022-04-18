'''
Algorithm:
1) keep dividing the array into equal parts
2) sort the divided arrays and then merge

Time Complexity:
worst-case: O(nlogn)
average-case: O(nlogn)
best-case: O(nlogn)

Space Complexity:
O(n)
'''


def sortArray(nums):
        if(len(nums) > 1):
            mid = len(nums)//2
            left = nums[:mid]
            right = nums[mid:]

            sortArray(left)
            sortArray(right)

            lp = 0
            rp = 0
            i = 0
            
            while(lp < len(left) and rp < len(right)):
                if(left[lp] < right[rp]):
                    nums[i] = left[lp]
                    lp += 1
                else:
                    nums[i] = right[rp]
                    rp += 1
                i += 1
            
            while(lp < len(left)):
                nums[i] = left[lp]
                i += 1
                lp += 1
            
            while(rp < len(right)):
                nums[i] = right[rp]
                i += 1
                rp += 1
                
            return nums

  
x = [-3,-1,-3,1,2,4]
print(sortArray(x))
print(x)