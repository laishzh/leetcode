#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printlist(head):
    while head != None:
        print(head.val)
        head = head.next

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        newlist = ListNode(0)
        p = newlist
        while (head != None):
            curhead = head
            i = 1
            while (head.next != None and i < k):
                head = head.next
                i += 1

            if i == k:
                (curhead, curtail) = self.reverseNodes(curhead)
            p.next = curhead
            if i == k:
                p = curtail

        newlist = newlist.next
        return newlist
    # @return (head, tail)
    def reverseNodes(self, head):
        tail = head
        p = tail
        head = head.next
        tail.next = None
        while head != None:
            q = head
            head = head.next
            q.next = p
            p = q
        head = p
        printlist(head)
        return (head, tail)

solution = Solution()

lists = []
for i in reversed(range(1, 6)):
    node = ListNode(i)
    if (len(lists) > 0):
        node.next = lists[-1]
    lists.append(node)
head = lists[-1]

printlist( solution.reverseKGroup(head, 2) )
printlist( solution.reverseKGroup(head, 3) )
