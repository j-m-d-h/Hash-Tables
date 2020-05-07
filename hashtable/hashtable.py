class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = self.capacity * [None]

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function
        """
        hash = 5381
        for e in key:
            hash = (hash * 33) + ord(e)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        self.size += 1
        if self.size >= self.capacity * 0.7:
            self.resize(self.capacity * 2)
        index = self.hash_index(key)
        node = self.storage[index]
        if node is None:
            self.storage[index] = HashTableEntry(key, value)
        else:
            while True:
                if node.key == key:
                    node.value = value
                    return
                elif node.next is None:
                    node.next = HashTableEntry(key, value)
                    return
                else:
                    node = node.next


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]
        if node is not None:
            self.storage[index] = None
            self.size -= 1
            if self.size <= self.capacity * 0.2:
                self.resize(self.capacity // 2)
            return node
        else:
            print('Key not found.')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]
        if node is None:
            return None
        else:
            while True:
                if node.key == key:
                    return node.value
                elif node.next is not None:
                    node = node.next
                else:
                    return None

    def resize(self, new_size=None):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        if new_size == None:
            new_size = self.capacity * 2
        new = HashTable(capacity=max(new_size, 8))
        for node in self.storage:
            if node is None:
                pass
            else:
                new.put(node.key, node.value)
                while node.next is not None:
                    node = node.next
                    new.put(node.key, node.value)
        self.capacity = new_size
        self.storage = new.storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
