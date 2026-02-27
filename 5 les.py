import colorama
from colorama import Fore, Back, Style
import inspect

#colorama.init()

print(dir(colorama))

print([name for name, value in inspect.getmembers(Fore) if name.isupper()])
print([name for name, value in inspect.getmembers(Back) if name.isupper()])
print([name for name, value in inspect.getmembers(Style) if name.isupper()])


print(Fore.RED + "Червоний")
print(Fore.BLACK + Back.GREEN + 'Зелений fon')
print(Style.RESET_ALL + Fore.BLUE + "aaaaa")
