def show_result(price, tax, rate, tax_amount, total):
    """
    Print the bill with the base price, the tax
    applied and the total to pay.

    Does not return anything.
    """

    # Print the invoice title
    print()
    print("--- INVOICE ---")
    # Show the base price
    print(f"Base price:      {price:.2f} €")
    # Show the tax and its rate
    print(f"{tax} ({rate}%):      {tax_amount:.2f} €")
    # Print a line to separate the total
    print("-" * 27)
    # Show the total to pay
    print(f"Total to pay:    {total:.2f} €")
