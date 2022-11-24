import requests
import Bank
from colorama import Fore

def counter(a):
    while a != 1 and a != 2 and a != 3:
        a = int(input(Fore.RED +'Please print 1, 2 or 3: '))
    if a == 1:
        b = float(input(Fore.MAGENTA +'Print your amount of UAH: '))
        print(Fore.BLUE + f'USD = {b / USD_in_UAH}$')
        print(f'EUR = {b / EUR_in_UAH}€')
    elif a == 2:
        b = float(input(Fore.MAGENTA +'Print your amount of USD: '))
        print(Fore.BLUE + f'UAH = {b * USD_in_UAH}₴')
        print(f'EUR = {b * USD_in_UAH / EUR_in_UAH}€')
    elif a == 3:
        b = float(input(Fore.MAGENTA +'Print your amount of EUR: '))
        print(Fore.BLUE + f'USD = {b*EUR_in_UAH/USD_in_UAH}$')
        print(f'UAH = {b*EUR_in_UAH}₴')

resp = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
if resp.status_code == 200:
    bank = Bank(resp.text, features="html.parser")
    bank_list = bank.find_all("td")
    res = str(bank_list[39]).split('<td data-label="Official exchange rate">')
    res = str(res[1]).split('</td>')
    USD_in_UAH = float(res[0].replace(',', '.'))

if resp.status_code == 200:
    bank = bank_all("td")
    res = str(bank[44]).split('<td data-label="Official exchange rate">')
    res = str(res[1]).split('</td>')
    EUR_in_UAH = float(res[0].replace(',', '.'))

print(Fore.LIGHTCYAN_EX + f'USD in UAH = {USD_in_UAH}'+ Fore.RESET)
print(Fore.LIGHTCYAN_EX + f'EUR in UAH = {EUR_in_UAH}'+ Fore.RESET)
a = int(input(Fore.LIGHTMAGENTA_EX +"Choose convertor, if you neet from UAH to USD and EUR print 1, from USD to UAH and EUR print 2, from EUR to USD and UAH print 3: "+ Fore.RESET))
counter(a)