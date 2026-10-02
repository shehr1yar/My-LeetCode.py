class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        dummyptr = dummy
        carry = 0
        while l1 or l2 or carry: #loop should remain running if carry isnt null
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            dummyptr.next = ListNode(val)
            # update pointers
            dummyptr = dummyptr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
