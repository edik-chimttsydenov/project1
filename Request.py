import requests
from pycoingecko import CoinGeckoAPI
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt


coin="ripple"
cur="usd"
url = "https://api.coingecko.com/api/v3/simple/price"
params = {
         "ids": "ripple",
         "vs_currencies": "USD"
}


#coment

# Replace 'YOUR_API_KEY' with your actual API key
#headers = { 'x-cg-demo-api-key': 'YOUR_API_KEY' }
currencies = {
    "USD": "usd",
    "EUR": "eur",
    "JPY": "jpy",
    "GBP": "gbp",
    "AUD": "aud",
    "CAD": "cad",
    "CHF": "chf",
    "CNY": "cny",
    "RUB": "rub",
    "KZT": "kzt",
    "UZS": "uzs"
}

coints = {
    "Bitcoin": "bitcoin",
    "Ethereum": "ethereum",
    "Ripple": "ripple",
    "Litecoin": "litecoin",
    "ADA": "cardano"
}
#BTC - Bitcoin, ETH - Ethereum, XRP - Ripple, LTC - Litecoin, ADA - Cardano
s="bitcoin"
d="rub"
params["ids"]=s
params["vs_currencies"]=d
print(params["ids"])

def update_b_label(event):
    code = base_combobox.get()
    name = coints[code]
    b_label.config(text=name)


def update_t_label(event):
    # Получаем полное название целевой валюты из словаря и обновляем метку
    code = target_combobox.get()
    name = currencies[code]
    t_label.config(text=name)

window = Tk()
window.title("Курс обмена криптовалюты")
window.geometry("360x300")
Label(text="Целевая криптовалюта:").pack(padx=10, pady=5)
base_combobox = ttk.Combobox(values=list(coints.keys()))
base_combobox.pack(padx=10, pady=5)
base_combobox.bind("<<ComboboxSelected>>", update_b_label)
b_label = ttk.Label()
b_label.pack(padx=10, pady=10)




window.mainloop()

response = requests.get(url, params = params)
#response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    price = data[s][d]
    print(f"The price of {s} in USD is ${price}")
else:
    print("Failed to retrieve data from the API")


''' 
cg = CoinGeckoAPI()


ohlc = cg.get_coin_ohlc_by_id(id = "ripple", vs_currency = "usd", days = "7")
#print (ohlc)

df = pd.DataFrame(ohlc)
df.columns = ["date", "open", "high", "low", "close"]
df["date"] = pd.to_datetime(df["date"],  unit = "ms")

#df.set_index("date", inplace = True)

str1=str(df["date"])
print(len(str1))

plt.figure(figsize=(10, 5))
plt.plot(df["date"], df["close"])
plt.title("Криптовалюта")
plt.xlabel("Дата")
plt.ylabel("Цена")



plt.show()
'''
