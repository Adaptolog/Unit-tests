from custom_list import CustomList

def main():
    print("Creating list...")
    lst = CustomList()
    
    print("\nAppending elements:")
    lst.append('a')
    lst.append('b')
    lst.append('c')
    print(f"Length: {lst.length()}")  # 3
    
    print("\nInserting 'd' at position 1:")
    lst.insert('d', 1)
    print(f"Element at index 1: {lst.get(1)}")  # d
    
    print("\nDeleting element at index 2:")
    print(f"Deleted: {lst.delete(2)}")  # b
    print(f"New length: {lst.length()}")  # 3
    
    print("\nCloning list:")
    clone = lst.clone()
    clone.append('e')
    print(f"Original length: {lst.length()}")  # 3
    print(f"Clone length: {clone.length()}")  # 4
    
    print("\nReversing list:")
    lst.reverse()
    print(f"First element after reverse: {lst.get(0)}")  # c
    
    print("\nFinding first 'd':")
    print(f"Index: {lst.findFirst('d')}")  # 1
    
    print("\nClearing list:")
    lst.clear()
    print(f"Length after clear: {lst.length()}")  # 0

if __name__ == "__main__":
    main()
