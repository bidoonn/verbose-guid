import requests
import sqlite3
from datetime import datetime

# Ваш URL для отримання погоди
weather_url = "https://pogodnik.com/uk/1834-pogoda-v-lvovi-ukrayina/month"

# Отримання погоди з сайту
def get_weather():
    try:
        response = requests.get(weather_url)
        response.raise_for_status()
        # Знайдемо температуру на сторінці
        temperature_start = response.text.find("Температура:")
        if temperature_start != -1:
            temperature_end = response.text.find("°C", temperature_start)
            if temperature_end != -1:
                temperature = response.text[temperature_start:temperature_end + 2]
                return temperature
        print("Не вдалося знайти температуру на сторінці")
        return None
    except requests.RequestException as e:
        print(f"Помилка при отриманні погоди: {e}")
        return None

# Збереження даних до бази даних SQLite
def save_to_database(temperature):
    try:
        conn = sqlite3.connect("weather.db")
        cursor = conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO weather (timestamp, temperature) VALUES (?, ?)", (timestamp, temperature))
        conn.commit()
        conn.close()
        print(f"Дані збережено: {timestamp}, Температура: {temperature}")
    except sqlite3.Error as e:
        print(f"Помилка при збереженні даних: {e}")

if __name__ == "__main__":
    temperature = get_weather()
    if temperature:
        save_to_database(temperature)
