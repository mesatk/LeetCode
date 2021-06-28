class Solution(object):
    def getIntersectionNode(self, headA, headB):
        p = headA
        q = headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p


#### Second Solution  ####


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        p = headA
        q = headB
        lenA = 1
        lenB = 1
        while p:
            p = p.next
            lenA += 1
        while q:
            q = q.next
            lenB += 1
        p = headA
        q = headB
        for i in range(abs(lenA - lenB)):
            if lenA > lenB :
                p = p.next
            else:
                q = q.next
        
        while p != q:
            p = p.next
            q= q.next
            
        return p