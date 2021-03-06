#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (33.49%)
# Total Accepted:    121.8K
# Total Submissions: 363.7K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the
# two partitions.
# 
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        pre = None
        ptr = head
        while ptr:
            if ptr.val >= x:
                break
            pre, ptr = ptr, ptr.next
        else:
            return head
        insert_position = pre
        while ptr:
            if ptr.val < x:
                if not insert_position:
                    ptr.next, pre.next = head, ptr.next
                    insert_position = head = pre = ptr
                    ptr = ptr.next
                else:
                    insert_position.next, pre.next, ptr.next = ptr, ptr.next, insert_position.next
                    ptr = pre.next
                    insert_position = insert_position.next
            else:
                pre, ptr = ptr, ptr.next
        return head

