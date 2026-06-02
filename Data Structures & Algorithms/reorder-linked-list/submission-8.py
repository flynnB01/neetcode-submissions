# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next

        left, right = 0, len(arr) - 1
        while left < right:
            arr[left].next = arr[right]
            left += 1
            if left == right:
                break
            arr[right].next = arr[left]
            right -= 1

        arr[left].next = None