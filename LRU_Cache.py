''''
LRU Cache
Solved
Medium
Topics
Companies
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

'''



class Node:
    def __init__(self, key, value):
        """
        Инициализирует новый узел в двусвязном списке.

        Аргументы:
            key (int): Ключ, связанный с узлом.
            value (int): Значение, связанное с узлом.
        """
        self.key = key
        self.value = value
        self.prev = None  # Указатель на предыдущий узел в списке
        self.next = None  # Указатель на следующий узел в списке

class LRUCache:
    def __init__(self, capacity: int):
        """
        Инициализирует LRU-кэш с заданной вместимостью.

        Аргументы:
            capacity (int): Максимальное количество пар ключ-значение, которое может хранить кэш.
        """
        self.capacity = capacity
        self.cache = {}  # Словарь для хранения пар ключ-значение
        self.head = Node(0, 0)  # Фиктивный узел-голова двусвязного списка
        self.tail = Node(0, 0)  # Фиктивный узел-хвост двусвязного списка
        self.head.next = self.tail  # Связываем голову и хвост
        self.tail.prev = self.head  # Связываем хвост и голову

    def get(self, key: int) -> int:
        """
        Извлекает значение, связанное с заданным ключом.

        Аргументы:
            key (int): Ключ, для которого нужно извлечь значение.

        Возвращает:
            int: Значение, связанное с ключом, или -1, если ключ не существует.
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]  # Получаем узел, связанный с ключом
        self.remove(node)  # Удаляем узел из его текущей позиции
        self.add(node)  # Добавляем узел в конец списка (наиболее недавно используемый)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Добавляет или обновляет значение, связанное с заданным ключом.
        Если количество ключей превышает вместимость, удаляется наименее недавно используемый ключ.

        Аргументы:
            key (int): Ключ, с которым нужно связать значение.
            value (int): Значение, которое нужно связать с ключом.
        """
        if key in self.cache:
            self.remove(self.cache[key])  # Удаляем существующий узел, связанный с ключом
        node = Node(key, value)  # Создаем новый узел с заданным ключом и значением
        self.add(node)  # Добавляем новый узел в конец списка (наиболее недавно используемый)
        self.cache[key] = node  # Добавляем пару ключ-узел в словарь кэша
        if len(self.cache) > self.capacity:
            node = self.head.next  # Получаем наименее недавно используемый узел (голова списка)
            self.remove(node)  # Удаляем наименее недавно используемый узел из списка
            del self.cache[node.key]  # Удаляем пару ключ-узел из словаря кэша

    def remove(self, node):
        """
        Удаляет заданный узел из двусвязного списка.

        Аргументы:
            node (Node): Узел, который нужно удалить.
        """
        prev = node.prev
        next = node.next
        prev.next = next  # Обновляем указатель 'next' предыдущего узла
        next.prev = prev  # Обновляем указатель 'prev' следующего узла

    def add(self, node):
        """
        Добавляет заданный узел в конец двусвязного списка (наиболее недавно используемый).

        Аргументы:
            node (Node): Узел, который нужно добавить.
        """
        prev = self.tail.prev
        prev.next = node  # Обновляем указатель 'next' предыдущего узла
        self.tail.prev = node  # Обновляем указатель 'prev' узла-хвоста
        node.prev = prev  # Обновляем указатель 'prev' нового узла
        node.next = self.tail  # Обновляем указатель 'next' нового узла