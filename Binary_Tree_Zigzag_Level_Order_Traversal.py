'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
 

Задача "Zigzag Level Order Traversal" заключается в том, чтобы обойти бинарное дерево по уровням и вывести 
значения узлов в "зигзагообразном" порядке. Это означает, что на первом уровне значения выводятся слева направо, 
на втором уровне - справа налево, на третьем - снова слева направо, и так далее, чередуя направление обхода.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Если корень дерева равен None, возвращаем пустой список
        if not root:
            return []
        
        # Инициализируем очередь с корневым узлом
        queue = deque([root])
        # Инициализируем список для хранения результата
        result = []
        # Флаг для отслеживания направления обхода уровней
        level_order = True
        
        # Пока очередь не пуста
        while queue:
            # Определяем размер текущего уровня
            level_size = len(queue)
            # Создаем список для хранения значений узлов текущего уровня
            level = []
            
            # Для каждого узла в текущем уровне
            for _ in range(level_size):
                # Извлекаем узел из очереди
                node = queue.popleft()
                # Добавляем значение узла в список level в соответствии с направлением обхода
                if level_order:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)
                
                # Если у узла есть левый потомок, добавляем его в очередь
                if node.left:
                    queue.append(node.left)
                # Если у узла есть правый потомок, добавляем его в очередь
                if node.right:
                    queue.append(node.right)
            
            # Добавляем список level в результирующий список
            result.append(level)
            # Меняем направление обхода на противоположное
            level_order = not level_order
        
        # Возвращаем результат
        return result