class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 初始化进位默认为 0
        carry = 0

        # 初始化一个链表
        res = cur = ListNode(0)

        # 当 l1 和 l2 两个链表中最后一个节点中 val 相加的值大于 10 时, carry == 1 需要再次进入循环
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next

            if l2:
                carry += l2.val
                l2 = l2.next

            cur.next = ListNode(carry % 10)
            cur = cur.next

            # 获取进位, l1 和 l2 两数之和（处于 0 ~ 18 之间）, 除十并取整
            carry //= 10

        # 第一个节点为默认节点, 返回第一个节点后面所有节点
        return res.next         

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

sol = Solution()
sol.addTwoNumbers(l1, l2)