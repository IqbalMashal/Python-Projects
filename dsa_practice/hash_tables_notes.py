# # Hash Table Notes
"""
Hash Table Notes
Definition:
- A hash table is a collection of key-value pairs (records).
- Keys are unique within a table.
Operations:
1. Search
2. Insert
3. Modify
4. Remove
Hash Function:
- A hash function takes a key and returns a hash value, which is an unsigned whole number.
    The run time of this function is independent of the number of records in the table, i.e., O(1) run time relative to the number of records in a table.
- To make the hash function work, we need a mathematical formula: hashvalue % capacity of array = hashIndex
- The hash formula ensures valid array index ranges from 0 to capacity - 1.
"""