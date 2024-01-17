import math


# Product class to store product details
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 0
        self.is_gift_wrapped = False


# Discount class to store discount details
class Discount:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


def apply_discount(subtotal, product_quantities):
    discounts = [
        Discount("flat_10_discount", 10.0) if subtotal > 200.0 else None,
        Discount("bulk_5_discount", 5.0) if any(quantity > 10 for quantity in product_quantities) else None,
        Discount("bulk_10_discount", 10.0) if sum(product_quantities) > 20 else None,
        Discount("tiered_50_discount", 50.0) if sum(product_quantities) > 30 and any(
            quantity > 15 for quantity in product_quantities) else None
    ]

    applicable_discounts = [discount for discount in discounts if discount is not None]

    if applicable_discounts:
        return max(applicable_discounts, key=lambda discount: discount.amount)
    else:
        return None


def main():
    # Product catalog
    catalog = [Product("Product A", 20.0),
               Product("Product B", 40.0),
               Product("Product C", 50.0)]

    # Cart details
    subtotal = 0.0
    product_quantities = []

    # Get quantity and gift wrap information for each product
    for product in catalog:
        product.quantity = int(input(f"Enter the quantity of {product.name}: "))
        product.is_gift_wrapped = bool(int(input(f"Is {product.name} wrapped as a gift? (1 for Yes, 0 for No): ")))

        subtotal += product.quantity * product.price
        product_quantities.append(product.quantity)

    # Apply discounts
    applied_discount = apply_discount(subtotal, product_quantities)

    # Calculate gift wrap fee
    gift_wrap_fee = sum(
        product.quantity for product in catalog if product.is_gift_wrapped) * 1.0  # Gift wrap fee per unit is $1

    # Calculate shipping fee
    shipping_fee = math.ceil(sum(product.quantity for product in catalog) / 10.0) * 5.0

    # Calculate total
    total_discount = applied_discount.amount if applied_discount else 0.0
    total = subtotal - total_discount + gift_wrap_fee + shipping_fee

    # Display details
    print("\nProduct Details:")
    for product in catalog:
        print(f"{product.name}: {product.quantity} units - ${product.quantity * product.price}")

    print(f"\nSubtotal: ${subtotal:.2f}")

    if applied_discount:
        print(f"Discount Applied: {applied_discount.name} = ${total_discount:.2f}")

    print(f"Shipping Fee: ${shipping_fee:.2f}")
    print(f"Gift Wrap Fee: ${gift_wrap_fee:.2f}")
    print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()
