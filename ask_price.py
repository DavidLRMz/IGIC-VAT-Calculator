def ask_price(message: str) -> float:
    """
    Ask the user for a price using the given message.
    Keeps asking until the price is not negative.
    Returns the price as a float.
    """
    price = float(input(message))
    while price < 0:
        print("The price cannot be negative.")
        price = float(input(message))
    print(f"Price entered: {price:.2f} €")
    return price
