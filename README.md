# Crypto Tracker

A small crypto price tracker built with Python. It pulls live market data from the CoinGecko API, stores it in SQLite, and shows it on a simple web page.

## What it does

- Fetches prices for Bitcoin, Ethereum, BNB, XRP, Solana and Cardano
- Cleans the data with pandas
- Marks each coin as BULLISH or BEARISH based on its 24h change
- Saves every update to a local SQLite database (`crypto_vault.db`)
- Shows everything in a table that refreshes every 60 seconds

## Stack

- **Backend:** Python, Flask, pandas, requests, SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Data source:** CoinGecko API

## Project structure

```
app.py              Flask server and /api/prices endpoint
cryptotracker.py    Data pipeline (fetch, process, save)
templates/
  index.html        Frontend page
```

## Run it

```bash
pip install flask pandas requests
python app.py
```

Then open `http://localhost:5000`.

To run only the terminal version of the pipeline:

```bash
python cryptotracker.py
```

## Note

CoinGecko's free API has rate limits, so the page refreshes once per minute.
