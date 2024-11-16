
#leet code problem
#add two numbers in reversed order


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  
        self.next = next 


def addTwoNumbers(l1, l2):
    
    dummy = ListNode(0)
    current = dummy 
    carry = 0 

    
    while l1 is not None or l2 is not None or carry != 0:
       
        if l1 is not None:
            val1 = l1.val
            l1 = l1.next 
        else:
            val1 = 0

        if l2 is not None:
            val2 = l2.val
            l2 = l2.next 
        else:
            val2 = 0

        
        total = val1 + val2 + carry

       
        carry = total // 10 
        digit = total % 10 

       
        current.next = ListNode(digit)
        current = current.next 

   
    return dummy.next


def create_linked_list(numbers):
    dummy = ListNode(0) 
    current = dummy 
    for number in numbers:
        current.next = ListNode(number) 
        current = current.next  
    return dummy.next 


def print_linked_list(node):
    result = []
    while node is not None:
        result.append(node.val) 
        node = node.next 
    return result


l1 = create_linked_list([2, 4, 3])  
l2 = create_linked_list([5, 6, 4])


result = addTwoNumbers(l1, l2)


print("Result:", print_linked_list(result))
