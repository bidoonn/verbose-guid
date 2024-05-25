import colorama
from colorama import Fore, Back, Style

# Виведення червоного тексту
print(Fore.RED + "Цей текст червоний" + Style.RESET_ALL)

# Виведення тексту на зеленому фоні
print(Back.GREEN + "Цей текст на зеленому фоні" + Style.RESET_ALL)

# Скидання всіх змінених стилів
print("Повертаємося до звичайного тексту")
