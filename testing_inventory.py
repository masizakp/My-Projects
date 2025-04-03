
from tabulate import tabulate

shoe_list = []
count = 0
with open("inventory.txt", "r", encoding='utf-8') as inventory_file:
    lines = inventory_file.readlines()
    for line in lines:
        parts = line.strip().split(",")
        for i in range (len(parts)):
            shoe_list.append(parts[i])
            
    print(shoe_list)
