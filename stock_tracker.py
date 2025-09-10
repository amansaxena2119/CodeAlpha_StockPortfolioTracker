# Hardcoded stock prices
stock_prices = {
    "APPLE": 180,
    "TESLA": 250,
    "GOOGLE": 2700,
    "MICROSOFT": 310,
    "AMAZON": 3400,
    "TATA": 2470,
    "RELIANCE": 9200,
    "WIPRO": 1800,
    "NVIDIA": 5500,
    "INFOSYS": 1750
}

def get_investment():
    total_investment = 0
    investment_details = []

    print("Stock Tracker")
    print("Enter stock symbols and quantities (type 'done' to finish).\n")

    while True:
        stock = input("Enter stock symbol (e.g., AAPL): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("Stock not found in price list. Try again.\n")
            continue
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            price = stock_prices[stock]
            value = quantity * price
            total_investment += value
            investment_details.append((stock, quantity, price, value))
        except ValueError:
            print("Please enter a valid number for quantity.\n")

    return total_investment, investment_details

def save_to_file(investment_details, total, filename="investment_report.csv"):
    with open(filename, "w") as file:
        file.write("Stock,Quantity,Price,Total Value\n")
        for stock, qty, price, value in investment_details:
            file.write(f"{stock},{qty},{price},{value}\n")
        file.write(f"\nTotal Investment,,,{total}\n")
    print(f"\nReport saved to '{filename}'")

# Main program
total, details = get_investment()
print("\nInvestment Summary:")
for stock, qty, price, value in details:
    print(f"{stock}: {qty} shares x ${price} = ${value}")
print(f"\nTotal Investment: ${total}")

# Optional: Save to file
save_option = input("\nWould you like to save the report to a CSV file? (yes/no): ").lower()
if save_option == "yes":
    save_to_file(details, total)
else:
    print("Report not saved.")
