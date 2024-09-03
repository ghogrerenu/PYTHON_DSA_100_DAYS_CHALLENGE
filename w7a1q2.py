"""Q2. Design a class called Product with properties like name, price,
category, and quantity. Implement a constructor to initialize these
attributes.
Add methods to calculate the total price after applying a discount, ask
discount percent within that method."""

class Product:
    def __init__(self, name, price, category, quantity):
        # Initialize the attributes
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity

    def calculate_total_price(self):
        # Ask for discount percentage
        discount_percent = float(input("Enter discount percentage: "))

        # Calculate discount amount
        discount_amount = (self.price * self.quantity) * (discount_percent / 100)

        # Calculate total price after discount
        total_price = (self.price * self.quantity) - discount_amount

        return total_price

# Example usage
product = Product("Laptop", 1000, "Electronics", 2)
total_price = product.calculate_total_price()
print(f"Total price after discount: ${total_price:.2f}")

