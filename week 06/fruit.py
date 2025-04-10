def main():

    # List of fruits
    fruit_list=["pear", "banana", "apple", "mango"];
    print(f"original: {fruit_list}");

    fruit_list.reverse();
    print(f"reversed: {fruit_list}");

    index = fruit_list.index("apple");
    fruit_list.insert(index, "cherry")
    print(f"after insert: {fruit_list}");

    fruit_list.remove("banana");
    print(f"after remove: {fruit_list}");

    popped = fruit_list.pop()
    print(f"popped element: {popped}");
    print(f"after pop: {fruit_list}");

    fruit_list.sort();
    print(f"sorted: {fruit_list}");

    fruit_list.clear()
    print(f"cleared: {fruit_list}");

main()