from tkinter import *

import tkinter as tk 
from tkinter import messagebox
import requests

window = tk.Tk()
window.title("برنامج عثمان تحويل العملة ")
window.geometry("400x600")
window.configure(bg="#3DDDF2") 

def convert_currency():
    base_currency = (entry_base_currucy.get().upper())
    tar_currency = (target_base_currucy.get().upper())
    amourooo_currency = (entry_amount_currucy.get())
    
    if not base_currency or not tar_currency or not amourooo_currency:
        messagebox.showerror("Input Error", "Please fill all fields.")
        return
    

    url = f"https://v6.exchangerate-api.com/v6/57e1ecd925b47192cfc5ea8e/latest/{base_currency}"

    response  = requests.get(url)

    data= response.json()

    exchange_rate = data['conversion_rates'].get(tar_currency)
    
    resu = exchange_rate *float(amourooo_currency) 

    result= (f"{amourooo_currency}  {base_currency } =  {resu }  {tar_currency}  ")

    label_result.config(text=result)



label_base_currency = tk.Label(window, text="أدخل رمز العملة الأساسية (مثل USD)",font=('Helvetica', 12),bg="orange",pady=15)
label_base_currency.pack(pady=15)
entry_base_currucy= tk.Entry(window)
entry_base_currucy.pack(pady=15)

label_target_currency = tk.Label(window, text="أدخل رمز العملة المراد التحويل إليها (مثل EUR)",bg="yellow",pady=15)
label_target_currency.pack(pady=15)
target_base_currucy= tk.Entry(window)
target_base_currucy.pack(pady=15)

label_amount = tk.Label(window, text="أدخل المبلغ المراد تحويله:",pady=15)
label_amount.pack(pady=15)
entry_amount_currucy= tk.Entry(window)
entry_amount_currucy.pack(pady=15)

buttono_convert = tk.Button(window,text=" حول ",command=convert_currency,pady=15)
buttono_convert.pack(pady=15)

label_result= tk.Label(window,text=" هنا ناتج التحويل ",pady=15)
label_result.pack(pady=15)



window.mainloop()
