class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def buildList(vals: list[int]):
    origin = ListNode(0)
    head = origin
    for val in vals:
        if val:
            head.val = val
            head.next = ListNode(0)
            head = head.next
    return origin

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

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next

if __name__ == "__main__":
    l1Vals = [2,4,3]
    l1 = buildList(l1Vals)
    print(l1)
    l2Vals = [5,6,4]
    l2 = buildList(l2Vals)
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    print_out = [result.val, result.next.val, result.next.next.val]
    print(print_out)
