# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        root_node = ListNode()
        current_node = root_node
        for node in lists:
            if (node != None): 
                heapq.heappush(heap, (node.val, node))
        while (len(heap) > 0):
            (val, node) = heapq.heappop(heap)
            current_node.next = ListNode(val)
            current_node = current_node.next
            if (node.next != None):
                heapq.heappush(heap, (node.next.val, node.next))
        if (root_node.next == None): 
            return None
        else: 
            return root_node.next
            
