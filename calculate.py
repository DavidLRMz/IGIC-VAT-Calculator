def calculate(price: float, rate: int) -> tuple[float, float]:
    """
    Calculate the tax amount and the final price.
    Args:
        price (float): The base price of the product.
        rate (int): The tax rate percentage.
    Returns:
        tuple[float, float]: The tax amount and the total, rounded to 2 decimals.
    """
    # Check if the product is tax-free
    if rate == 0:
        print("This product is tax-free.")
    # Calculate the tax amount based on the given rate
    tax_amount = round(price * rate / 100, 2)
    # Compute the final price including tax
    total = round(price + tax_amount, 2)
    # Return the computed tax and total
    return (tax_amount, total)
