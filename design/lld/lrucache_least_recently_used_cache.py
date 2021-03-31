"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
Follow up:
Could you do get and put in O(1) time complexity?

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None
        
class LRUCache:
    def __init__(self, capacity):
        self.cache = dict()
        self.capacity = capacity
        self.left, self.right = Node(0,0), Node(0,0)
        
        #attach head and tail back to back
        self.left.next =  self.right
        self.right.prev = self.left

    def delete(self, node): #DELETE FROM HEAD
        prev, nxt = node.prev, node.next 
        prev.next = nxt
        nxt.prev = prev       
        

    def insert_at_tail(self, node): #INSERT AT END
        prev, nxt = self.right.prev, self.right.next 
        prev.next = node
        nxt.prev = node
        
        node.next = nxt
        
    
    
    def move_to_end(self, node):
        self.delete(node)
        self.insert_at_tail(node)
        
    def get(self, key):
        if key in self.cache:
            # Case: cache hit -> move to most recently used
            node = self.cache[key]
            #self.move_to_end(node)
            self.delete(node)
            self.insert_at_tail(node)
            return node.val
        else:
            return -1
        
    def put(self, key, value):
        if key in self.cache:
            #case: cache hit, remove previous entry to keep the latest in use
            self.delete(self.cache[key])
        
        new_node = Node(key, value)   #create new node
        self.cache[key] = new_node    #insert into cache
        self.insert_at_tail(self.cache[key])  #insert into Dlist
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.delete(lru)
            del self.cache[key]
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# class Node:
#     def __init__(self, key, val):
#         self.key, self.val = key, val
#         self.prev = self.next = None

# class LRUCache:

#     def __init__(self, capacity):
#         self.cap = capacity
#         self.cache = {} # map key to node
        
#         # doubly linked list
#         self.left, self.right = Node(0, 0), Node(0, 0)
#         self.left.next, self.right.prev = self.right, self.left
    
#     # remove node from list
#     def remove(self, node):
#         prev, nxt = node.prev, node.next
#         prev.next, nxt.prev = nxt, prev
    
#     # insert node at right
#     def insert(self, node):
#         prev, nxt = self.right.prev, self.right
#         prev.next = nxt.prev = node
#         node.next, node.prev = nxt, prev
        
#     def get(self, key):
#         if key in self.cache:
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])
#             return self.cache[key].val
#         return -1

#     def put(self, key, value):
#         if key in self.cache:
#             self.remove(self.cache[key])
#         self.cache[key] = Node(key, value)
#         self.insert(self.cache[key])
        
#         if len(self.cache) > self.cap:
#             # remove LRU from list and delete from hashmap
#             lru = self.left.next
#             self.remove(lru)
#             del self.cache[lru.key]
