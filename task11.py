#leetcode 2270
#number of ways to split array


def maxi(s) -> int:
    valid = 0
    right = sum(s)
    left = 0
    
    for val in range(len(s) - 1):
        left += s[val]   
        right -= s[val]  
        if left >= right:
            valid += 1
    return valid  
            
test = [10, 4, -8, 7]          
print(maxi(test))   
