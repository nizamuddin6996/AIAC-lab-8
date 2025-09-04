class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        """Add an item with the given name and price to the cart."""
        if name in self.items:
            self.items[name].append(price)
        else:
            self.items[name] = [price]

    def remove_item(self, name):
        """Remove one occurrence of the item with the given name from the cart."""
        if name in self.items:
            if self.items[name]:
                self.items[name].pop()
                if not self.items[name]:
                    del self.items[name]

    def total_cost(self):
        """Return the total cost of all items in the cart."""
        return sum(sum(prices) for prices in self.items.values())

if __name__ == "__main__":
    cart = ShoppingCart()
    while True:
        print("\nOptions: add, remove, total, quit")
        choice = input("Enter your choice: ").strip().lower()
        if choice == "add":
            name = input("Enter item name: ").strip()
            try:
                price = float(input("Enter item price: "))
                cart.add_item(name, price)
                print(f"Added {name} (${price:.2f}) to cart.")
            except ValueError:
                print("Invalid price. Please enter a number.")
        elif choice == "remove":
            name = input("Enter item name to remove: ").strip()
            cart.remove_item(name)
            print(f"Removed one occurrence of {name} from cart.")
        elif choice == "total":
            total = cart.total_cost()
            print(f"Total cost: ${total:.2f}")
        elif choice == "quit":
            print("Exiting ShoppingCart.")
            break
        else:
            print("Invalid option. Please try again.")

