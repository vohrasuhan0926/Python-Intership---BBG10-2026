def process_order(order):
    try:
        item = order["item"]
        price = order["price"]

    except KeyError:
        print("Error: Missing required key in order dictionary.")

    else:
        print("Order Item:", item)
        print("Order Price:", price)

    finally:
        print("Processing complete")


# Example 1: Valid order
process_order({"item": "Laptop", "price": 50000})

print("----------------")

# Example 2: Missing key
process_order({"item": "Laptop"})