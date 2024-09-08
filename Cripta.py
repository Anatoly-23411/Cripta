from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests

# Получаем полное название криптовалюты из словаря currencies1  и обновляем метку
def update_base_label(_):
    code = base_combobox.get()
    name = currencies1[code]
    base_label.config(text=name)

# Получаем полное название целевой валюты из словаря currencies2 и обновляем метку
def update_target_label(_):
    code = target_combobox.get()
    name = currencies2[code]
    target_label.config(text=name)


def exchange():
    target_code = target_combobox.get()
    base_code = base_combobox.get()
    if target_code and base_code:
        try:
            response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum%2Cbitcoin"
                                    "%2Cnyan-meme-coin%2Coctaspace%2Corbitpad%2Cvopo%2Cztx%2Ctoro&vs_currencies=usd%2Crub&x_cg_demo_api_key=CG-VWpzJKoa2nSsu3fzD1Ayr8wU")
            response.raise_for_status()
            data = response.json()
            exchange_rate = data[base_code][target_code]
            base = currencies1[base_code]
            target = currencies2[target_code]
            mb.showinfo("Курс обмена", f"Курс {exchange_rate: 1f} {target} за 1 {base}")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка {e}")
    else:
        mb.showwarning("Внимание", "Выберите код криптовалюты (валюты)")

# Словарь кодов криптовалют и их  названий
currencies1 = {
    "bitcoin": 'Bitcoin',
    "ethereum": 'Ethereum',
    "nyan-meme-coin": 'Nyan Meme Coin',
    "octaspace": 'OctaSpace',
    "orbitpad": 'Orbitpad',
    "vopo": 'VOPO',
    "ztx": 'ZTX',
    "toro": 'TORO'
}

# Словарь кодов целевых валют и их полных названий
currencies2 = {
    "rub": 'Российский рубль',
    "usd": 'Доллар США'
}

# Создание графического интерфейса
window = Tk()
window.title("Курсы обмена криптовалют")
window.geometry("360x360")

Label(text="Криптовалюта", foreground="#4310c9", font="Arial12").pack(padx=10, pady=10)
base_combobox = ttk.Combobox(values=list(currencies1.keys()))
base_combobox.pack(padx=10, pady=10)
base_combobox.bind("<<ComboboxSelected>>", update_base_label)
base_label = ttk.Label(foreground="#de09e7", font="_")
base_label.pack(padx=10, pady=10)

Label(text="Целевая валюта", foreground="#4310c9", font="Arial12").pack(padx=10, pady=10)
target_combobox = ttk.Combobox(values=list(currencies2.keys()))
target_combobox.pack(padx=10, pady=10)
target_combobox.bind("<<ComboboxSelected>>", update_target_label)
target_label = ttk.Label(foreground="#de09e7", font="_")
target_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена криптовалют", command=exchange).pack(padx=10, pady=10)
window.mainloop()

