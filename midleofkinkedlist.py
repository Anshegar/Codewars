'''
Связанный список (linked list) - это структура данных, которая состоит из узлов, где каждый узел содержит данные 
и ссылку на следующий узел в списке. Это позволяет эффективно добавлять и удалять элементы из списка, 
поскольку не требуется перемещать все элементы при вставке или удалении.

Задача: 
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        # Конструктор узла связанного списка
        self.val = val  # значение узла
        self.next = next  # ссылка на следующий узел

class Solution:
    # Метод для нахождения среднего узла связанного списка
    # Атрибут head может либо объектом типа ListNode, либо None
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head  # Инициализируем медленный и быстрый указатели на голову списка
        # Пока быстрый указатель не достиг конца списка или следующего узла после конца списка
        while fast and fast.next:  
            slow = slow.next  # Перемещаем медленный указатель на следующий узел
            fast = fast.next.next  # Перемещаем быстрый указатель на следующий узел или на следующий узел после следующего узла
        
        # Когда быстрый указатель достиг конца списка или следующего узла после конца списка, медленный указатель указывает на средний узел
        return slow  
    
# Проверка
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()
middle_node = solution.middleNode(node1)
print(middle_node.val)  # Output: 3




vnode1 = ListNode(1)
vnode2 = ListNode(2)
vnode3 = ListNode(3)
vnode4 = ListNode(4)
vnode5 = ListNode(5)
vnode6 = ListNode(6)

vnode1.next = vnode2
vnode2.next = vnode3
vnode3.next = vnode4
vnode4.next = vnode5
vnode5.next = vnode6

solution = Solution()
middle_node = solution.middleNode(vnode1)
print(middle_node.val)  # Output: 4