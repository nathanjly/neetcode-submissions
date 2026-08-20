# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        current = head
        list = []
        while current != None:
            list.append(current)
            current = current.next

        rev_list = list[::-1]
        rev_list[-1].next = None
        for i in range(len(rev_list)-1):
            rev_list[i].next = rev_list[i+1]

        return rev_list[0]
        

            
            
