class CurrencyConverter:
    def __init__(self, usd_to_uah):
        self.usd_to_uah = usd_to_uah

    def convert_to_usd(self, amount):
        return amount / self.usd_to_uah

if __name__ == "__main__":

    usd_to_uah = 39
    converter = CurrencyConverter(usd_to_uah)

    try:
        amount_uah = float(input("Введіть кількість валюти своєї країни (гривень): "))
        amount_usd = converter.convert_to_usd(amount_uah)
        print(f"Відповідна сума в доларах США: {amount_usd:.2f} USD")
    except ValueError:
        print("Будь ласка, введіть коректне число.")
