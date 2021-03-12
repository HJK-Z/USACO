# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    numl1 = ""
    numl2 = ""

    cnt = l1
    while l1.next != None:
        numl1 = str(cnt.val) + numl1
        cnt = next

    cnt = l2
    while cnt.next != None:
        numl2 = str(cnt.val) + numl2
        cnt = next

    print(numl1, numl2)

    bussy = str(int(numl1) + int(numl2))

    nxt = ListNode(val=bussy[0])
    for i in range(1, len(bussy)):
        crt = ListNode(val=bussy[i], next=nxt)
        nxt = crt

    return nxt

print(addTwoNumbers(ListNode(1), ListNode(2)).val)