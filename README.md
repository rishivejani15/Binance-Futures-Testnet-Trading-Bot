# 🟡 Binance Futures Testnet Trading Bot

A Python-based trading bot that connects to the Binance Futures Testnet API to place various types of cryptocurrency orders via a command-line interface.

## 🚀 Features

* ✅ Place **Market Orders**
* ✅ Place **Limit Orders**
* ✅ Place **Stop-Market Orders**
* ✅ Log order activity in a structured log file
* ✅ CLI menu-based interface

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/binance-futures-bot.git
cd binance-futures-bot
```

### 2. Create a Virtual Environment (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuration

### 1. Set Up Your Binance API Keys

Create a `.env` file or use `config.py`:

```python
API_KEY = "your_testnet_api_key"
API_SECRET = "your_testnet_api_secret"
BASE_URL = "https://testnet.binancefuture.com"  # Futures Testnet URL
```

Make sure your API key has **Futures Trading** enabled.

---

## 🛆 Project Structure

```
binance-futures-bot/
│
├── main.py                 # CLI Interface
├── bot.py                  # Core bot logic
├── config.py               # API keys & base URL
├── utils.py                # Logger setup
├── logs/
│   └── bot.log             # Log file for all activities
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🔤️ How to Run

```bash
python main.py
```

Then follow the CLI prompts:

```
Welcome to Binance Bot
1. Market Order
2. Limit Order
3. Stop-Market
4. OCO Order
Enter your choice: ...
```

---

## 🧠 Order Types Explained

* **Market**: Execute immediately at current market price.
* **Limit**: Set a price at which you want to buy/sell.
* **Stop-Market**: Executes a market order when stop price is hit.
* **OCO (Spot Only)**: Combines a limit order and a stop-limit order.

---

## 📝 Logs

All order actions and errors are saved to `logs/bot.log` for traceability and debugging.

---

## 🧪 Testnet Information

This bot uses the [Binance Futures Testnet](https://testnet.binancefuture.com/) for development and testing purposes. You can get free testnet funds from the [Binance Testnet Faucet](https://testnet.binancefuture.com/futures/BTCUSDT).

---


## 🧑‍💻 Author

**Rishi Vejani**

---

## 📄 License

MIT License – Use freely, but at your own risk. Binance trading involves risk.
