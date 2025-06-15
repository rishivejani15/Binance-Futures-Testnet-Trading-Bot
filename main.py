from bot import BasicBot
from config import API_KEY, API_SECRET

def get_input(prompt, cast_type=str):
    while True:
        try:
            return cast_type(input(prompt))
        except ValueError:
            print("Invalid input. Please try again.")

def main():
    bot = BasicBot(API_KEY, API_SECRET, testnet=True)

    print("Welcome to Binance Futures Testnet Trading Bot")
    print("Choose order type:\n1. Market\n2. Limit\n3. Stop-Limit")
    order_type = get_input("Enter choice (1/2/3): ", int)

    symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY/SELL): ").upper()
    quantity = get_input("Enter quantity: ", float)

    if order_type == 1:
        result = bot.place_market_order(symbol, side, quantity)
    elif order_type == 2:
        price = get_input("Enter limit price: ", float)
        result = bot.place_limit_order(symbol, side, quantity, price)
    elif order_type == 3:
        stop_price = get_input("Enter stop price: ", float)
        result = bot.place_stop_limit_order(symbol, side, quantity, stop_price)
    else:
        print("Invalid order type selected.")
        return

    if result:
        print("\n✅ Order Placed Successfully:")
    else:
        print("\n❌ Order Failed. Check logs for details.")

if __name__ == "__main__":
    main()
