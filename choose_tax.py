def choose_tax(rates: dict[str, dict[str, int]]) -> tuple[str, int]:

Docstring explaining shortly what the function does.

    """
    Ask the user which tax to apply and which rate to use.
    Receives a dictionary with the available taxes and rates.
    Returns the tax name (str) and the rate (int).
    """
    tax = input(f"Which tax? {list(rates)}: ").upper()
    while tax not in rates:
        tax = input(f"Invalid option. Choose one of {list(rates)}: ").upper()

