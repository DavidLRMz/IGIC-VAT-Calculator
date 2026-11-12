RATES: dict[str, dict[str, int]] = {
    "VAT":  {"standard": 21, "reduced": 10, "super-reduced": 4},
    "IGIC": {"standard": 7,  "reduced": 3,  "zero rate": 0},
}

if __name__ == "__main__":
  price = ask_price("Enter the price before taxes: ")
  # Let the user choose the tax and its rate
  tax, rate = choose_tax(RATES)
  # Calculate the tax amount and the total price
  tax_amount, total = calculate(price, rate)
  # Show the invoice
  show_result(price, tax, rate, tax_amount, total)
