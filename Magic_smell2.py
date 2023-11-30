import random

def discount(price):
    magic_number = random.uniform(0.1, 0.3)
    discounted_price = price - (price * magic_number)
    return discounted_price

def main():

    p = float(input("Enter the original price: "))

    m=.02
    n=10
    m=.02
    n=10
    m=.02
    n=10
    m=.02
    n=10
    m=.02
    n=10
    m=.02
    n=10
    m=.02
    n=10
    
    dp = discount(p)

    print(f"Original Price: ${p:.2f}")
    print("Discounted Price: $" + str(round(dp, 2)))

if __name__ == "__main__":
    main()
