# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def build_bst(nums, start, end):
            if start > end:
                return None

            mid = (start + end) // 2
            
            node = TreeNode(nums[mid])
            node.left = build_bst(nums, start, mid - 1)
            node.right = build_bst(nums, mid + 1, end)
                 
            return node

        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        return build_bst(nums, 0, len(nums) - 1)
