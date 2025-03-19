import math

items = int(input("Enter the number of manufacturing items:" ))
items_per_box = int(input("Enter the number of items per box:" ))

boxes_needed = math.ceil(items / items_per_box)

print(f"You will need{boxes_needed} boxes to ship {items} items.")