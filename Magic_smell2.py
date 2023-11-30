import random

def discount(price):
    # Magic number not clear
    magic_number = random.uniform(0.1, 0.3)
    discounted_price = price - (price * magic_number)
    return discounted_price

def main():
    # Single-letter variable names
    p = float(input("Enter the original price: "))
    
    # Inconsistent variable naming
    mn = 0.2

    dp = discount(p)

    print(f"Original Price: ${p:.2f}")
    # Using f-string unnecessarily
    print("Discounted Price: $" + str(round(dp, 2)))

if __name__ == "__main__":
    main()
