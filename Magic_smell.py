def apply_discount(original_price):
    discounted_price = original_price - (original_price * 0.2)
    return discounted_price

def main():
    original_price = float(input("Enter the original price: "))
    discounted_price = apply_discount(original_price)

    print(f"Original Price: ${original_price:.2f}")
    print(f"Discounted Price: ${discounted_price:.2f}")

if __name__ == "__main__":
    main()

#     def apply_discount(original_price):
#     discounted_price = original_price - (original_price * 0.2)
#     return discounted_price

# def main():
#     original_price = float(input("Enter the original price: "))
#     discounted_price = apply_discount(original_price)

#     print(f"Original Price: ${original_price:.2f}")
#     print(f"Discounted Price: ${discounted_price:.2f}")

# if __name__ == "__main__":
#     main()

#     def apply_discount(original_price):
#     discounted_price = original_price - (original_price * 0.2)
#     return discounted_price
