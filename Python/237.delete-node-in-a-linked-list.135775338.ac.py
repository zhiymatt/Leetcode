#
# [237] Delete Node in a Linked List
#
# https://leetcode.com/problems/delete-node-in-a-linked-list/description/
#
# algorithms
# Easy (47.24%)
# Total Accepted:    202.5K
# Total Submissions: 428.6K
# Testcase Example:  '[0,1]\nnode at index 0 (node.val = 0)'
#
# 
# Write a function to delete a node (except the tail) in a singly linked list,
# given only access to that node.
# 
# 
# 
# Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node
# with value 3, the linked list should become 1 -> 2 -> 4 after calling your
# function.
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        pre = node
        while node.next:
            node.val = node.next.val
            pre = node
            node = node.next
        pre.next = None
