#leetcode 1422  
#maximum score after splitting a string


def solution(s: str):
    zero = 0
    one = s.count("1")
    res = 0
    
    for val in range(len(s) - 1):
        if s[val] == "0":
            zero += 1
        else:
            one -= 1
        res = max(res, zero + 1)    
                
    
    return res


test = "100100"

print(solution(test))