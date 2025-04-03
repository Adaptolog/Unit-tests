from custom_list import CustomList

def main():
    lst = CustomList()
    lst.append('a')
    lst.insert('b', 1)
    print("Length:", lst.length())  # 2
    # Демонстрація всіх методів

if __name__ == "__main__":
    main()
