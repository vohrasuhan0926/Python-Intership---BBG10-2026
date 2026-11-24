class Inventory:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]


# Creating an inventory object
inv = Inventory(["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"])

# Getting total number of items
print("Total items:", len(inv))

# Accessing items using indexing
print("Item at index 0:", inv[0])
print("Item at index 2:", inv[2])
print("Item at index 4:", inv[4])