import colorama
#проэкт "colorama"
from colorama import Fore, Back, Style

print(Fore.GREEN + 'Зелений текст без фону'+ Style.RESET_ALL)
#Fore дає змогу змінювати колір тексту

print(Back.BLACK + Fore.GREEN + 'Зелений текст на чорному фоні'+ Style.RESET_ALL)
#Back може змінювати фон тексту
print(Style.BRIGHT + Back.WHITE + Fore.BLUE +'Яскравий синій текст на білому фоні' + Style.RESET_ALL)
