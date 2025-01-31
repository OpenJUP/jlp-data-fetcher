```
# JLP Data Fetcher

📡 **Fetch and display JLP Pool & Custody data from Solana in real-time. No database required.**

---

## 🚀 Features
- Fetches **JLP Pool** and **Custody** data from the Solana blockchain.
- Uses **Solana RPC** to retrieve live data.
- **No database required**—prints data directly.
- Lightweight and async for efficient execution.

---

## 📥 Installation

### 1️⃣ Clone the repository
```sh
git clone https://github.com/OpenJUP/jlp-data-fetcher.git
cd jlp-data-fetcher
```

### 2️⃣ Set up a virtual environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

---

## 📡 Usage
Run the script to fetch and display JLP data:
```sh
python fetch_jlp_data.py
```

This will output real-time **Pool** and **Custody** data from Solana.

---

## 📜 Example Output
```
=== Pool Info ===
Timestamp: 1698654307
Pool AUM (USD): 1,500,000.0
Supply: 50,000.0
Pool Limit (USD): 3,000,000.0
Pool APR (bps): 150
Pool Realized Fee (USD): 25,000.0
Theoretical Price: 30.0

=== Custody Data ===
Token: SOL
Target Ratio (bps): 2000
Max Global Long Sizes: 100000
Max Global Short Sizes: 50000
Fees Reserves: 1000.0
Owned: 5000.0
Locked: 2000.0
Guaranteed USD: 15000.0
Global Short Sizes: 3000.0
Global Short Average Prices: 29.5
----------------------------------
```

---

## 🔧 Dependencies
- **Python 3.8+**
- `solana`
- `solders`
- `borsh-construct`
- `anchorpy`

If any dependencies are missing, install them with:
```sh
pip install -r requirements.txt
```

---

## 📝 How It Works
1. **Connects to Solana RPC** to fetch JLP Pool details.
2. **Retrieves custody asset data** for SOL, BTC, ETH, USDC, and USDT.
3. **Prints the results** in a structured format.

---

## 🤝 Contributing
We welcome contributions! To contribute:
1. **Fork** this repository.
2. **Create a feature branch** (`feature-xyz`).
3. **Submit a Pull Request** for review.

---

## 📜 License
This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

### 🌍 Stay Connected
- **GitHub:** [OpenJUP](https://github.com/OpenJUP)
- **Solana Community:** [Solana Docs](https://docs.solana.com/)