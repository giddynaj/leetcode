class ListNode(object):
    def __init__(self, x):
        self.val = x 
        self.next = None 

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l2 else None)
            l2 = (l2.next if l2 else None)

        return result.next
    
if __name__ == "__main__":
    #l1 = [2,4,3]
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4) 
    #l2 = [5,0,8]
    solution = Solution()
    print(solution.addTwoNumbers(l1, l2))
