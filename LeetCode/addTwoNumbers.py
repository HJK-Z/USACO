# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        numl1 = ""
        numl2 = ""
        
        cnt = l1
        while True:
            numl1 = str(cnt.val) + numl1
            if cnt.next == None:
                break
            cnt = cnt.next
            
            
        cnt = l2
        while True:
            numl2 = str(cnt.val) + numl2
            if cnt.next == None:
                break
            cnt = cnt.next
        
        bussy = str(int(numl1) + int(numl2))
        
        nxt = ListNode(val = bussy[0])
        for i in range(1, len(bussy)):
            crt = ListNode(val = bussy[i], next = nxt)
            nxt = crt
            
        return nxt