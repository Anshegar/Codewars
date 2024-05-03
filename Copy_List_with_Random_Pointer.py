'''
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.


Как я понял:

Задача: Копирование связного списка со случайными указателями.
Условие:
Дан связный список длины n, в котором каждый узел содержит дополнительный случайный указатель, 
который может указывать на любой узел в списке или быть равным null.
Необходимо создать глубокую копию этого списка. Глубокая копия должна состоять из ровно n абсолютно новых узлов,
 где каждый новый узел имеет значение, равное значению соответствующего оригинального узла. Как next, так и random указатели новых узлов должны указывать на новые узлы в скопированном списке, так, чтобы указатели в оригинальном списке и скопированном списке представляли одно и то же состояние списка. Ни один из указателей в новом списке не должен указывать на узлы в оригинальном списке.
Например, если в оригинальном списке есть два узла X и Y, где X.random --> Y, то для соответствующих 
двух узлов x и y в скопированном списке x.random --> y.

Возвращаемое значение: Голова скопированного связного списка.

Решение:
Для решения этой задачи мы будем использовать словарь node_map, который будет хранить соответствие между 
оригинальными узлами и их копиями.

Сначала мы проходим по оригинальному списку и создаем копии всех узлов, сохраняя их в словаре node_map, 
где ключом является оригинальный узел, а значением - его копия.

Затем мы снова проходим по оригинальному списку и устанавливаем next и random указатели для каждой копии узла, 
используя словарь node_map для получения соответствующих копий узлов.

Наконец, мы возвращаем копию головного узла, которую можно получить из словаря node_map.

Таким образом, мы создаем глубокую копию связного списка со случайными указателями, сохраняя соответствие 
между оригинальными и скопированными узлами.

Ключевые моменты:
Использование словаря node_map для хранения соответствия между оригинальными и скопированными узлами.
Двухэтапный подход: сначала создаем копии узлов, затем устанавливаем next и random указатели.
Возвращаем копию головного узла, полученную из словаря node_map.
Данное решение имеет линейную временную сложность O(n), так как мы проходим по списку дважды, 
и линейную пространственную сложность O(n), так как мы используем словарь для хранения копий узлов.

'''


from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Создаем словарь для хранения соответствия оригинальных и копий узлов
        node_map = {}
        
        # Первый проход: создаем копии всех узлов и сохраняем их в словаре
        current = head
        while current:
            node_map[current] = Node(current.val)  # Создаем копию узла с таким же значением
            current = current.next

        # Второй проход: устанавливаем next и random указатели для каждой копии узла
        current = head
        while current:
            # Устанавливаем next указатель копии на копию следующего узла
            node_map[current].next = node_map.get(current.next)
            # Устанавливаем random указатель копии на копию узла, на который указывает random оригинального узла
            node_map[current].random = node_map.get(current.random)
            current = current.next

        # Возвращаем копию головного узла, полученную из словаря
        return node_map[head]